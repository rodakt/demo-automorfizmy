# Dziennik eksperymentu

Start: 23.10.2026 09:30

## Etap 0

Znana konstrukcja (dwa odwzorowania trójkątne z interpolacji) zapisana w praca/iter00/baza/.


## Iteracja 01 — plan

Wiemy tylko tyle, że konstrukcja bazowa daje zweryfikowany stopień 16 (m=5); stopień 1 jest wykluczony prostym argumentem (p₁..p₄ tworzą równoległobok, obrazy nie). Planujemy oprzeć ograniczenia dolne na twierdzeniu Junga–van der Kulka: stopień zredukowanego słowa to iloczyn stopni czynników trójkątnych, więc stopnie pierwsze to klasa „afiniczne∘jedno trójkątne∘afiniczne”, a stopień 4 to dodatkowo złożenia dwóch kwadratowych. Zadanie 1 rozstrzyga klasę z jednym czynnikiem trójkątnym (liniowy warunek L(pᵢ)=L'(qᵢ)) i dowodzi niemożliwości stopnia 1; zadanie 2 rozstrzyga Gröbnerem w Sage złożenia dwóch kwadratowych (stopień 4). Zadanie 3 równolegle zabezpiecza ograniczenie górne, szukając konstrukcji stopnia 6–9 (pary stopni (2,3), (3,3), trzy kwadratowe). Jeśli (1) i (2) dadzą wyniki negatywne, a (3) rozwiązanie stopnia 6, kolejna iteracja zajmie się stopniem 5 (pokryte przez (1)) i dowodem pełnej listy dla stopnia 6.
