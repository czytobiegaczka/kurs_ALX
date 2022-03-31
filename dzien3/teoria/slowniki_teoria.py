cennik = {'herbata': 10, 'kawa': 15}
print(cennik)

# dostęp do wartości poprzez klucz
# odczyt
print('Kawa kosztuje', cennik['kawa'])

# ale także zapis:
cennik['kawa'] = 17
print('Kawa kosztuje', cennik['kawa'])
cennik['herbata'] -= 1
print(cennik)

# w taki sam sposób można dodawać nowe elementy
cennik['woda'] = 5
print(cennik)
print()

# Jak w pętli przejrzeć wszystkie elementy?
# Przy takim zapisie przejrzymy wszystkie klucze:
for klucz in cennik:
   print(klucz)
print()

# To samo uzyskamy pisząć:
for klucz in cennik.keys():
   print(klucz)
print()

# Tak można przejrzeć wartości (tutaj ceny)
for wartosc in cennik.values():
   print(wartosc)
print()

# Aby przejrzeć klucze wraz z wartościami, najlepiej zrobić to tak:
for klucz, wartosc in cennik.items():
   print(f'{klucz} → {wartosc}')
print()

# Można ten efekt uzyskać też w ten sposób, ale będzie to odrobinkę mniej wydajne:
for klucz in cennik:
   print(f'{klucz} → {cennik[klucz]}')
print()

# Kluczami najczęściej są stringi, ale mogą być dowolne obiekty, dla których dobrze zdefiniowane są
# operacja porównywania eq oraz hash.
# Dobrą praktyką jest, aby klucze były typów "niemutowalnych".
# Dobrymi kluczami są: str, int, tupla składająca się ze stringów i intów.
# Złymi kluczami będą: float (bo są pomyłki w obliczeniach i porówanie == jest zdradliwe), list (bo jest mutowalna).
# Wartości w słowniki mogą być zpełnie dowolne.

sale = {
   101: ['matematyka', 'fizyka'],
   102: ['j.polski'],
   111: ['historia', 'WOS', 'geografia'],
   113: [],
}

for nr, przedmioty in sale.items():
   print(f'W sali nr {nr} prowadzone są lekcje: ', end='')
   for p in przedmioty:
       print(p, end=', ')
   print()


faktury = {
   (2020, '113/W'): 'pomidory za 330.00',
   (2020, '115/W'): 'ziemniaki za 330.00',
   (2021, '113/W'): 'inne pomidory',
}

print(faktury[2020, '113/W'])


