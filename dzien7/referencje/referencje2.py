from klasy import *

def funkcja(a, b, c, x):
   print('Początek funkcji:')
   print('a:', a)
   print('b:', b)
   print('c:', c)
   print('x:', x)
   print()

   x += 55

   # modyfikujemy obiekt wewnątrz, zmieniamy jego stan, atrybut saldo
   b.wplata(44)

   # do zmiennej lokalnej wpisujemy referencję do innego obiektu
   # tę zmianę widzi tylko funkcja, a main nie widzi
   a = Konto(a._numer, a._wlasciciel, a._saldo)
   a.wplata(24)
   a._wlasciciel.imie = 'Alicja'

   print('Koniec funkcji:')
   print('a:', a)
   print('b:', b)
   print('c:', c)
   print('x:', x)
   print()


def main():
   ala = Osoba('Ala', 'Kowalska', 20)
   ola = Osoba('Ola', 'Malinowska', 30)
   a = Konto(1, ala, 1000)
   b = Konto(2, ola, 2000)
   c = b
   x = 5000

   print('Początek main:')
   print('a:', a)
   print('b:', b)
   print('c:', c)
   print('x:', x)
   print()

   funkcja(a, b, c, x)

   print('Koniec main:')
   print('a:', a)
   print('b:', b)
   print('c:', c)
   print('x:', x)
   print()


if __name__ == '__main__':
   main()









