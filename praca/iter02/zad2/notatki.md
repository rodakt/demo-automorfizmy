# iter02/zad2 — niezależne potwierdzenie braku wymiernych F ∈ K2

K2 = {a2∘t∘a1∘t∘a0}, t=(x, y+x²), a_i afiniczne odwracalne (redukcja dowolnych dwóch trójkątnych
stopnia 2 do t — jak w iter01/zad2, nie powtarzano). Warunek pośredni: u_i = t(a0 p_i),
w_i = t⁻¹(b q_i), b = a2⁻¹, a1(u_i) = w_i.

## Metoda (inna niż w iter01: bez baz Gröbnera, czysta enumeracja nad F_p + algebra liniowa)
`skrypty/modp_enum.py`: dla danego p przegląda WSZYSTKIE reprezentanty warstw B\Aff(F_p) dla a0 i b
(B = {(cx+e, c²y+lx+f)} normalizuje t: t∘β = β'∘t, więc a0 ↦ β∘a0, b ↦ β∘b nie zmienia
istnienia rozwiązania). Reprezentanty: translacja 0, część liniowa [[1,s],[0,e]] (e≠0) lub
[[0,1],[d,0]] (d≠0) — pokrywają B_lin\GL2 nad dowolnym ciałem. Dla każdej pary a1 wyznacza się
eliminacją Gaussa mod p (gdy rząd < 3 — pełne przeszukanie warstwy rozwiązań), z warunkiem det a1 ≠ 0.
Wynik: liczba rozwiązań N_p (modulo cechowanie).

## Wyniki (tmp/modp.txt, tmp/elim_modp.txt)
p:   5  7 11 13 17 19 23 29 31 37 41 43
N_p: 3  0  1  4  2  1  3  3  4  1  0  1
Liczba pierwiastków eliminantu iter01 f=(15s²+38s−1)(3s³+39s²+29s+9) w F_p
(`skrypty/eliminant_modp.sage`): 2 0 1 4 2 1 3 3 4 1 0 1.
**Pełna zgodność dla wszystkich p = 7…43** (p=5: zła redukcja, współczynnik 15 ≡ 0, deg f spada).
To niezależnie potwierdza, że zbiór rozwiązań nad Q̄ (modulo cechowanie) to 5 punktów nad ciałami
Q(√94) i ciałem kubicznym — dokładnie jak w iter01.
N_7 = N_41 = 0: brak rozwiązań nawet nad F_7 i F_41.

Ostrożnie: brak rozwiązań mod p NIE jest sam w sobie dowodem braku rozwiązań wymiernych
(rozwiązanie wymierne mogłoby mieć mianowniki podzielne przez 7 lub det ≡ 0 mod 7 — wtedy nie
redukuje się do rozwiązania nad F_7). Ale rozwiązanie wymierne redukuje się dobrze dla prawie
wszystkich p, więc dawałoby N_p ≥ 1 dla prawie wszystkich p; tymczasem (Czebotariew) f bez
pierwiastków mod p zdarza się dla dodatniej gęstości p — tu dla 7 i 41. Silny argument heurystyczny,
zgodny z rozstrzygnięciem Gröbnerem w iter01.

## Test kontrolny (`skrypty/kontrola.py`, tmp/kontrola.txt)
q_i := G(p_i), G = a2∘t∘a1∘t∘a0 z całkowitymi a_i (det = ±1). N_p ≥ 1 dla p = 7,11,13,17,19,23
(wartości 2,2,1,2,2,1) — metoda wykrywa istniejące rozwiązania.

## Układ bez cechowania (`skrypty/bez_cechowania.sage`, tmp/bez_cech.txt)
18 współczynników + 3 zmienne z·det=1, 10 równań. Oczekiwany wymiar 8 = dim(B×B) (działanie
grupy na zbiorze rozwiązań; bez cechowania punkty wymierne nie dają się rozstrzygnąć wprost —
stąd cechowanie). Wynik: patrz niżej.
Obliczenie wymiaru (Singular przez Sage, timeout 240 s) **nie zakończyło się** — brak wyniku.
Nie zdążono. Dla następnego agenta: liczyć mod 32003 albo z częściowym cechowaniem (np. tylko
translacje a0, b = 0), co redukuje 4 zmienne.

## Podsumowanie i zgodność z iter01
Zgodność pełna: N_p = #{pierwiastki f w F_p} dla p = 7…43, co potwierdza (inną metodą) 5 punktów
nad Q̄ i strukturę eliminantu. Rozstrzygnięcie „brak punktów wymiernych” opiera się formalnie na
Gröbnerze z iter01; tutaj — mocne niezależne potwierdzenie (OBLICZENIOWE dla liczb N_p,
HIPOTEZA/heurystyka dla wniosku o Q z samych danych mod p). Zakres: tylko klasa K2, nie wszystkie
automorfizmy stopnia 4.
