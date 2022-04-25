licznik = 0

with open('pan-tadeusz.txt', mode='r', encoding='utf-8') as plik:
   for linia in plik:
       licznik +=1
       print(f'{licznik}. ', linia, end='')

with open('pan-tadeusz.txt', mode='r', encoding='utf-8') as plik:
   for i, linia in enumerate(plik, 1):
       print(f'{i:5}: {linia.strip()}')

print('Wszystkich linii:', i)
