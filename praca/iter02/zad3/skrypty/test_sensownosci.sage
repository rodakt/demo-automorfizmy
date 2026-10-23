# Test sensownosci: rozwiazania ukladu K2 (karta (0,0) z iter01/zad2/k2_szczegoly.sage) nad ciałami liczbowymi
# Kodowanie z iter01: a0(x,y)=(x+s*y, k*y); t(x,y)=(x,y+x^2); a1(x,y)=(a*x+b*y+e, c*x+d*y+f);
# warunek: t(a1(t(a0(p)))) = A2inv(q), A2inv(X,Y)=(X+S*Y, K*Y); stąd F = A2inv^{-1} ∘ t ∘ a1 ∘ t ∘ a0.
P=[(-1,-1),(1,-1),(1,1),(-1,1),(2,2)]
Q=[(1,1),(-1,1),(-1,-1),(2,2),(1,-1)]
R=PolynomialRing(QQ,'z,a,b,c,d,e,f,S,K,k,s',order='lex')
z,a,b,c,d,e,f,S,K,k,s=R.gens()
eqs=[]
for p,q in zip(P,Q):
    u=(p[0]+s*p[1],k*p[1]); w=(u[0],u[1]+u[0]^2)
    v=(a*w[0]+b*w[1]+e,c*w[0]+d*w[1]+f); r=(v[0],v[1]+v[0]^2)
    eqs+=[r[0]-(q[0]+S*q[1]), r[1]-K*q[1]]
eqs.append(z*k*K*(a*d-b*c)-1)
I=R.ideal(eqs)
print("dim",I.dimension(),"deg",I.vector_space_dimension())
T.<x>=QQ[]
for name,pol in [("kwadr",15*x^2+38*x-1),("kub",3*x^3+39*x^2+29*x+9)]:
    L.<r>=NumberField(pol)
    if name=="kwadr":
        print("disc", pol.discriminant(), "L ~ Q(sqrt(94))?", L.is_isomorphic(QuadraticField(94)))
    V=I.variety(L)
    print("===",name,"liczba punktów nad L:",len(V))
    for pt in V:
        vals={str(kk):vv for kk,vv in pt.items()}
        print("punkt:",vals)
        A.<X,Y>=PolynomialRing(L)
        vs=lambda n: L(vals[n])
        a0=(X+vs('s')*Y, vs('k')*Y)
        a0i=(X-vs('s')/vs('k')*Y, Y/vs('k'))
        tt=(X,Y+X^2); ti=(X,Y-X^2)
        a1=(vs('a')*X+vs('b')*Y+vs('e'), vs('c')*X+vs('d')*Y+vs('f'))
        M=matrix(L,[[vs('a'),vs('b')],[vs('c'),vs('d')]]); Mi=M.inverse()
        a1i=tuple(Mi[i,0]*(X-vs('e'))+Mi[i,1]*(Y-vs('f')) for i in range(2))
        a2=(X-vs('S')/vs('K')*Y, Y/vs('K'))       # odwrotność (X+S*Y, K*Y)
        a2i=(X+vs('S')*Y, vs('K')*Y)
        comp=lambda g,h: tuple(gi(h[0],h[1]) for gi in g)   # g∘h
        F=a0
        for g in [tt,a1,tt,a2]: F=comp(g,F)
        G=a2i
        for g in [ti,a1i,ti,a0i]: G=comp(g,G)
        ok_pts=all(F[0](*p)==q[0] and F[1](*p)==q[1] for p,q in zip(P,Q))
        FG=comp(F,G); GF=comp(G,F)
        print("F(p_i)=q_i:",ok_pts,"| F∘G=id:",FG==(X,Y),"| G∘F=id:",GF==(X,Y),"| deg F:",max(F[0].degree(),F[1].degree()),"| deg G:",max(G[0].degree(),G[1].degree()))
        print("F1 =",F[0]); print("F2 =",F[1]); print("G1 =",G[0]); print("G2 =",G[1])
        if name=="kwadr":
            print("osadzenia rzeczywiste L:",[str(e(r).n(30)) for e in L.embeddings(RR)])
        else:
            print("osadzenia rzeczywiste L:",len(L.embeddings(RR)))

