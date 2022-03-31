cennik = {'herbata':10, 'kawa':15}
print(cennik)
print(cennik['kawa'])
cennik['kawa'] = 20
print(cennik)
cennik['herbata'] -= 1
print(cennik['herbata'])

cennik['cukier'] = 5

print(cennik)

#pętle po elementach

# przeglądanie kluczy
for x in cennik:
    print(x)

for klucz in cennik.keys():
    print(klucz)

# przegladanie wartości
for x in cennik.values():
    print(x)

# przeglądanie kluczy z wartościami

for klucz, wartosc in cennik.items():
    print(klucz, wartosc)

#to samo mniej wydajnie
for klucz in cennik:
    print(klucz, cennik[klucz])

# kluczem może być dowolny typ możliwy do porównania - str, int, tupla stringów, tupla intów
sale = {
    101: ['matematyka', 'fizyka'],
    102: ['j.polski'],
    111: ['historia', 'geografia', 'WOS'],
    113: []
}

for nr, przedmioty in sale.items():
    print(f'W sali nr {nr} są lekcje: ', end='')
    for p in przedmioty:
        print(p, end=', ')
    print()

faktury = {
    (2020,'110/2020'): 'pomidory',
    (2020, '115/2020'): 'ogórki',
    (2021, '113/2021'): 'sałata',
}

print(faktury[2020, '115/2020'])