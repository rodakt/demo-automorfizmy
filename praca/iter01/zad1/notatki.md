# iter01/zad1 — dolne ograniczenia: stopień 1 i klasa K1

Dane: p = A(-1,-1), B(1,-1), C(1,1), D(-1,1), E(2,2) ↦ q = C, D, A, E, B,
tj. q = (1,1), (-1,1), (-1,-1), (2,2), (1,-1).

## (a) Brak automorfizmu stopnia 1 — UDOWODNIONE
Odwzorowanie afiniczne F(v) = Av + t spełnia F(u)+F(w) = A(u+w) + 2t, więc zachowuje
relację u+w = u'+w' (dowolne dwie pary o równych sumach przechodzą w pary o równych sumach).
Mamy p1+p3 = (0,0) = p2+p4, a q1+q3 = (0,0) ≠ (1,3) = q2+q4. Zatem żadne odwzorowanie
afiniczne (nawet nieodwracalne, nawet nad R) nie spełnia F(p_i)=q_i dla i=1..4.
(Wynika to też z (b), bo afiniczne ⊂ K1.)

## (b) Klasa K1 = {a∘t∘b} jest pusta — UDOWODNIONE + OBLICZENIOWE
K1 = {a∘t∘b : a, b afiniczne odwracalne nad Q, t(x,y) = (x, y+f(x)), f ∈ Q[x] dowolne}.
(Obejmuje też a∘(x+g(y), y)∘b, bo to sprzężenie przez zamianę współrzędnych, która jest afiniczna.)

Lemat (UDOWODNIONE). Niech ℓ(x,y)=x. Wtedy ℓ∘t = ℓ. Jeśli F = a∘t∘b, to
ℓ∘a⁻¹∘F = ℓ∘t∘b = ℓ∘b. Kładąc L = ℓ∘b, L' = ℓ∘a⁻¹ (niestałe funkcjonały afiniczne, bo a, b
odwracalne) dostajemy L'(q_i) = L(p_i) dla wszystkich i.

Rachunek (OBLICZENIOWE, `skrypty/k1.py`, wynik w tmp/k1.out). L = a x + b y + c,
L' = a' x + b' y + c'; 5 równań liniowych jednorodnych w 6 niewiadomych. Macierz ma rząd 5,
jądro rozpięte przez (a,b,c,a',b',c') = (0,0,1,0,0,1), czyli tylko L = L' = stała.
Rachunek jest też łatwy ręcznie (dokładne liczby wymierne, sympy `nullspace`).
Wniosek: nie ma niestałych L, L' ⇒ K1 nie zawiera żadnego rozwiązania, niezależnie od deg f.
Nie zapisano więc rozwiazanie_K1.json.

## (c) Wniosek przez twierdzenie Junga–van der Kulka
Twierdzenie (cytowane, nie dowodzone tu; van den Essen, *Polynomial Automorphisms and the
Jacobian Conjecture*, 2000, rozdz. 5; Friedland–Milnor 1989): każdy automorfizm Q² niebędący
afinicznym jest zredukowanym słowem a₀∘t₁∘a₁∘…∘t_k∘a_k (t_j trójkątne stopnia d_j ≥ 2,
a_j afiniczne nie-trójkątne dla 0<j<k), i deg F = d₁·…·d_k.

Jeśli deg F = p jest liczbą pierwszą, to k = 1 i F ∈ K1. Afiniczne też ∈ K1.
**Twierdzenie (UDOWODNIONE przy założeniu JvdK + OBLICZENIOWE część liniowa):** żaden
automorfizm stopnia 1 ani stopnia pierwszego (2, 3, 5, 7, 11, …) nie realizuje danej bijekcji.
W szczególności każdy realizujący automorfizm ma stopień ≥ 4, a dopuszczalne stopnie to
tylko liczby złożone: 4, 6, 8, 9, 10, …

Uwaga: K1 NIE zawiera złożeń dwóch (i więcej) trójkątnych — nic tu nie wykluczono dla
stopni 4, 6, 8, 9, …; stopień 4 = 2·2 pozostaje otwarty (konstrukcja bazowa daje 16).
Ogólniej wiadomo: wykluczone są wszystkie F z dokładnie jednym nieafinicznym czynnikiem.

## Czego nie zrobiono / sugestie
- Klasa a∘t₁∘a₁∘t₂∘a₂ z deg t₁ = deg t₂ = 2 (stopień 4) — następny krok. Ten sam trik:
  ℓ zachowywane przez t₁ daje warunek: istnieje L z L(p_i)=x-owa współrzędna pośrednich punktów.
