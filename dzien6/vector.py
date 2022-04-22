class Vector:
   def __init__(self, x, y):
       self.x = x
       self.y = y

   def __str__(self):
       return f'<{self.x},{self.y}>'

   def __repr__(self):
       return f'Vector({self.x},{self.y})'

   def __add__(self, other):
       return Vector(x=self.x + other.x, y=self.y + other.y)

   def __sub__(self, other):
       return Vector(x=self.x - other.x, y=self.y - other.y)

   def __mul__(self, num):
       return Vector(x=self.x * num, y=self.y * num)

   def __rmul__(self, num):
       return Vector(x=self.x * num, y=self.y * num)
       # albo: return self.__mul__(num)
       # albo nawet: return num * self

   # dekorator @property powoduje, że aby odczytać wynik tej metody, nie używa się już wywołania
   # v.dlugosc()
   # tylko stosuje się zapis taki jak przy odczycie atrybutu (zmiennej)
   # v.dlugosc
   @property
   def dlugosc(self):
       return (self.x ** 2 + self.y ** 2) ** 0.5

   def __eq__(self, other):
       return self.dlugosc == other.dlugosc

   def __lt__(self, other):
       return self.dlugosc < other.dlugosc

   def __le__(self, other):
       return self.dlugosc <= other.dlugosc

   def __gt__(self, other):
       return self.dlugosc > other.dlugosc

   def __ge__(self, other):
       return self.dlugosc >= other.dlugosc

   def __bool__(self):
       if self.dlugosc != 0.0:
           return True
       else:
           return False


def proste_testy():
   a = Vector(3, 4)
   b = Vector(5, 11)
   print('a:', a)
   print('b:', b)

   print('repr a:', repr(a))
   print('repr b:', repr(b))
   print()

   wynik = a + b
   print(wynik)

   wynik = a - b
   print(wynik)

   wynik = a * 5
   print(wynik)

   wynik = 4 * b
   print(wynik)

   print(a.dlugosc)
   print(b.dlugosc)

   if a:
       print('Wektor nie jest zerowy')


# Ten warunek jest prawdziwy, gdy plik jest uruchamiany bezpośrednio jako program.
# A nie jest prawdziwy, gdy ten plik jest importowany z innego.
# Taki charakterystyczny if zapobiega wykonaniu instrukcji, gdy plik źródłowy jest importowany.
if __name__ == '__main__':
   proste_testy()
