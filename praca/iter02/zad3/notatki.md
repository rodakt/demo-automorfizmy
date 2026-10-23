# iter02/zad3 — test sensowności: automorfizmy stopnia 4 nad Q(√94) i nad ciałem kubicznym

## Metoda
Skrypt `skrypty/test_sensownosci.sage` (wyjście: `tmp/test.out`, czas < 1 min) odtwarza DOKŁADNIE układ z
`praca/iter01/zad2/skrypty/k2_szczegoly.sage` (karta (0,0)):
a0(x,y)=(x+s·y, k·y), t(x,y)=(x, y+x²), a1(x,y)=(a x+b y+e, c x+d y+f), a2 = odwrotność (X+S·Y, K·Y),
warunek t∘a1∘t∘a0(p_i) = a2⁻¹(q_i), plus z·k·K·(ad−bc)=1. F = a2∘t∘a1∘t∘a0, G = a0⁻¹∘t⁻¹∘a1⁻¹∘t⁻¹∘a2⁻¹.
Następnie `I.variety(L)` dla L = Q[r]/(15r²+38r−1) (Sage: `is_isomorphic(QuadraticField(94))` → True; disc = 1504 = 16·94)
oraz L = Q[r]/(3r³+39r²+29r+9). Dla każdego punktu budowane są F i G w L[X,Y] i sprawdzane
równości arytmetyką dokładną w L (nie numerycznie).

## Wyniki (OBLICZENIOWE)
- Ideał: wymiar 0, stopień (dim przestrzeni ilorazowej) 5 — zgodnie z iter01.
- Nad Q(√94): 2 punkty (r = s = (−19 ± √94)/15). Dla OBU: F(p_i)=q_i (i=1..5), F∘G=id, G∘F=id, deg F = deg G = 4. Wszystko True.
- Nad ciałem kubicznym: 1 punkt (s = r). F(p_i)=q_i, F∘G=id, G∘F=id, deg F = deg G = 4. Wszystko True.
- Ciało Q(√94) jest rzeczywiste (oba osadzenia rzeczywiste: r ≈ −2.5594 i r ≈ 0.02605); ciało kubiczne ma
  1 osadzenie rzeczywiste. Zatem istnieją (co najmniej 3) automorfizmy wielomianowe R² stopnia 4 o
  współczynnikach rzeczywistych realizujące tę bijekcję.
- Wniosek: kodowanie układu K2 z iteracji 01 jest poprawne w tym sensie, że punkty bazy dają prawdziwe
  automorfizmy realizujące bijekcję; rozwiązania istnieją, tylko nie nad Q. (Nie testuje to kompletności
  kart/cechowania — to zadanie iter02/zad2.)

## Wniosek opcjonalny (nad R) — HIPOTEZA/warunkowe
Nad R najniższy stopień dla tej bijekcji wynosi ≤ 4 (OBLICZENIOWE, powyżej). Jeżeli argument K1 z iter01/zad1
(układ liniowy z wymiernymi współczynnikami, rząd nie zależy od rozszerzenia ciała) oraz redukcja JvdK
(deg ≤ 3 ⇒ K1) z iter02/zad1 są poprawne, to nad R minimalny stopień wynosi dokładnie 4, a dolne
ograniczenie 6 nad Q jest zjawiskiem arytmetycznym (brak punktów wymiernych), nie geometrycznym.
Nie sprawdzone tutaj szczegółowo — etykieta HIPOTEZA.

## Jawne F, G dla pierwszego punktu nad Q(√94), r = (−19+√94)/15 (lub drugi pierwiastek — kolejność z Sage)
punkt: {'s': r, 'k': 454/75*r + 22/75, 'K': -9870*r + 258, 'S': -15*r, 'f': 3910*r - 102, 'e': 5*r - 1, 'd': -5445/4*r + 141/4, 'c': 13875/2*r - 363/2, 'b': -15/8*r + 7/8, 'a': 45/4*r - 5/4, 'z': 25645/23136*r + 98453/34704}
F1 = (8175/61696*r + 17935/61696)*X^4 + (-2775/15424*r + 545/15424)*X^3*Y + (22725/30848*r - 555/30848)*X^2*Y^2 + (-19375/15424*r + 505/15424)*X*Y^3 + (148765/185088*r - 3875/185088)*Y^4 + (-7125/15424*r - 10325/15424)*X^3 + (15975/15424*r + 2855/15424)*X^2*Y + (-15095/15424*r + 585/15424)*X*Y^2 + (-6235/15424*r + 165/15424)*Y^3 + (7485/15424*r + 7701/15424)*X^2 + (11075/7712*r - 2453/7712)*X*Y + (-68825/46272*r + 4207/46272)*Y^2 + (5555/3856*r - 2385/3856)*X + (-2435/3856*r + 209/3856)*Y + (-485/723*r - 428/723)
F2 = (17935/61696*r + 137941/185088)*X^4 + (545/15424*r + 3587/46272)*X^3*Y + (-555/30848*r + 109/30848)*X^2*Y^2 + (505/15424*r - 37/46272)*X*Y^3 + (-3875/185088*r + 101/185088)*Y^4 + (-10325/15424*r - 79895/46272)*X^3 + (2855/15424*r + 24893/46272)*X^2*Y + (585/15424*r + 1427/46272)*X*Y^2 + (165/15424*r + 7/46272)*Y^3 + (-5795/15424*r - 36761/46272)*X^2 + (-525/7712*r - 19127/23136)*X*Y + (-13145/46272*r + 6455/46272)*Y^2 + (2435/3856*r + 3647/3856)*X + (-755/3856*r - 3039/3856)*Y + (295/723*r + 158/241)
G1 = (3875/185088*r + 29753/555264)*X^4 + (-505/15424*r - 3875/46272)*X^3*Y + (555/30848*r + 1515/30848)*X^2*Y^2 + (-545/15424*r - 185/15424)*X*Y^3 + (-17935/61696*r + 545/61696)*Y^4 + (-165/15424*r - 1247/46272)*X^3 + (-585/15424*r - 3019/46272)*X^2*Y + (-2855/15424*r + 1065/15424)*X*Y^2 + (10325/15424*r - 475/15424)*Y^3 + (13145/46272*r + 119267/138816)*X^2 + (525/7712*r - 15137/23136)*X*Y + (5795/15424*r + 2427/15424)*Y^2 + (755/3856*r - 3379/11568)*X + (-2435/3856*r - 7565/11568)*Y + (-295/723*r - 820/2169)
G2 = (-148765/185088*r - 1142239/555264)*X^4 + (19375/15424*r + 148765/46272)*X^3*Y + (-22725/30848*r - 58125/30848)*X^2*Y^2 + (2775/15424*r + 7575/15424)*X*Y^3 + (-8175/61696*r - 2775/61696)*Y^4 + (6235/15424*r + 47881/46272)*X^3 + (15095/15424*r + 116477/46272)*X^2*Y + (-15975/15424*r - 37615/15424)*X*Y^2 + (7125/15424*r + 7725/15424)*Y^3 + (68825/46272*r + 535691/138816)*X^2 + (-11075/7712*r - 91529/23136)*X*Y + (-7485/15424*r - 11261/15424)*Y^2 + (2435/3856*r + 19133/11568)*X + (-5555/3856*r - 49373/11568)*Y + (485/723*r + 2402/2169)

Drugi punkt kwadratowy i punkt kubiczny: pełne napisy w tmp/test.out (odtwarzalne skryptem).

Obserwacja (bez dowodu): dla drugiego punktu kwadratowego F1 jest równe G2 pierwszego z zamianą X↔Y itd. — sugeruje symetrię F ↦ σ∘F⁻¹∘σ, σ=(y,x), między dwoma sprzężonymi rozwiązaniami.
Uzasadnienie symetrii: bijekcja π (A→C, B→D, C→A, D→E, E→B) spełnia σ∘π⁻¹∘σ = π dla σ=(y,x) (sprawdzone ręcznie
na 5 punktach: σ zamienia B↔D, ustala A, C, E). Zatem F ↦ σ∘F⁻¹∘σ przeprowadza rozwiązania w rozwiązania (i zachowuje K2
po sprzężeniu), co tłumaczy parowanie dwóch punktów nad Q(√94).
Czego nie zrobiono: nie zbadano wymiernych punktów innych kart (to iter01/zad2, iter02/zad2).
