# Niezalezna enumeracja nad F_p: czy istnieja a0,a2 afiniczne i a1 afiniczne z
# a1(t(a0 p_i)) = t^{-1}(a2^{-1} q_i), t=(x,y+x^2). Cechowanie: a0, b=a2^{-1} jako
# reprezentanci warstw B\Aff, B={(cx+e, c^2y+lx+f)} (B normalizuje t z obu stron).
# Reprezentanci czesci liniowej: [[1,s],[0,e]] (e!=0) lub [[0,1],[d,0]] (d!=0); translacja 0.
# a1 wyznaczane algebra liniowa mod p (pelne przeszukanie jadra gdy rzad<3).
import sys, itertools
P=[(-1,-1),(1,-1),(1,1),(-1,1),(2,2)]
Q=[(1,1),(-1,1),(-1,-1),(2,2),(1,-1)]
def reps(p):
    for s in range(p):
        for e in range(1,p): yield ((1,s),(0,e))
    for d in range(1,p): yield ((0,1),(d,0))
def app(M,v,p): return ((M[0][0]*v[0]+M[0][1]*v[1])%p,(M[1][0]*v[0]+M[1][1]*v[1])%p)
def solve(U,W,p):
    # rozwiazania r (3-wektor) U r = W; zwraca (r0, baza jadra) albo None
    A=[list(U[i])+[W[i]] for i in range(len(U))]; n=3; piv=[]; r=0
    for c in range(n):
        k=next((i for i in range(r,len(A)) if A[i][c]%p),None)
        if k is None: continue
        A[r],A[k]=A[k],A[r]; inv=pow(A[r][c],p-2,p); A[r]=[x*inv%p for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]%p:
                f=A[i][c]; A[i]=[(x-f*y)%p for x,y in zip(A[i],A[r])]
        piv.append(c); r+=1
    if any(A[i][n]%p for i in range(r,len(A))): return None
    x0=[0]*n
    for i,c in enumerate(piv): x0[c]=A[i][n]
    free=[c for c in range(n) if c not in piv]; ker=[]
    for f in free:
        v=[0]*n; v[f]=1
        for i,c in enumerate(piv): v[c]=(-A[i][f])%p
        ker.append(v)
    return x0,ker
def count(p,P,Q):
    sols=0
    for M0 in reps(p):
        U=[]
        for pt in P:
            a=app(M0,pt,p); U.append((a[0],(a[1]+a[0]**2)%p,1))
        for Mb in reps(p):
            W=[]
            for pt in Q:
                b=app(Mb,pt,p); W.append((b[0],(b[1]-b[0]**2)%p))
            r1=solve(U,[w[0] for w in W],p)
            if r1 is None: continue
            r2=solve(U,[w[1] for w in W],p)
            if r2 is None: continue
            # przeszukaj warstwy rozwiazan, warunek det a1 != 0
            for c1 in itertools.product(range(p),repeat=len(r1[1])):
                v1=[(r1[0][j]+sum(c*k[j] for c,k in zip(c1,r1[1])))%p for j in range(3)]
                for c2 in itertools.product(range(p),repeat=len(r2[1])):
                    v2=[(r2[0][j]+sum(c*k[j] for c,k in zip(c2,r2[1])))%p for j in range(3)]
                    if (v1[0]*v2[1]-v1[1]*v2[0])%p: sols+=1
    return sols
if __name__=="__main__":
    for p in map(int,sys.argv[1:]):
        print(p,count(p,P,Q),flush=True)
