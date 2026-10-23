# iter02/zad1 — redukcja deg ≤ 5 ⇒ F ∈ K1 ∪ K2 (Jung–van der Kulk)

Oznaczenia: k = Q (argument działa nad dowolnym ciałem). Złożenie zapisujemy jak funkcje:
(f∘g)(v) = f(g(v)). A = grupa automorfizmów afinicznych, J = grupa de Jonquières
J = {(x,y) ↦ (αx + f(y), βy + γ) : α,β ∈ k*, γ ∈ k, f ∈ k[y]}, B = A ∩ J.
σ = (y, x) — zamiana zmiennych (σ ∈ A). t = (x, y + x²), s = (x + y², y) = σ∘t∘σ.

K1 = {a∘(x, y+f(x))∘b : a,b ∈ A, f ∈ k[x]},  K2 = {a2∘t∘a1∘t∘a0 : a_i ∈ A}.
Obie klasy są zamknięte na sprzężenie przez σ (σ ∈ A wchłania się w skrajne czynniki;
dla K2 dodatkowo σ∘t∘σ = s wymaga osobnej uwagi — patrz Lemat 3).

## 1. Cytowane twierdzenia

**Tw. A (Jung 1942 dla k=C, van der Kulk 1953 dla dowolnego ciała).** Dla dowolnego ciała k
Aut_k(k[x,y]) = A *_B J (iloczyn wolny z amalgamacją wzdłuż B = A ∩ J).
Równoważnie: każdy F ∉ A ma zapis F = a0∘j1∘a1∘j2∘…∘jk∘ak, k ≥ 1, z j_i ∈ J∖A,
a_i ∈ A∖J dla 0 < i < k, a0, ak ∈ A dowolne („słowo zredukowane”); długość k jest
wyznaczona jednoznacznie przez F.
Odnośnik: A. van den Essen, *Polynomial Automorphisms and the Jacobian Conjecture*,
Birkhäuser 2000, rozdz. 5.1 (tw. Junga–van der Kulka, Thm 5.1.11 — numer do potwierdzenia
przez redaktora; HIPOTEZA co do numeru, nie co do treści); W. van der Kulk, Nieuw Arch.
Wisk. (3) 1 (1953) 33–41.

**Tw. B (stopień słowa zredukowanego).** Dla słowa zredukowanego jak wyżej
deg F = ∏_{i=1}^{k} deg j_i.
Odnośnik: S. Friedland, J. Milnor, *Dynamical properties of plane polynomial automorphisms*,
Ergodic Theory Dynam. Systems 9 (1989), 67–99, Thm 2.1 / Cor. 2.4 (sformułowane nad C, ale
dowód jest czysto algebraiczny i działa nad każdym ciałem); van den Essen 2000, rozdz. 5.1
(wersja nad dowolnym ciałem); J.-P. Furter, *On the length of polynomial automorphisms of
the affine plane*, Math. Ann. 322 (2002).

**Szkic dowodu Tw. B (składowe najwyższego stopnia).** Dla G = (G1,G2) niech ⁺G_i oznacza
formę wiodącą. Twierdzenie pomocnicze (indukcja po k): dla słowa zredukowanego
H = j1∘a1∘…∘a_{k−1}∘jk∘ak (a0 = id) mamy deg H = ∏ deg j_i, a formy wiodące składowych
H spełniają: ⁺H_1 = c·ℓ^{d}, deg H_2 < deg H_1 = d (ℓ — forma liniowa, c ≠ 0)
— tzn. „stopień skupia się w pierwszej współrzędnej i jest potęgą jednej formy liniowej”.
Krok: j = (αx + f(y), βy+γ), deg f = e ≥ 2; a ∈ A∖J, czyli a ma składową liniową, która nie
zachowuje kierunku osi y w sensie J — konkretnie druga współrzędna a, a_2(x,y), zależy
od x. Wtedy j∘a∘H: druga współrzędna a∘H to a_2(H) i ponieważ a_2 zależy od x (który
niesie ⁺H_1 stopnia d), ma formę wiodącą c'·ℓ^d stopnia d; pierwsza współrzędna j to
αX + f(Y), więc po podstawieniu forma wiodąca to lc(f)·(c'ℓ^d)^e stopnia d·e — brak
skracania, bo jest to jedyny składnik stopnia de (αX ma stopień ≤ d < de). Druga
współrzędna βY+γ ma stopień d < de. Skrajne afiniczne a0 nie zmieniają stopnia
(odwracalne liniowe przekształcenie składowych). Warunek a_i ∉ J jest dokładnie tym,
co wyklucza skracanie. (Szkic — pełny dowód: Friedland–Milnor, Lemat 2.2–Thm 2.1.)
Etykieta: cytowane twierdzenie; szkic dla czytelnika, nie zastępuje odnośnika.

Uwaga: dla j ∈ J∖A mamy deg j = max(1, deg f) i j ∉ A ⇔ deg f ≥ 2, więc deg j_i ≥ 2.

## 2. Lematy o czynnikach

**Lemat 1.** Każde j = (αx + f(y), βy+γ) ∈ J ma postać j = d1∘(x + g(y), y)∘d2 z
d1, d2 ∈ A, deg g = deg f. Dowód: d2 = (αx, βy + γ) (afiniczne, αβ ≠ 0),
g(Y) := f((Y−γ)/β); wtedy (x+g(y),y)∘d2 = (αx + f(y), βy+γ), d1 = id. ∎
Ponadto (x + g(y), y) = σ∘(x, y + g(x))∘σ.

**Lemat 2.** Każde j ∈ J z deg f = 2 ma postać j = d1∘s∘d2, s = (x+y², y), d1,d2 ∈ A,
więc j = d1∘σ∘t∘σ∘d2. Dowód: z Lematu 1 j = (x+g(y),y)∘d2, g(y) = c(y+e)² + h, c ≠ 0.
Wtedy (x + g(y), y) = u∘s∘v, gdzie v = (x/c, y+e), u = (cX + h, Y − e):
s∘v = (x/c + (y+e)², y+e), u∘s∘v = (x + c(y+e)² + h, y). ∎ (sprawdzone sympy:
skrypty/lemat_czynniki.py)

## 3. Twierdzenie redukcyjne (UDOWODNIONE, przy Tw. A, B)

**Tw.** Jeśli F ∈ Aut_Q(Q[x,y]) i deg F ≤ 5, to F ∈ A ∪ K1 ∪ K2. (A ⊂ K1, f = 0.)

Dowód. Jeśli F ∈ A — f = 0 w K1. Inaczej słowo zredukowane długości k ≥ 1 i z Tw. B
deg F = ∏ deg j_i ≥ 2^k, więc k ≤ 2 (2³ = 8 > 5).
- k = 1: F = a0∘j1∘a1. Z Lematu 1: F = a0∘d1∘σ∘(x, y+g(x))∘σ∘d2∘a1 ∈ K1
  (a = a0 d1 σ, b = σ d2 a1 są afiniczne). Obejmuje d = 2,3,4,5.
- k = 2: deg j1·deg j2 ≤ 5, oba ≥ 2 ⇒ deg j1 = deg j2 = 2, deg F = 4. Z Lematu 2:
  F = a0∘d1∘σ∘t∘σ∘d2∘a1∘d1'∘σ∘t∘σ∘d2'∘a2 = a2'∘t∘a1'∘t∘a0' z
  a2' = a0 d1 σ, a1' = σ d2 a1 d1' σ, a0' = σ d2' a2 — afiniczne (A jest grupą,
  wchłanianie poprawne; warunek a1 ∉ J nie jest potrzebny do przynależności do K2).
  Więc F ∈ K2. ∎
Wniosek przypadków: d=1 ⇒ A; d=2,3,5 ⇒ K1 (k=1 jedyne możliwe); d=4 ⇒ K1 (k=1, deg j=4)
lub K2 (k=2, stopnie (2,2)).

Uwaga: współczynniki są wymierne — Tw. A nad k = Q daje czynniki nad Q, a Lematy 1–2
używają tylko działań wymiernych (e = współczynnik/2c, h itd. ∈ Q). Ważne, bo wynik K2
(iter01/zad2) wyklucza tylko rozwiązania wymierne (nad R istnieją!).

## 4. Wniosek dla zadania (deg ≥ 6)

- Lemat K1 (iter01/zad1): F ∈ K1, F = a∘(x,y+f(x))∘b ⇒ pierwsza współrzędna a⁻¹∘F równa
  się x∘b, tj. L'∘F = L, gdzie L' = pierwsza współrzędna a⁻¹, L = pierwsza współrzędna b —
  obie niestałe afiniczne. Stąd L'(q_i) = L(p_i). **Niezależne sprawdzenie** (mój skrypt
  skrypty/lemat_K1.py, sympy, dokładnie): macierz 5×6 ma rząd 5, jądro = (0,0,1,0,0,1),
  tzn. tylko L, L' stałe — sprzeczność. Zatem K1 (a więc i A) nie zawiera rozwiązania.
  Etykieta: UDOWODNIONE (rachunek rzędu macierzy 5×6 dokładny, wynik w tmp/lemat_K1.out).
- K2: brak rozwiązań wymiernych — **OBLICZENIOWE** (iter01/zad2, baza Gröbnera w Sage);
  nie sprawdzałem tego niezależnie.
- Zatem: **deg F ≥ 6 dla każdego automorfizmu nad Q realizującego bijekcję** —
  UDOWODNIONE z zastrzeżeniem, że zależy od wyniku OBLICZENIOWEGO dla K2 oraz od
  cytowanych Tw. A, B. Z rozwiązaniem stopnia 6 (iter01/zad3, ZWERYFIKOWANE) daje to,
  warunkowo, minimalny stopień 6.

## Czego nie zrobiono
- Nie potwierdzono dokładnych numerów twierdzeń w van den Essen (2000) i Friedland–Milnor.
- Szkic dowodu Tw. B jest skrócony (przypadek a_i ∉ J opisany przez „a_2 zależy od x”;
  ściśle: a ∈ A∖J ⇔ część liniowa a nie jest górnotrójkątna w sensie J, tj. druga
  współrzędna zależy od x).
- Niezależna weryfikacja wyniku K2 (np. inną parametryzacją) — do zrobienia.

## Dopisek: porządek indukcji w szkicu Tw. B
Słowo H = j1∘a1∘j2∘…∘jk∘ak (a0 = id). Niezmiennik dla G_m = j_m∘a_m∘…∘jk∘ak:
deg G_{m,1} = ∏_{i≥m} deg j_i =: d_m, deg G_{m,2} < d_m.
Baza m = k: jk∘ak = (α·ak_1 + f(ak_2), β·ak_2 + γ); ak_2 jest niestałą formą afiniczną
(ak odwracalne), więc pierwsza współrzędna ma stopień e = deg f ≥ 2, druga stopień 1 < e.
Krok: G_{m} = j_m∘a_m∘G_{m+1}. Ponieważ a_m ∉ J, druga współrzędna a_m zależy od x:
(a_m)_2 = λX + μY + ν, λ ≠ 0; zatem (a_m∘G_{m+1})_2 ma stopień d_{m+1} (składnik λG_{m+1,1}
dominuje, bo deg G_{m+1,2} < d_{m+1}); pierwsza współrzędna a_m∘G_{m+1} ma stopień ≤ d_{m+1}.
Wtedy (j_m∘…)_1 = α(·)_1 + f((·)_2) ma stopień e·d_{m+1} (forma wiodąca lc(f)·(forma
wiodąca)^e ≠ 0 w pierścieniu bez dzielników zera), a (j_m∘…)_2 = β(·)_2+γ ma stopień
d_{m+1} < e·d_{m+1}. Na koniec a0 odwracalne liniowo miesza składowe — max stopnia
się nie zmienia (deg a0∘H = deg H, bo H = a0⁻¹∘(a0∘H)). ∎ (Ten szkic jest w istocie
pełnym dowodem Tw. B; Tw. A pozostaje cytowane.)
