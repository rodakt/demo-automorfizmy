# Certyfikaty lift dla kart K2 (układ przepisany z iter01/zad2/skrypty/k2.sage)
import itertools, sys
P=[(-1,-1),(1,-1),(1,1),(-1,1),(2,2)]
Q=[(1,1),(-1,1),(-1,-1),(2,2),(1,-1)]
R=PolynomialRing(QQ,'s,k,S,K,a,b,c,d,e,f,z',order='degrevlex')
s,k,S,K,a,b,c,d,e,f,z=R.gens()
def norm(pt,ch,s,k):
    X,Y=pt
    return (X+s*Y, k*Y) if ch==0 else (Y, k*X)
def uklad(ch0,ch2):
    eqs=[]
    for p,q in zip(P,Q):
        u=norm(p,ch0,s,k); w=(u[0],u[1]+u[0]^2)
        v=(a*w[0]+b*w[1]+e, c*w[0]+d*w[1]+f); r=(v[0],v[1]+v[0]^2)
        qq=norm(q,ch2,S,K)
        eqs+= [r[0]-qq[0], r[1]-qq[1]]
    eqs.append(z*k*K*(a*d-b*c)-1)
    if ch0==1: eqs.append(s)
    if ch2==1: eqs.append(S)
    return eqs
karty=[(0,1),(1,0),(1,1),(0,0)] if len(sys.argv)<2 else [tuple(map(int,sys.argv[1].split(',')))]
for ch0,ch2 in karty:
    g=uklad(ch0,ch2); I=R.ideal(g)
    if ch0==0 and ch2==0:
        J=R.ideal(g).change_ring(R.change_ring(order='lex'))
        GL=J.groebner_basis()
        E=[h for h in GL if h.variables()==(J.ring().gens()[0],)]
        print("lex GB:",list(GL)); sys.stdout.flush()
        targets=[R(h) for h in GL]
    else:
        targets=[R(1)]
    out=open('tmp/cert_%d%d.txt'%(ch0,ch2),'w')
    out.write(repr([str(x) for x in g])+'\n')
    for T in targets:
        H=T.lift(I)
        assert sum(hh*gg for hh,gg in zip(H,g))==T
        out.write(repr([str(T),[str(hh) for hh in H]])+'\n'); out.flush()
        print("karta",ch0,ch2,"cel",T if T==1 else T.lm(),"OK"); sys.stdout.flush()
    out.close()
