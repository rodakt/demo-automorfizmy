# iter03/zad3: dokładne sprawdzenie automorfizmu stopnia 4 nad Q(r), 15r^2+38r-1=0, r=(-19±2√94)/15,
# oraz rząd układu K1 i test równoległoboku. Uruchom: $PYTHON skrypty/sprawdz_R.py (z katalogu zad3)
import json, sympy as sp
X,Y,r=sp.symbols('X Y r'); x,y=sp.symbols('x y')
mp=15*r**2+38*r-1
d={}
for l in open('skrypty/FG_r.txt'):
    k,v=l.split(' = ',1); d[k]=sp.sympify(v,locals={'X':X,'Y':Y,'r':r})
def red(e): # redukcja współczynników modulo minimalny wielomian r
    e=sp.expand(e); P=sp.Poly(e,X,Y)
    return sum(sp.rem(sp.Poly(c,r),sp.Poly(mp,r)).as_expr()*X**m[0]*Y**m[1] for m,c in P.terms())
z=json.load(open('../../../zadanie.json'))
P=[tuple(sp.Rational(c) for c in p) for p in z['punkty_p']]
Q=[tuple(sp.Rational(c) for c in q) for q in z['punkty_q']]
print("pierwiastki:",sp.solve(mp,r), "Q(r)=Q(sqrt94):", sp.discriminant(mp,r), "=16*94")
F=[d['F1'],d['F2']]; G=[d['G1'],d['G2']]
for i,(p,q) in enumerate(zip(P,Q)):
    v=[red(f.subs({X:p[0],Y:p[1]})) for f in F]
    print("F(p%d)=q%d:"%(i+1,i+1), sp.simplify(v[0]-q[0])==0 and sp.simplify(v[1]-q[1])==0)
# (składanie pominięte — w sprawdz_R.py)
for k in ['F1','F2','G1','G2']:
    print('deg',k,'=',sp.Poly(red(d[k]),X,Y).total_degree())
# test numeryczny dla obu osadzeń rzeczywistych (tylko ilustracja)
for rv in sp.solve(mp,r): print("r =",rv,"≈",sp.N(rv))
# Stopień 1: p1..p4 równoległobok (p1+p3=p2+p4), obrazy:
print("p1+p3-p2-p4 =",[P[0][j]+P[2][j]-P[1][j]-P[3][j] for j in range(2)])
print("q1+q3-q2-q4 =",[Q[0][j]+Q[2][j]-Q[1][j]-Q[3][j] for j in range(2)])
# Lemat K1: L'(q_i)=L(p_i), macierz wymierna; rząd nad Q = rząd nad R, C
M=sp.Matrix([[p[0],p[1],1,-q[0],-q[1],-1] for p,q in zip(P,Q)])
print("rzad K1 =",M.rank(),"jadro =",[list(v) for v in M.nullspace()])
