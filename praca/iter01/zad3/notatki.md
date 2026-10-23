# iter01/zad3 — szybka konstrukcja stopnia < 16

## Wynik
`rozwiazanie_6.json` — stopień **6**, przyjęty przez lokalny weryfikator (`ok: true`, stopnie czynników [2, 3]).
F = L⁻¹ ∘ T2 ∘ T1 (T1 działa pierwszy), gdzie
- T1 = (x, y + f(x)), f = 8/3·x² − 3x − 8/3,
- T2 = (x + g(y), y), g = y³/96 − y²/8 − 25y/24 + 1/2,
- L(q) = M q, M = [[-3,0],[3,-1]], czyli L⁻¹ = [[-1/3,0],[-1,-1]].
Skrypt: `skrypty/deg6.py`.

## Metoda (pomysł)
Bez zmiany afinicznej na początku: punkty p mają tylko 3 różne współrzędne x (−1: A,D; 1: B,C; 2: E).
Szukamy v_i = L(q_i) (L afiniczne, 6 parametrów) tak, by:
1. T1 przesuwało p_i pionowo do wysokości v_i,y: f(p_x) = v_y − p_y musi być spójne dla A,D i dla B,C
   (2 warunki liniowe na L) ⇒ f interpoluje 3 wartości ⇒ deg f ≤ 2. Wychodzi c=3, d=−1 (druga linia M).
2. T2 przesuwało poziomo: g(v_y) = v_x − p_x. Przy c=3, d=−1 punkty D i E dostają tę samą wysokość v_y;
   wymuszamy zgodność wartości g dla D,E (warunek liniowy a+3b=−3) ⇒ g interpoluje 4 wartości ⇒ deg g ≤ 3.
Stopień złożenia = 2·3 = 6. Wybrano a=−3, b=0, s=0.

## Sprawdzone negatywnie (OBLICZENIOWE, wąska klasa)
`skrypty/deg4.py`: w tej samej rodzinie (pierwszy czynnik = identyczność, T1 typu „zmienia y”, potem T2 typu
„zmienia x”, potem afiniczne; z tymi samymi koincydencjami A~D, B~C po x i D~E po y) nie da się uzyskać deg g ≤ 2:
3. różnica dzielona = −(a+3b)/96 − 1/48 = 1/96 ≠ 0 przy a+3b=−3. To NIE jest ograniczenie dolne — dotyczy
tylko tej rodziny (inne afiniczne B na początku, inne koincydencje, więcej czynników nie były badane).

## Czego nie zrobiono
- Nie badano ogólnego B (afiniczne na początku) ani słów z 3+ czynnikami nieafinicznymi dla stopni 4–5.
- `skrypty/szukaj.py` — pierwsza (nieudana) próba losowa; ujawniła, że D i E mają wspólne y, co dało pomysł.
- Brak jakichkolwiek twierdzeń o minimalności: 6 to najniższy znaleziony tu stopień.
