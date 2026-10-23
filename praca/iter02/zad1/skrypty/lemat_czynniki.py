# Sprawdzenie Lematów 1-2 (rozkład elementu J stopnia 2) symbolicznie.
import sympy as sp
x,y,X,Y,al,be,ga,c,e,h=sp.symbols('x y X Y alpha beta gamma c e h')
def comp(f,g):  # f∘g
    return tuple(sp.expand(fi.subs({x:X,y:Y},simultaneous=True).subs({X:g[0],Y:g[1]},simultaneous=True)) for fi in f)
f=lambda Y_: c*(Y_+e)**2+h
j=(al*x+f(y), be*y+ga)
d2=(al*x, be*y+ga)
G=(x+f((y-ga)/be), y)
print("Lemat1:", [sp.simplify(a-b) for a,b in zip(comp(G,d2),j)])
s=(x+y**2,y); v=(x/c,y+e); u=(c*x+h, y-e)
print("Lemat2:", [sp.simplify(a-b) for a,b in zip(comp(u,comp(s,v)),(x+f(y),y))])
sig=(y,x); t=(x,y+x**2)
print("sigma t sigma = s:", comp(sig,comp(t,sig))==s)
