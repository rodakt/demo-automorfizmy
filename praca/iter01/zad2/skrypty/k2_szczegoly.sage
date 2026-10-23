# Szczegóły karty (0,0): wielomian eliminacyjny i rozwiązania zespolone
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
I=R.ideal(eqs); G=I.groebner_basis()
for g in G: print(g.factor() if g.variables()==(s,) else g)
el=[g for g in G if g.variables()==(s,)][0]
print("eliminant s:",el.factor())
print("pierwiastki rzeczywiste:",el.univariate_polynomial().real_roots() if hasattr(el.univariate_polynomial(),'real_roots') else None)
print("galois/nierozkładalność:",[ (fa.degree(), fa.is_irreducible()) for fa,_ in el.univariate_polynomial().factor()])
for pt in I.variety(CC): print({str(kk):vv for kk,vv in pt.items() if str(kk) in 'skSKab'})
