# iter03/zad2 — dowód Tw. B: stopień słowa zredukowanego = iloczyn stopni

## 0. Konwencje
k — dowolne ciało (charakterystyka dowolna; nad Q w szczególności). Złożenie jak funkcje:
(f∘g)(v) = f(g(v)); dla G = (G1, G2) i a = (a1(X,Y), a2(X,Y)) mamy a∘G = (a1(G1,G2), a2(G1,G2)).
deg G = max(deg G1, deg G2) (stopień całkowity). ⁺P — forma wiodąca (składnik najwyższego
stopnia) wielomianu P ≠ 0.
A — automorfizmy afiniczne, J = {(αx + f(y), βy + γ): α, β ∈ k*, γ ∈ k, f ∈ k[y]},
B = A ∩ J = {(αx + μy + ν, βy + γ)}.
Dla j = (αx + f(y), βy+γ) ∈ J∖A mamy e := deg f ≥ 2 i deg j = e.

**Charakteryzacja A∖J.** a = (a1, a2) ∈ A, a2 = λX + μY + ν. Wówczas a ∈ J ⇔ λ = 0
(bo element J ma drugą współrzędną βy+γ, a pierwsza współrzędna afinicznego a jest zawsze
postaci αx + (afiniczna w y) z α ≠ 0, gdy λ = 0 — z det ≠ 0). Zatem
**a ∈ A∖J ⇔ druga współrzędna a zależy od x (λ ≠ 0)**, tj. macierz części liniowej nie jest
górnotrójkątna (element (2,1) ≠ 0). Sprawdzone: jeśli λ = 0, to det = a_{11}·μ ≠ 0, więc
współczynnik a_{11} przy x w a1 jest ≠ 0 i a = (a_{11}x + (a_{12}y + c), μy + ν) ∈ J.

## 1. Twierdzenie B i dowód (UDOWODNIONE)

**Tw. B.** Niech F = a0∘j1∘a1∘j2∘…∘a_{k−1}∘jk∘ak, k ≥ 1, j_i ∈ J∖A, a_i ∈ A∖J dla
0 < i < k, a0, ak ∈ A dowolne. Wtedy deg F = ∏ deg j_i.

**Lemat (mocniejsza teza).** Dla m = k, k−1, …, 1 niech G^{(m)} = j_m∘a_m∘j_{m+1}∘…∘jk∘ak
oraz d_m = ∏_{i ≥ m} deg j_i. Wtedy
  (i) deg G^{(m)}_1 = d_m,  (ii) deg G^{(m)}_2 < d_m.
(Faktycznie ⁺G^{(m)}_1 = c·ℓ^{d_m} dla formy liniowej ℓ i c ≠ 0 — patrz Uwaga 2; do dowodu
stopnia wystarcza (i)–(ii).)

Dowód (indukcja malejąca po m).
*Baza m = k.* jk = (αX + f(Y), βY + γ), e = deg f ≥ 2. ak = (u, v), gdzie u, v — wielomiany
afiniczne; v jest niestały (gdyby v stały, obraz ak leżałby na prostej, a ak jest
bijekcją). G^{(k)} = (α·u + f(v), β·v + γ). Forma wiodąca f(v): jeśli f = c_e Y^e + …,
to f(v) = c_e v^e + (stopnie ≤ e−1), a ⁺(v^e) = (⁺v)^e ≠ 0, bo k[x,y] jest dziedziną
(⁺v ≠ 0 forma liniowa). Więc deg f(v) = e, a α·u ma stopień ≤ 1 < 2 ≤ e, zatem
deg G^{(k)}_1 = e = d_k. Druga współrzędna: stopień 1 < e. ✓

*Krok m+1 → m* (m < k, więc a_m ∈ A∖J). Niech G = G^{(m+1)}, d = d_{m+1};
z założenia deg G1 = d, deg G2 < d (d ≥ 2). a_m = (λ'X + μ'Y + ν', λX + μY + ν), λ ≠ 0.
Niech H = a_m∘G = (λ'G1 + μ'G2 + ν', λG1 + μG2 + ν).
 - H2 = λG1 + μG2 + ν: składnik λG1 ma stopień d i jego forma wiodąca λ·⁺G1 ≠ 0;
   μG2 + ν ma stopień < d (bo deg G2 < d, d ≥ 1). Zatem deg H2 = d, ⁺H2 = λ·⁺G1.
   **Tu i tylko tu używamy a_m ∉ J (λ ≠ 0).**
 - H1: deg H1 ≤ d.
j_m = (αX + f(Y), βY + γ), e = deg f ≥ 2, f = c_e Y^e + niższe.
G^{(m)} = j_m∘H = (α H1 + f(H2), β H2 + γ).
 - f(H2) = c_e H2^e + Σ_{i<e} c_i H2^i; ⁺(H2^e) = (⁺H2)^e ≠ 0 (dziedzina), stopień e·d;
   pozostałe składniki mają stopień ≤ (e−1)d < ed; α H1 ma stopień ≤ d < ed (bo e ≥ 2).
   Zatem deg G^{(m)}_1 = ed = d_m, ⁺G^{(m)}_1 = c_e (λ⁺G1)^e.
 - G^{(m)}_2 = βH2 + γ ma stopień d < ed = d_m. ✓ ∎

*Dowód Tw. B.* Z lematu deg(j1∘…∘ak) = d_1 = ∏ deg j_i. Dla a0 ∈ A: składowe a0∘G są
kombinacjami afinicznymi składowych G, więc deg(a0∘G) ≤ deg G; a G = a0⁻¹∘(a0∘G), więc
też ≥. Zatem deg F = ∏ deg j_i. ∎

**Uwaga 1 (charakterystyka).** Nigdzie nie dzielimy ani nie różniczkujemy; jedyny użyty
fakt to ⁺(PQ) = ⁺P·⁺Q ≠ 0 w dziedzinie k[x,y] (stąd ⁺(P^e) = (⁺P)^e ≠ 0) —
prawdziwe w każdej charakterystyce. Nad Q wszystko tym bardziej działa. Zastrzeżenie
z polecenia „problemy z potęgami” dotyczy np. tożsamości typu (a+b)^p = a^p + b^p w char p
— nie mają wpływu, bo patrzymy tylko na formę wiodącą iloczynu.

**Uwaga 2 (forma c·ℓ^d).** Indukcyjnie ⁺G^{(k)}_1 = c_e(⁺v)^e, a ⁺G^{(m)}_1 =
c_e λ^e (⁺G^{(m+1)}_1)^e, więc ⁺G^{(m)}_1 = c·ℓ^{d_m} z ℓ = ⁺(ak)_2 (forma liniowa).
Niepotrzebne do Tw. B, ale potwierdza tezę ze szkicu Friedlanda–Milnora.

**Uwaga 3 (gdzie byłoby skracanie).** Gdy a_m ∈ J (λ = 0), H2 = μG2 + ν ma stopień < d
i f(H2) może mieć stopień mniejszy niż ed; ponadto j_m∘a_m∘j_{m+1} ∈ J, więc
składniki mogą się zredukować (np. (x+y²,y)∘id∘(x−y²,y) = id). Patrz §3.

**Co jest w pełni sprawdzone:** cały dowód powyżej (sprawdziłem każdy krok ręcznie).
**Co jest cytowane:** tylko Tw. A (Jung–van der Kulk), które zapewnia istnienie zapisu
zredukowanego; Tw. B nie wymaga już cytatu. Lemat nie używa jednoznaczności rozkładu.

## 2. Wniosek dla deg F ≤ 5 (UDOWODNIONE przy Tw. A)
Niech F ∉ A, F = a0∘j1∘…∘jk∘ak zredukowane (Tw. A). Każde deg j_i ≥ 2, więc
deg F = ∏ deg j_i ≥ 2^k. Jeśli deg F ≤ 5, to 2^k ≤ 5, czyli k ≤ 2.
Dla k = 2: deg j1·deg j2 ≤ 5 i deg j1, deg j2 ≥ 2. Gdyby któryś był ≥ 3, iloczyn ≥ 6 > 5.
Zatem deg j1 = deg j2 = 2 i deg F = 4. (k = 1: deg F = deg j1 ∈ {2,…,5}.)
To jest dokładnie przesłanka twierdzenia redukcyjnego z iter02/zad1 §3 (F ∈ A ∪ K1 ∪ K2).

## 3. Kontrola obliczeniowa (OBLICZENIOWE) — skrypty/kontrola.py, wynik tmp/kontrola.out
Losowe słowa nad Q (seed 2026, współczynniki a/b, |a| ≤ 9, 1 ≤ b ≤ 5), a_i ∉ J wymuszone
(λ ≠ 0), a0, ak dowolne afiniczne, j_i = (αx + f(y), βy+γ) z deg f zadanym:
- (2,2): 15/15 deg F = 4; (2,3): 15/15 deg = 6; (3,2): 15/15 deg = 6; (2,2,2): 8/8 deg = 8.
Słowa niezredukowane (a1 = id ∈ J):
- (x+y², y)∘id∘(x−y², y) = (x, y): stopień 1 zamiast 4;
- (x+y²+y³, y)∘id∘(x+y², y): stopień 3 zamiast 6 (bo złożenie leży w J).
Kontrast: (x+y², y)∘σ∘(x+y², y), σ = (y,x) ∉ J: stopień 4 = 2·2.
Wniosek: warunek a_i ∉ J jest istotny.

## 4. Ocena argumentu K1 z iter02/zad1 (UDOWODNIONE — rozumowanie poprawne)
F = a∘T∘b, T = (x, y + f(x)), a, b ∈ A. Wtedy a⁻¹∘F = T∘b, a pierwsza współrzędna T∘b
to pierwsza współrzędna b (T nie zmienia x). Oznaczmy L' := (a⁻¹)_1, L := b_1 — afiniczne
i niestałe (a⁻¹, b są bijekcjami afinicznymi, każda ich współrzędna jest niestała).
Zatem L'(F(v)) = L(v) dla wszystkich v, w szczególności L'(q_i) = L(p_i). To 5 równań
liniowych jednorodnych na 6 współczynników (L, L'); jeśli jedynymi rozwiązaniami są
L = L' = stała (jądro (0,0,1,0,0,1) — rachunek iter02/zad1, nie powtarzany), to
sprzeczność. Rozumowanie poprawne; nie wymaga nawet wymierności a, b (rząd macierzy
wymiernej jest taki sam nad każdym rozszerzeniem Q), co jest zgodne z iter03/zad3
(nad R stopnie 2, 3 też wykluczone). Uwaga: K1 obejmuje także k = 1 dla dowolnego deg j1
(Lemat 1 z iter02/zad1), więc stopnie 2, 3, 5 i część stopnia 4 są wykluczone tym lematem.

## Czego nie zrobiono
- Tw. A (Jung–van der Kulk) nadal tylko cytowane (zgodnie z zakresem zadania).
