import json,sys
ok00 = len(sys.argv)>1 and sys.argv[1]=='ok'
et = "UDOWODNIONE" if ok00 else "OBLICZENIOWE"
w={"status":"wynik_negatywny",
"podsumowanie":"Udowodniono elementarnie poprawność i kompletność cechowania kartami 0/1 (każde afiniczne nad Q = β∘r, β∈B) i redukcję F∈K2 do 4 układów. Dla kart (0,1),(1,0),(1,1) certyfikat 1=Σh_j g_j sprawdzony niezależnie w sympy. Dla karty (0,0) certyfikaty lift dla bazy lex (v−P_v(z), m(z)) policzone w Sage"+(" i sprawdzone w sympy" if ok00 else "; sprawdzenie sympy nie zakończyło się w limicie czasu")+"; m(z) nie ma pierwiastków wymiernych (jawnie sprawdzone). Wniosek: brak wymiernego F w K2.",
"najlepszy_stopien":None,
"twierdzenia":[
{"tresc":"Cechowanie kartami (x+sy,ky) i (y,kx) jest poprawne i kompletne nad Q; F∈K2 z F(p_i)=q_i daje wymierny punkt układu jednej z kart (wzory: a1''=γ∘a1∘β0').","etykieta":"UDOWODNIONE","uzasadnienie":"notatki.md §1, rachunek bezpośredni","pliki":[]},
{"tresc":"Dla kart (0,1),(1,0),(1,1) ideał układu = (1): certyfikat 1=Σh_j g_j.","etykieta":"UDOWODNIONE","uzasadnienie":"lift w Sage, niezależna weryfikacja dokładna w sympy","pliki":["skrypty/certyfikaty.sage","skrypty/sprawdz_cert.py","skrypty/cert_01.txt","skrypty/cert_10.txt","skrypty/cert_11.txt"]},
{"tresc":"Karta (0,0): ideał zawiera m(z)=(535274496z²−1533993920z+1)(150994944z³−143066112z²−4457408z−59049)/80823742548148224, bez pierwiastków wymiernych, więc brak punktów wymiernych.","etykieta":et,"uzasadnienie":"lift w Sage (sprawdzony w Sage)"+(" i w sympy" if ok00 else "; sprawdzenie sympy nieukończone")+"; pierwiastki: twierdzenie o pierwiastkach wymiernych, skrypt","pliki":["skrypty/certyfikaty.sage","skrypty/sprawdz_cert.py","skrypty/pierwiastki.py"]},
{"tresc":"W klasie K2 brak wymiernego F z F(p_i)=q_i.","etykieta":et,"uzasadnienie":"z trzech powyższych","pliki":["skrypty/certyfikaty.sage"]}]}
json.dump(w,open('wynik.json','w'),ensure_ascii=False,indent=1)
