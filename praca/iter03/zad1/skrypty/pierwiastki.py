# Twierdzenie o pierwiastkach wymiernych: jawne sprawdzenie obu czynników eliminanta w z
import sympy as sp
from fractions import Fraction as Fr
z=sp.symbols('z')
q2=535274496*z**2-1533993920*z+1
c3=150994944*z**3-143066112*z**2-4457408*z-59049
D=1533993920**2-4*535274496
print('wyroznik q2 =',D,' kwadrat?',sp.sqrt(D).is_integer)
A=[150994944,-143066112,-4457408,-59049]
kand=[Fr(sg*p,q) for p in sp.divisors(59049) for q in sp.divisors(150994944) for sg in (1,-1)]
zera=[r for r in set(kand) if sum(Fr(a)*r**(3-i) for i,a in enumerate(A))==0]
print('kandydatow',len(set(kand)),'pierwiastki wymierne c3:',zera)
