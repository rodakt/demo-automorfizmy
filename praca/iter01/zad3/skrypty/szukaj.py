# F = Ainv^{-1} o T2 o T1, T1=(x,y+f(x)), T2=(x+g(y),y); v_i = Ainv(q_i) = M q_i + s
import sympy as sp, itertools, random, json
from fractions import Fraction
P=[(-1,-1),(1,-1),(1,1),(-1,1),(2,2)]; Q=[(1,1),(-1,1),(-1,-1),(2,2),(1,-1)]
a,b,c,d,e,h=sp.symbols('a b c d e h')
V=[(a*qx+b*qy+e, c*qx+d*qy+h) for qx,qy in Q]
# f consistency: v_y - p_y equal for A,D (x=-1) and B,C (x=1)
eqs=[sp.Eq(V[0][1]-P[0][1], V[3][1]-P[3][1]), sp.Eq(V[1][1]-P[1][1], V[2][1]-P[2][1])]
sol=sp.solve(eqs,[c,d],dict=True)[0]; print(sol)
V=[(vx,vy.subs(sol)) for vx,vy in V]
X=sp.Symbol('X')
def ddiff(xs,ys):
    # leading coefficient of interpolant of degree n-1
    return sum(ys[i]/sp.prod([xs[i]-xs[j] for j in range(len(xs)) if j!=i]) for i in range(len(xs)))
ys=[V[i][1] for i in range(5)]; gs=[V[i][0]-P[i][0] for i in range(5)]
cond4=sp.together(ddiff(ys,gs)); num4=sp.numer(cond4)
print('free', num4.free_symbols)
res=[]
for trial in range(4000):
    vals={s:sp.Rational(random.randint(-3,3),random.randint(1,2)) for s in [b,e,h,a]}
    keys=list(vals); k=random.choice(keys); del vals[k]
    pe=sp.expand(num4.subs(vals))
    for r in sp.roots(sp.Poly(pe,k),filter='Q') if pe.free_symbols else []:
        vv=dict(vals); vv[k]=r; vv.update({c:sol[c].subs(vv), d:sol[d].subs(vv)})
        M=sp.Matrix([[vv[a],vv[b]],[vv[c],vv[d]]])
        if M.det()==0: continue
        Y=[y.subs(vv) for y in ys]
        if len(set(Y))<5: continue
        G=[g.subs(vv) for g in gs]
        # also check 3rd diff (deg g<=2)
        c3=ddiff(Y[:4],G[:4])
        print('FOUND',vv,'deg2?',c3==0); res.append(vv)
        json.dump([{str(k):str(v) for k,v in r_.items()} for r_ in res],open('tmp/res.json','w'))
    if len(res)>=3: break
