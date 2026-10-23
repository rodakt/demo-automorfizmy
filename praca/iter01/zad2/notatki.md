# iter01/zad2 — klasa K2 (złożenia dwóch trójkątnych stopnia 2)

## Klasa
K2 = { a2∘t∘a1∘t∘a0 : a0,a1,a2 afiniczne nad Q }, t(x,y) = (x, y+x²).
Wynik: **brak elementów K2 przeprowadzających p_i → q_i** (OBLICZENIOWE). Nad Q̄ jest dokładnie 5 rozwiązań
(po cechowaniu), żadne wymierne: współrzędna s spełnia (15s²+38s−1)(3s³+39s²+29s+9)=0 — oba czynniki
nierozkładalne nad Q. Dwa rozwiązania nad Q(√94) (rzeczywiste), trzy nad ciałem stopnia 3 (jedno rzeczywiste,
dwa zespolone sprzężone). Zatem nad R istnieją 3 takie automorfizmy (stopnia ≤4), nad Q — żaden.

## Redukcje (UDOWODNIONE, elementarne)
1. Dowolne trójkątne stopnia 2: (x, y+αx²+βx+γ), α≠0, równa się diag(1,α)∘t∘diag(1,1/α) złożone z afinicznym
   (x,y)↦(x,y+βx+γ); te czynniki afiniczne wchłaniają sąsiednie a_i. Trójkątne „zmienia x” stopnia 2 to
   σ∘(trójkątne zmienia y)∘σ, σ=(y,x) — też wchłaniane. Więc K2 obejmuje wszystkie złożenia
   afin∘trójk2∘afin∘trójk2∘afin.
2. Grupa B = {(cx+e, c²y+lx+f): c≠0} spełnia t∘b = b'∘t z b'=(cx+e, c²y+(l+2ce)x+f+e²) ∈ B, czyli tBt⁻¹=B.
   Stąd a0 można zastąpić reprezentantem warstwy B\Aff, a a2⁻¹ też (b∘t∘a1 = t∘(b''∘a1)).
3. Reprezentanci B\Aff: g=(α(x,y), β(x,y)) z α,β formami afinicznymi. Jeśli współczynnik α przy x ≠0:
   g=(x+s·y, k·y), k≠0 (karta 0). W przeciwnym razie g=(y, k·x) (karta 1). (c ustalone przez normalizację α,
   więc skala k przy β zostaje jako parametr.)
4. Niewiadome: s,k (dla a0), S,K (dla a2⁻¹), a,b,c,d,e,f (a1 pełne), z: z·k·K·det(a1)=1.
   Równania: a2⁻¹(q_i) = t(a1(t(a0(p_i)))), 10 równań, 10 niewiadomych + z.

## Obliczenia (skrypty/k2.sage, wynik tmp/k2.out; skrypty/k2_szczegoly.sage)
Sage/Singular, Gröbner nad Q, dokładnie.
- karta (0,0): ideał zerowymiarowy, vdim=5 (= liczba punktów, ideał radykalny), punkty QQ: brak.
- karty (0,1),(1,0),(1,1): ideał = (1), brak rozwiązań nawet nad C.
Baza leksykograficzna (k2_szczegoly): wszystkie zmienne są wielomianami od s, eliminant jak wyżej.

## Interpretacja (uwaga na zakres)
- Z tw. Junga–van der Kulka (nad dowolnym ciałem) automorfizm stopnia ≤4 jest afiniczny, jednym trójkątnym
  (stopnia ≤4) między afinicznymi, albo leży w K2 (słowo długości 2 ze stopniami 2·2). Niniejszy wynik
  wyklucza K2. Po dołączeniu wyniku zadania o klasie „jedno trójkątne między afinicznymi” (stopnie 2,3,4)
  dawałoby to ograniczenie dolne deg ≥5 — ale to wymaga tamtego wyniku i starannego zapisu argumentu JvdK
  (to HIPOTEZA do domknięcia, nie twierdzenie tego zadania).
- Nie sprawdzono niezależnie (np. drugim systemem) — rekomendacja: powtórzyć w Singular/msolve lub mod p.

## Test kontrolny (skrypty/k2_test_kontrolny.sage, tmp/test.out)
Te same równania i cechowanie dla q_i = F(p_i), F = A2∘t∘A1∘t∘A0 z losowymi wymiernymi A_i:
karta (0,0) daje dokładnie 1 punkt wymierny, pozostałe ideał (1). Kodowanie układu i cechowanie zachowują
więc znane rozwiązania (sprawdzenie zdrowego rozsądku, nie dowód poprawności).

## Czego nie zrobiono
- Brak pliku rozwiazanie_*.json (w K2 nie ma rozwiązania wymiernego).
- Nie powtórzono rachunku innym systemem (msolve/M2 niedostępne; Singular to ten sam silnik co Sage).
