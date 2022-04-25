# Aby odczytać dane z pliku tekstowego, należy ten plik otworzyć:
plik = open('plik.txt')

# zawartość pliku można odczytać na różne sposoby
# read() - czyta cały plik jako jeden obiekt str
tresc = plik.read()
print('1:')
print(tresc)
print()

# pliki należy zamykać
plik.close()

# mode - tryb otwarcia pliku, r-odczyt (domyślnie), w - zapis z czyszczeniem zawartości, a - dopisywanie na końcu
# encoding = kodowanie znaków, domyślnie takie jak w systemie
plik = open('plik.txt', mode='r', encoding='utf-8')

# inny sposób czytania: czytanie pojedynczych linii
# Gdy Python czyta linię z pliku, to wczytuje ją wraz ze znakiem końca linii.
# Na końcu stringa wiersz1 znajduje się znak nowej linii \n
wiersz1 = plik.readline()
print('wiersz1 :', wiersz1)
print('len:', len(wiersz1))

# można podać limit - maks. ilość znaków wczytywanych jednorazowo
wiersz2 = plik.readline(4)
print('wiersz2 :', wiersz2)

wiersz2 = plik.readline()
print('wiersz2a:', wiersz2)

wiersz3 = plik.readline()
print('wiersz3 :', wiersz3)

plik.close()
print()

plik = open('plik.txt')
# całą zawartość, ale od razu podzieloną na linie można odczytać tak:
linie = plik.readlines()
plik.close()

# linie to jest lista wszystkich linii wczytanych do pamięci
print('Ile jest linii?', len(linie))
for linia in linie:
   print(linia, end='')
print()

# Ale nie trzeba wszystkich linii wczytywać na raz do pamięci,
# w Pythonie otwarty plik jest obiektem iterowalnym i za pomocą pętli for można odczytywać kolejne linie tego pliku.
plik = open('plik.txt')
for linia in plik:
   print(linia, end='')
print()
plik.close()

# Natomiast zamiast zamykania plików za pomocą operacji close()
# lepiej jest otwierać je za pomocą konstrukcji with
# dopóki jesteśmy w bloku with możemy korzystać z pliku, a przy wyjściu z tego bloku
# plik zostanie automatycznie zamknięty bez pisania close()

with open('plik.txt', mode='r', encoding='utf-8') as plik:
   for linia in plik:
       print(' *', linia, end='')

# nie trzeba pisać close
print('teraz plik jest zamknięty')

