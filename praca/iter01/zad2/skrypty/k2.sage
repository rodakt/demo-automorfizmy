# Klasa K2: a2∘t∘a1∘t∘a0, t=(x,y+x^2). Cechowanie: a0 = (alpha(p), k*beta(p)), a2^{-1} analogicznie,
# alpha = x+s*y (karta 0) lub y (karta 1), beta = y (karta 0) lub x (karta 1). a1 pełne (6 parametrów).
import itertools, sys
P=[(-1,-1),(1,-1),(1,1),(-1,1),(2,2)]
Q=[(1,1),(-1,1),(-1,-1),(2,2),(1,-1)]
R=PolynomialRing(QQ,'s,k,S,K,a,b,c,d,e,f,z',order='degrevlex')
s,k,S,K,a,b,c,d,e,f,z=R.gens()
def norm(pt,ch,s,k):
    X,Y=pt
    return (X+s*Y, k*Y) if ch==0 else (Y, k*X)
for ch0,ch2 in itertools.product([0,1],[0,1]):
    eqs=[]
    for p,q in zip(P,Q):
        u=norm(p,ch0,s,k); w=(u[0],u[1]+u[0]^2)
        v=(a*w[0]+b*w[1]+e, c*w[0]+d*w[1]+f); r=(v[0],v[1]+v[0]^2)
        qq=norm(q,ch2,S,K)
        eqs+= [r[0]-qq[0], r[1]-qq[1]]
    eqs.append(z*k*K*(a*d-b*c)-1)
    extra=[]
    if ch0==1: extra.append(s)
    if ch2==1: extra.append(S)
    I=R.ideal(eqs+extra)
    G=I.groebner_basis()
    print("karta",ch0,ch2,"dim",I.dimension(),"GB",list(G) if len(G)<15 else len(G)); sys.stdout.flush()
    if I.dimension()==0:
        print(" vdim",I.vector_space_dimension())
        print(" punkty QQ:",I.variety(QQ))
        try:
            print(" punkty QQbar (liczba):",len(I.variety(QQbar)))
        except Exception as ex: print(" QQbar err",ex)
    elif I.dimension()>0:
        for J in I.minimal_associated_primes(): print("  prime",J.dimension(),J.gens())
    sys.stdout.flush()
