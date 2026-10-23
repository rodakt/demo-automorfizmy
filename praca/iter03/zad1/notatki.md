# iter03/zad1 — certyfikat braku wymiernych F ∈ K2 + dowód kompletności kart

## 1. Dowód poprawności i kompletności cechowania (UDOWODNIONE)

Oznaczenia: t=(x, y+x²), B = {β=(cx+e, c²y+lx+f) : c≠0} (nad Q). B jest grupą
(złożenie: (c,e,l,f)∘(c',e',l',f') daje znów element tej postaci; odwrotność też).

**Lemat 1 (t∘β = β'∘t).** t(cx+e, c²y+lx+f) = (cx+e, c²y+lx+f+(cx+e)²)
= (cx+e, c²(y+x²) + (l+2ce)x + f+e²), czyli t∘β = β'∘t, β' = (c, e, l+2ce, f+e²) ∈ B.
Odwzorowanie β↦β' jest bijekcją B→B (odwrotne: l = l'−2ce, f = f'−e²), więc też dla każdego
γ'∈B istnieje γ∈B z γ'∘t = t∘γ. Wszystko wymierne, gdy dane wymierne.

**Lemat 2 (karty).** Każde afiniczne g = (αx+βy+e₁, γx+δy+e₂), Δ=αδ−βγ≠0, nad Q, ma postać
g = b∘r, b∈B nad Q, r jednym z reprezentantów:
- α≠0 (karta 0): r=(x+s·y, k·y), s=β/α, k=Δ/α³ ≠0, b=(c,e,l,f)=(α, e₁, γ, e₂).
  Sprawdzenie: b∘r = (αx+αsy+e₁, α²k y + γx + γsy + e₂) = (αx+βy+e₁, γx+(Δ/α+γβ/α)y+e₂) = g.
- α=0 (karta 1): wtedy Δ=−βγ≠0, więc β≠0, γ≠0; r=(y, k·x), k=γ/β², b=(β, e₁, δ, e₂).
  Sprawdzenie: b∘r = (βy+e₁, β²k x + δy + e₂) = g.
Translacje (e₁,e₂) zawsze wchłania b; przypadek „współczynnik przy x w pierwszej składowej = 0”
to dokładnie karta 1. Przypadki są rozłączne i wyczerpujące.

**Redukcja.** Niech F = a2∘t∘a1∘t∘a0, F(pᵢ)=qᵢ. Piszemy a0 = β0∘r0, a2⁻¹ = β2∘r2 (Lemat 2).
Wtedy F(p)=q ⇔ t∘a1∘t∘β0∘r0(p) = β2∘r2(q). Z Lematu 1: t∘β0 = β0'∘t, a β2⁻¹∘t = t∘γ
dla pewnego γ∈B (β2⁻¹ = γ'). Zatem
  t∘a1''∘t∘r0(pᵢ) = r2(qᵢ),  a1'' := γ∘a1∘β0'  (afiniczne, wymierne, det≠0).
To jest dokładnie układ karty (r0, r2) ze skryptu iter01/zad2/skrypty/k2.sage: niewiadome
s,k (r0), S,K (r2), a..f (a1'' = (a x+b y+e, c x+d y+f)), z z warunkiem z·k·K·(ad−bc)=1;
w karcie 1 skrypt dokłada s=0 (odp. S=0) — zmienna nieużywana, nie zmienia rozwiązalności.
Wniosek: wymierne F∈K2 ⇒ wymierny punkt jednego z 4 układów.

## 2. Certyfikaty (skrypty/certyfikaty.sage, sprawdzenie skrypty/sprawdz_cert.py)

Układ przepisany 1:1 z k2.sage (pierścień Q[s,k,S,K,a,b,c,d,e,f,z]).
- Karty (0,1),(1,0),(1,1): `R(1).lift(I)` daje h_j z 1 = Σ h_j g_j. Pliki skrypty/cert_01.txt,
  cert_10.txt, cert_11.txt (1. linia: generatory g_j; dalej [cel, [h_j]]).
  **Sympy (niezależnie) potwierdza dokładną równość dla wszystkich trzech: OK.**
- Karta (0,0): baza lex (s>k>…>z). Postać: v − P_v(z) dla v ∈ {s,k,S,K,a,b,c,d,e,f} oraz
  m(z) = z⁵ − … (eliminant w z, nie w s jak w iter01 — inny porządek, równoważne).
  Dla każdego z 11 elementów policzono lift (Sage sprawdza Σh_j g_j = cel). Plik
  tmp/cert_00.txt (14 MB — w tmp, nie publikowany; odtwarzalny skryptem w ~30 s).
  Sprawdzenie w sympy: wynik w tmp/sprawdz_00.txt (patrz niżej, stan na koniec pracy).
- m(z) = (1/80823742548148224)·(535274496z² − 1533993920z + 1)(150994944z³ − 143066112z² − 4457408z − 59049).
  skrypty/pierwiastki.py: wyróżnik czynnika kwadratowego 2353137344455868416 nie jest kwadratem;
  dla sześciennego sprawdzono wszystkie 650 kandydatów ±p/q (p|59049, q|150994944) — brak zer.
  Zatem m nie ma pierwiastka wymiernego; punkt wymierny układu (0,0) dawałby wymierne z z m(z)=0.

## 3. Wniosek
W klasie K2 (a2∘t∘a1∘t∘a0, a_i afiniczne nad Q, t=(x,y+x²)) nie ma automorfizmu nad Q z F(pᵢ)=qᵢ.
Uwaga zakresowa: obejmuje to tylko ten kształt słowa; pełny wniosek „stopień ≤5 niemożliwy”
zależy od twierdzenia iter02/zad1 (K1∪K2 wyczerpuje stopnie ≤5) — tu nie sprawdzane.

## Stan sprawdzenia sympy (09:54)
- tmp/cert_00_m.txt (generatory + certyfikat m(z) = Σh_j g_j): **OK** — to wystarcza do wniosku
  (m ∈ I, m bez pierwiastków wymiernych ⇒ brak punktu wymiernego karty (0,0)).
- tmp/cert_00.txt (wszystkie 11 elementów bazy lex): sympy potwierdził s−P_s(z); pozostałe
  9 równań v−P_v(z) nie zdążyły się sprawdzić w sympy (sprawdzone tylko w Sage) — niepotrzebne do wniosku.
- Odtworzenie: `sage skrypty/certyfikaty.sage` (wszystkie karty, ~30 s), potem
  `$PYTHON skrypty/sprawdz_cert.py tmp/cert_*.txt` (karta 00: kilka minut na cel).
