# Konstrukcja stopnia 6: F = L^{-1} o T2 o T1, L(q) = M q + s, M=[[-3,0],[3,-1]], s=0
import sympy as sp, json
x,y=sp.symbols('x y')
P=[(-1,-1),(1,-1),(1,1),(-1,1),(2,2)]; Q=[(1,1),(-1,1),(-1,-1),(2,2),(1,-1)]
M=sp.Matrix([[-3,0],[3,-1]]); s=sp.Matrix([0,0])
V=[tuple(M*sp.Matrix(q)+s) for q in Q]
fpts={}; 
for p,v in zip(P,V): fpts.setdefault(p[0],set()).add(v[1]-p[1])
assert all(len(t)==1 for t in fpts.values())
f=sp.expand(sp.interpolate([(k,list(t)[0]) for k,t in fpts.items()],x))
gpts={}
for p,v in zip(P,V): gpts.setdefault(v[1],set()).add(v[0]-p[0])
assert all(len(t)==1 for t in gpts.values())
g=sp.expand(sp.interpolate([(k,list(t)[0]) for k,t in gpts.items()],y))
print('f=',f,'g=',g)
Mi=M.inv(); t=-Mi*s
sol={"autor":"iter01/zad3","opis":"T1=(x,y+f(x)) z f st. 2 (punkty kwadratu parami o wspólnym x), T2=(x+g(y),y) z g st. 3 (D,E mają wspólne y po zmianie afinicznej), następnie afiniczne; stopień 2*3=6",
 "postac":"slowo","czynniki":[
 {"typ":"trojkatne","zmienia":"y","f":str(f)},
 {"typ":"trojkatne","zmienia":"x","f":str(g)},
 {"typ":"afiniczne","A":[[str(Mi[i,j]) for j in range(2)] for i in range(2)],"t":[str(t[0]),str(t[1])]}]}
json.dump(sol,open('rozwiazanie_6.json','w'),indent=1,ensure_ascii=False)
