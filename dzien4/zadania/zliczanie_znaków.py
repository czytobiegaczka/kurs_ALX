def zlicz_znaki(tekst, poczatek = '<', koniec = '>'):
    ile_znakow = 0
    poziom = 0
    for znak in tekst:
        if znak == poczatek:
            poziom += 1
        elif znak == koniec:
            poziom -= 1
        else:
            ile_znakow += poziom
    return ile_znakow


wprowadz_tekst = 'Ala <ma<a>> kota <psa>'
print(zlicz_znaki(wprowadz_tekst))