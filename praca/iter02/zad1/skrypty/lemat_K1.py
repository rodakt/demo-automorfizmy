# Niezależne sprawdzenie lematu K1: czy istnieją afiniczne L(x,y)=l1 x+l2 y+l3,
# L'(x,y)=m1 x+m2 y+m3, nie obie stałe, z L'(q_i)=L(p_i) dla i=1..5.
import json, sympy as sp
z=json.load(open('../../../zadanie.json'))
P=[tuple(sp.Rational(c) for c in p) for p in z['punkty_p']]
Q=[tuple(sp.Rational(c) for c in q) for q in z['punkty_q']]
l1,l2,l3,m1,m2,m3=sp.symbols('l1 l2 l3 m1 m2 m3')
M=sp.Matrix([[p[0],p[1],1,-q[0],-q[1],-1] for p,q in zip(P,Q)])
print("macierz:",M.tolist())
print("rzad =",M.rank())
print("jadro =",[list(v) for v in M.nullspace()])
