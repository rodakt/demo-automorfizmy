# Test kontrolny: q_i = G(p_i), G = a2 o t o a1 o t o a0 z wymiernymi (calkowitymi) wspolczynnikami.
# Enumeracja mod p musi dac >=1 rozwiazanie dla p, gdzie det a_i != 0 mod p i punkty pozostaja rozne.
import sys; sys.path.insert(0,'skrypty')
from modp_enum import count, P
from fractions import Fraction as Fr
def aff(A,t): return lambda v:(A[0][0]*v[0]+A[0][1]*v[1]+t[0],A[1][0]*v[0]+A[1][1]*v[1]+t[1])
T=lambda v:(v[0],v[1]+v[0]**2)
a0=aff([[2,1],[1,1]],[1,0]); a1=aff([[1,3],[-1,-2]],[0,2]); a2=aff([[3,1],[1,0]],[-1,1])
G=lambda v:a2(T(a1(T(a0(v)))))
Qc=[G(v) for v in P]; print("Q kontrolne:",Qc)
for p in [7,11,13,17,19,23]:
    Qm=[(x%p,y%p) for x,y in Qc]
    print(p,"rozne mod p:",len(set(Qm))==5,"liczba rozw.:",count(p,P,Qm),flush=True)
