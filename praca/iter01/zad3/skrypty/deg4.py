# Rodzina: L(q)=M q+s, M=[[a,b],[3,-1]], s=(e,h); warunki zgodności f (liniowe) i g (D,E: a+3b=-3).
# Pytanie: czy można wymusić deg g <= 2 (zerowa 3. różnica dzielona -- liniowa w a,b,e)?
import sympy as sp
a,b,e,h=sp.symbols('a b e h')
P=[(-1,-1),(1,-1),(1,1),(-1,1),(2,2)]; Q=[(1,1),(-1,1),(-1,-1),(2,2),(1,-1)]
V=[(a*qx+b*qy+e, 3*qx-qy+h) for qx,qy in Q]
ys=[V[i][1] for i in range(4)]; gs=[V[i][0]-P[i][0] for i in range(4)]
dd=sum(gs[i]/sp.prod([ys[i]-ys[j] for j in range(4) if j!=i]) for i in range(4))
print('3. roznica dzielona:',sp.simplify(dd))
print(sp.solve([sp.simplify(dd), a+3*b+3],[a,b],dict=True))
