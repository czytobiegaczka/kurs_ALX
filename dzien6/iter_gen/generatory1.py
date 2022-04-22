# Gdy definiujemy funkcję, ale w tej funkcji zamiast return użyjemy słowa yield
# to wynikiem wywołania tej funkcji jest generator.
# Generator będzie dawał kolejne wartości, gdy wywołamy na nim __next__,
# albo (i to jest praktyczne) uzyjemy w pętli for.

def ala():
   yield 'Ala'

print('Początek programu')
generator = ala()
print(generator)

print('next:', generator.__next__())
# print(generator.__next__())

generator = ala()
for imie in generator:
   print('for:', imie)

print('----')

def miasta():
   print('początek działania funkcji miasta')
   yield 'Warszawa'
   print('jestem w środku działania funkcji miasta')
   yield 'Kraków'
   yield 'Toruń'
   yield 'Bydgoszcz'
   yield 'Łódź'
   print('jestem w środku działania funkcji miasta')

print('Zaraz uruchomię funkcję miasta:')
gen = miasta()
print('Teraz zadziała for:')
for m in gen:
   print(m)
print('Koniec pętli for:')
