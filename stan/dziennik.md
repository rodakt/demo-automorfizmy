# Dziennik eksperymentu

Start: 23.10.2026 09:30

## Etap 0

Znana konstrukcja (dwa odwzorowania trójkątne z interpolacji) zapisana w praca/iter00/baza/.


## Iteracja 01 — plan

Wiemy tylko tyle, że konstrukcja bazowa daje zweryfikowany stopień 16 (m=5); stopień 1 jest wykluczony prostym argumentem (p₁..p₄ tworzą równoległobok, obrazy nie). Planujemy oprzeć ograniczenia dolne na twierdzeniu Junga–van der Kulka: stopień zredukowanego słowa to iloczyn stopni czynników trójkątnych, więc stopnie pierwsze to klasa „afiniczne∘jedno trójkątne∘afiniczne”, a stopień 4 to dodatkowo złożenia dwóch kwadratowych. Zadanie 1 rozstrzyga klasę z jednym czynnikiem trójkątnym (liniowy warunek L(pᵢ)=L'(qᵢ)) i dowodzi niemożliwości stopnia 1; zadanie 2 rozstrzyga Gröbnerem w Sage złożenia dwóch kwadratowych (stopień 4). Zadanie 3 równolegle zabezpiecza ograniczenie górne, szukając konstrukcji stopnia 6–9 (pary stopni (2,3), (3,3), trzy kwadratowe). Jeśli (1) i (2) dadzą wyniki negatywne, a (3) rozwiązanie stopnia 6, kolejna iteracja zajmie się stopniem 5 (pokryte przez (1)) i dowodem pełnej listy dla stopnia 6.

## Iteracja 02 — plan

Mamy zweryfikowane rozwiązanie stopnia 6 (czynniki trójkątne 2 i 3) oraz dwa wyniki negatywne z iteracji 01: klasa „jedno trójkątne między afinicznymi” (dowolnego stopnia) jest pusta, a złożenia dwóch trójkątnych stopnia 2 nie mają rozwiązań wymiernych (5 rozwiązań nad Q̄, m.in. nad Q(√94)). Przy twierdzeniu Junga–van der Kulka każdy automorfizm stopnia ≤ 5 należy do jednej z tych klas, więc najlepszy znaleziony stopień 6 byłby minimalny — ale to wciąż wymaga domknięcia. Zadanie 1 pisze staranny dowód redukcji „deg ≤ 5 ⇒ K1 ∪ K2” z dokładnym sformułowaniem JvdK i niezależnie sprawdza lemat K1. Zadanie 2 niezależnie (inne cechowanie, rachunek modularny, test kontrolny) potwierdza brak wymiernych elementów K2, bo to najsłabsze ogniwo — pojedyncza implementacja. Zadanie 3 buduje jawnie automorfizmy stopnia 4 nad Q(√94) i dokładnie sprawdza, że realizują bijekcję, co potwierdza poprawność kodowania układu. Jeśli wszystkie trzy się zgodzą, następna iteracja może zakończyć eksperyment.
