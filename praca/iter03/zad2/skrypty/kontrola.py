# Kontrola Tw. B: losowe słowa zredukowane nad Q, deg F == iloczyn deg j_i.
import random
from sympy import symbols, Rational, expand, Poly
x, y = symbols('x y'); random.seed(2026)
R = lambda: Rational(random.randint(-9, 9), random.randint(1, 5))
def nz():
    while True:
        r = R()
        if r != 0: return r
def comp(f, g):  # (f∘g)(v) = f(g(v))
    return tuple(expand(c.subs({x: g[0], y: g[1]}, simultaneous=True)) for c in f)
def deg(F): return max(Poly(c, x, y).total_degree() for c in F)
def afin(wJ=None):
    while True:
        a, b, c, d = R(), R(), R(), R()
        if wJ is True: c = 0
        if wJ is False and c == 0: continue
        if a*d - b*c != 0: return (a*x + b*y + R(), c*x + d*y + R())
def jon(e):
    f = sum(R()*y**i for i in range(e)) + nz()*y**e
    return (nz()*x + f, nz()*y + R())
wyn = []
for stopnie in [(2, 2), (2, 3), (3, 2), (2, 2, 2)]:
    ok = 0; N = 15 if len(stopnie) < 3 else 8
    for _ in range(N):
        F = afin()                      # a_k (dowolne)
        for i, e in enumerate(reversed(stopnie)):
            F = comp(jon(e), F)
            if i < len(stopnie) - 1: F = comp(afin(wJ=False), F)  # a_i ∉ J
        F = comp(afin(), F)             # a_0 (dowolne)
        p = 1
        for e in stopnie: p *= e
        ok += (deg(F) == p)
    wyn.append((stopnie, ok, N)); print(stopnie, f"{ok}/{N} zgodnych")
# Przykład niezredukowany: a1 = id ∈ J  =>  j1∘j2 ∈ J, stopień nie mnoży się
j1 = (x + y**2, y); j2 = (x - y**2, y)
print("j1∘id∘j2 =", comp(j1, j2), "stopień", deg(comp(j1, j2)), "(iloczyn byłby 4)")
j3 = (x + y**2 + y**3, y)
print("j3∘id∘j1: stopień", deg(comp(j3, j1)), "(iloczyn byłby 6)")
# Kontrast: a1 = σ ∉ J
s = (y, x)
print("j1∘σ∘j1: stopień", deg(comp(j1, comp(s, j1))), "(iloczyn 4)")
