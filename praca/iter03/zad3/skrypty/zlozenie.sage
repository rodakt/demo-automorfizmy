# Dokładne F∘G, G∘F w Q(r)[X,Y], 15r^2+38r-1=0. Uruchom z katalogu zad3: sage skrypty/zlozenie.sage
R.<t>=QQ[]; L.<r>=NumberField(15*t^2+38*t-1); print("Q(r)~Q(sqrt94):", L.is_isomorphic(QuadraticField(94)))
S.<X,Y>=L[]
d={}
for l in open('skrypty/FG_r.txt'):
    k,v=l.split(' = ',1); d[k]=S(sage_eval(v.replace('**','^'),locals={'X':X,'Y':Y,'r':r}))
F=[d['F1'],d['F2']]; G=[d['G1'],d['G2']]
print("G∘F=id:", [g(F[0],F[1]) for g in G]==[X,Y])
print("F∘G=id:", [f(G[0],G[1]) for f in F]==[X,Y])
print("deg:", [p.degree() for p in F+G])
print("osadzenia rzeczywiste:", L.real_places())
