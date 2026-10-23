for p in [5,7,11,13,17,19,23,29,31,37,41,43]:
    R.<s>=GF(p)[]
    f=(15*s^2+38*s-1)*(3*s^3+39*s^2+29*s+9)
    print(p, len(f.roots()), f.roots(multiplicities=False), f.degree())
