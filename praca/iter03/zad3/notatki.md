# iter03/zad3 — nad R (i C) najniższy stopień tej bijekcji = 4

## (1) Ograniczenie górne: deg 4 nad Q(√94) ⊂ R (OBLICZENIOWE)
Automorfizm F=(F1,F2), G=F⁻¹ z iter02/zad3 (notatki tamże, punkt 1), współczynniki w Q(r),
gdzie 15r²+38r−1=0, tj. r=(−19±2√94)/15 (UWAGA: w iter02/zad3 napisano „(−19±√94)/15” — błąd zapisu;
poprawnie 2√94, dyskryminanta 1504=16·94). Oba pierwiastki rzeczywiste (≈0.02605, ≈−2.5594), więc F ma
współczynniki rzeczywiste przy każdym osadzeniu. Pełne F1,F2,G1,G2 (z r): `skrypty/FG_r.txt`
(skopiowane z praca/iter02/zad3/notatki.md); wstawiając r = (−19±2√94)/15 dostaje się jawne wyrażenia z √94.
Niezależne sprawdzenie (moje skrypty):
- `skrypty/sprawdz_R_szybkie.py` (sympy, redukcja mod 15r²+38r−1, dokładnie): F(p_i)=q_i dla i=1..5 — True;
  deg F1=deg F2=deg G1=deg G2=4. Wyjście: tmp/szybkie.out.
- `skrypty/zlozenie.sage` (Sage, ciało liczbowe Q(r), dokładnie): F∘G=id i G∘F=id — wynik w tmp/zlozenie.out
  — WYNIK: G∘F=id True, F∘G=id True, deg [4,4,4,4], Q(r)≅Q(√94) True, 2 osadzenia rzeczywiste. (Wersja sympy składania była za wolna — usunięta.)
Uwaga: F(p_i)=q_i sprawdzono symbolicznie w Q(r) bez wyboru pierwiastka — działa dla obu osadzeń.

## (2) Ograniczenie dolne nad R i C: deg ≥ 4
- deg 1 (UDOWODNIONE + rachunek): p1+p3−p2−p4 = (0,0) (kwadrat), a q1+q3−q2−q4 = (−1,−3) ≠ 0.
  Afiniczne F(x)=Ax+t spełnia F(p1)+F(p3)−F(p2)−F(p4) = A(p1+p3−p2−p4) = 0 — sprzeczność. Niezależne od ciała.
- deg 2, 3 (UDOWODNIONE przy cytowanych tw.): tw. Junga–van der Kulka (dowolne ciało, w szczególności R, C)
  + multiplikatywność stopnia słowa zredukowanego (Tw. B w iter02/zad1/notatki.md, §3; też dowolne ciało):
  słowo zredukowane długości k ma stopień = iloczyn stopni czynników trójkątnych ≥ 2^k; deg ∈ {2,3} ⇒ k=1,
  ⇒ F = a∘(x, y+f(x))∘b, a,b afiniczne nad tym samym ciale (Lemat 1 z iter02/zad1 używa tylko działań ciała).
  Wtedy L := 1. współrzędna b, L' := 1. współrzędna a⁻¹ są niestałymi funkcjami afinicznymi i L'∘F = L,
  więc L'(q_i) = L(p_i). To jednorodny układ liniowy na (l1,l2,l3,m1,m2,m3) z macierzą 5×6 o wyrazach
  WYMIERNYCH; rząd = 5 nad Q (sprawdzone ponownie: tmp/szybkie.out), a rząd macierzy nie zmienia się przy
  rozszerzeniu ciała (minory ≠ 0 pozostają ≠ 0) ⇒ nad R i C jądro = span(0,0,1,0,0,1), czyli L, L' stałe —
  sprzeczność. Zatem nad R, C brak automorfizmów stopnia 2 i 3 (ani 1).
- Ten sam argument wyklucza też deg 5 i część deg 4 (k=1), ale to tu niepotrzebne.

## (3) Wniosek
- Nad R: min stopień = 4 (dolne: UDOWODNIONE przy tw. JvdK i multiplikatywności stopnia — klasyczne,
  cytowane; górne: OBLICZENIOWE, dokładna arytmetyka w Q(√94)). Nad C — to samo (Q(√94) ⊂ R ⊂ C,
  dolne ograniczenie niezależne od ciała charakterystyki 0).
- Nad Q: najniższy znaleziony = 6 (ZWERYFIKOWANE), deg ≤ 5 wykluczone warunkowo na wynik OBLICZENIOWY
  dla K2 (iter01/zad2, iter02). Różnica 4 vs 6 jest arytmetyczna (punkty bazy układu K2 nie są wymierne).
- Rozwiązań nie zapisano jako rozwiazanie*.json (niewymierne współczynniki — niedozwolone).
