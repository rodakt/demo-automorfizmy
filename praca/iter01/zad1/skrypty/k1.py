# Rozstrzygniecie klasy K1 = {a o t o b}, t=(x, y+f(x)): uklad L(p_i)=L'(q_i).
import json, sympy as sp
Z=json.load(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'../../../../zadanie.json')))
P=[tuple(sp.Rational(c) for c in p) for p in Z['punkty_p']]
Q=[tuple(sp.Rational(c) for c in q) for q in Z['punkty_q']]
a,b,c,a2,b2,c2=sp.symbols('a b c a2 b2 c2')
eqs=[a*p[0]+b*p[1]+c-(a2*q[0]+b2*q[1]+c2) for p,q in zip(P,Q)]
M=sp.Matrix([[sp.diff(e,v) for v in (a,b,c,a2,b2,c2)] for e in eqs])
print("macierz ukladu:");sp.pprint(M)
print("rzad:",M.rank())
ns=M.nullspace()
print("jadro:",[list(v) for v in ns])
for v in ns:
    if any(v[i]!=0 for i in (0,1)) or any(v[i]!=0 for i in (3,4)):
        print("NIESTALE rozwiazanie:",list(v))
        break
else:
    print("WNIOSEK: tylko rozwiazania z L, L' stalymi -> K1 pusta")
# test parallelogramu (stopien 1)
print("p1+p3=",tuple(P[0][i]+P[2][i] for i in range(2)),"p2+p4=",tuple(P[1][i]+P[3][i] for i in range(2)))
print("q1+q3=",tuple(Q[0][i]+Q[2][i] for i in range(2)),"q2+q4=",tuple(Q[1][i]+Q[3][i] for i in range(2)))
