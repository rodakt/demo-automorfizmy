# Niezależne sprawdzenie certyfikatów w sympy: T == sum h_j g_j (dokładnie nad Q)
import sys, ast, sympy as sp
V=sp.symbols('s k S K a b c d e f z')
loc={str(v):v for v in V}
for fn in sys.argv[1:]:
    L=open(fn).read().splitlines()
    g=[sp.Poly(sp.sympify(x,locals=loc),*V,domain='QQ') for x in ast.literal_eval(L[0])]
    for line in L[1:]:
        T,H=ast.literal_eval(line)
        T=sp.Poly(sp.sympify(T,locals=loc),*V,domain='QQ')
        S=sp.Poly(0,*V,domain='QQ')
        for h,gg in zip(H,g): S+=sp.Poly(sp.sympify(h,locals=loc),*V,domain='QQ')*gg
        print(fn, 'OK' if S==T else 'BLAD', T.as_expr() if T.is_ground else T.LM()); sys.stdout.flush()
