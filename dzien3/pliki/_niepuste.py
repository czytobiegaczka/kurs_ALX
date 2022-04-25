licznik = 0

with open('pan-tadeusz.txt', mode='r', encoding='utf-8') as plik:
   for linia in plik:
       if linia != '\n':
            licznik +=1
            print(f'{licznik}. ', linia, end='')

with open('pan-tadeusz.txt', mode='r', encoding='utf-8') as plik:
   i = 0
   for linia in plik:
       if not linia.isspace():
           i += 1

print('Niepustych linii:', i)