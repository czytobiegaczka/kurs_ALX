# Metody, których nazwy rozpoczynają się od __,
# np. __str__ , __eq__, __lt__, __add__ itp...
# wpływają na to, co Python ma zrobić z podanym obiektem gdy...
# - ma go wypisać (zamienić na tekst)
# - ma porównać za pomocą ==
# - ma porównać za pomocą <
# - dodać za pomocą +

# Duża część z tych metod pozwala zaimplementować działanie operatorów (+ - * .....)
# dla obiektów danej klasy.
import sys


class Liczba:
   def __init__(self, wartosc=0):
       self.wartosc = wartosc

   def __str__(self):
       # wypisujemy liczbę biorąc ją w [nawiasy]
       return f'[{self.wartosc}]'

   def __repr__(self):
       return f'Liczba({self.wartosc})'

   # operacje arytmetyczne
   def __add__(self, other):
       return Liczba(self.wartosc + other.wartosc)

   def __sub__(self, other):
       return Liczba(self.wartosc - other.wartosc)

   def __mul__(self, other):
       return Liczba(self.wartosc * other.wartosc)

   # dzielenie / to jest truediv
   # dzielenie // to floordiv
   # reszta z dzielenia to jest mod
   def __truediv__(self, other):
       return Liczba(self.wartosc / other.wartosc)

   def __mod__(self, other):
       return Liczba(self.wartosc % other.wartosc)

   # operatory porównania
   def __eq__(self, other):
       return self.wartosc == other.wartosc

   # < , z tego automatycznie zadziała też >
   def __lt__(self, other):
       return self.wartosc < other.wartosc

   # <= , z tego automatycznie zadziała też >=
   def __le__(self, other):
       return self.wartosc <= other.wartosc

   # Twórca klasy w Pythonie może nawet zaimplementować działanie indeksowania za pomocą []
   # tutaj liczba[i] to jest i-ta cyfra licząc od końca
   def __getitem__(self, item):
       return (self.wartosc // 10**item) % 10

   def __setattr__(self, key, value):
       if key == 'wartosc':
           # pozwalam na modyfikację tego atrybutu
           super().__setattr__(key, value)
       else:
           # blokuję możliwość ustawiania innych atrybutów niż wartosc
           print(f'Nie wolno zapisywać atrybutu {key}', file=sys.stderr)


a = Liczba(13)
b = Liczba(17)

print(a)
print(b)
print(repr(b))
print()

c = a + b
print('c jest klasy', type(c), 'i ma wartość', c)

print(b - a)
print(a * b)
print(a / b)
print(a % b)
print()

m = Liczba(50)
n = Liczba(50)

print(m == n)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print()

d = Liczba(98765)
print(d[0])
print(d[1])
print(d[4])
print(d[7])
print()

d.wahadlo = 150
# print(d.wahadlo)
