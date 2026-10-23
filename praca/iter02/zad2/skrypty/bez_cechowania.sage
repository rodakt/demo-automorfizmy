# Uklad bez cechowania: a0, b=a2^{-1}, a1 pelne afiniczne + z*det=1. Oczekiwany wymiar 8
# (= wymiar grupy symetrii B x B dzialajacej wolno na zbiorze rozwiazan).
R=PolynomialRing(QQ,['a%d'%i for i in range(6)]+['b%d'%i for i in range(6)]+['c%d'%i for i in range(6)]+['z0','z1','z2'],order='degrevlex')
g=R.gens(); A=g[0:6]; B=g[6:12]; C=g[12:18]; z0,z1,z2=g[18:21]
P=[(-1,-1),(1,-1),(1,1),(-1,1),(2,2)]; Q=[(1,1),(-1,1),(-1,-1),(2,2),(1,-1)]
af=lambda M,v:(M[0]*v[0]+M[1]*v[1]+M[2],M[3]*v[0]+M[4]*v[1]+M[5])
eqs=[]
for p,q in zip(P,Q):
    a=af(A,p); u=(a[0],a[1]+a[0]^2)
    b=af(B,q); w=(b[0],b[1]-b[0]^2)
    v=af(C,u); eqs+= [v[0]-w[0],v[1]-w[1]]
dets=[z0*(A[0]*A[4]-A[1]*A[3])-1, z1*(B[0]*B[4]-B[1]*B[3])-1, z2*(C[0]*C[4]-C[1]*C[3])-1]
I=R.ideal(eqs+dets)
print("dim nad Q:",I.dimension(),flush=True)
Ip=I.change_ring(R.change_ring(GF(32003)))
print("dim mod 32003:",Ip.dimension(),flush=True)
