# Test kontrolny: q_i = F(p_i) dla losowego wymiernego F z K2 -> układ musi mieć punkt wymierny.
import itertools
P=[(-1,-1),(1,-1),(1,1),(-1,1),(2,2)]
t=lambda w:(w[0],w[1]+w[0]^2)
af=lambda M,v:(lambda w:(M[0]*w[0]+M[1]*w[1]+v[0],M[2]*w[0]+M[3]*w[1]+v[1]))
A0=af([2,1,1,-1],[1,0]);A1=af([1,3,-1,2],[0,1]);A2=af([1,0,2,1],[-1,2])
Q=[A2(t(A1(t(A0(p))))) for p in P]
R=PolynomialRing(QQ,'s,k,S,K,a,b,c,d,e,f,z')
s,k,S,K,a,b,c,d,e,f,z=R.gens()
norm=lambda pt,ch,s,k:(pt[0]+s*pt[1],k*pt[1]) if ch==0 else (pt[1],k*pt[0])
for ch0,ch2 in itertools.product([0,1],[0,1]):
    eqs=[]
    for p,q in zip(P,Q):
        r=t(af([a,b,c,d],[e,f])(t(norm(p,ch0,s,k))))
        qq=norm(q,ch2,S,K); eqs+=[r[0]-qq[0],r[1]-qq[1]]
    eqs.append(z*k*K*(a*d-b*c)-1)
    if ch0: eqs.append(s)
    if ch2: eqs.append(S)
    I=R.ideal(eqs); dm=I.dimension()
    print(ch0,ch2,"dim",dm, "punkty QQ:", len(I.variety(QQ)) if dm==0 else "-")
