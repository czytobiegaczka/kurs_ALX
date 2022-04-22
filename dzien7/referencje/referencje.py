from klasy import *

a = Konto(1, 'Ala', 1000)
b = Konto(2, 'Ola', 2000)
c = b

print('a:', a)
print('b:', b)
print('c:', c)
print()

b.wplata(48)
print('a:', a)
print('b:', b)
print('c:', c)
print()

b = a
print('a:', a)
print('b:', b)
print('c:', c)
print()

# Tracimy referencję do konta nr 2
c = b
print('a:', a)
print('b:', b)
print('c:', c)
print()

# Aby ostatecznie stracić referencję do obiektu, można też do zmiennej przypisać None
a = b = None

# W Pythonie można też jawnie usunąć zmienną
del c

# To usuwa zmienną, a nie obiekt. Obiekt na normalnych zasadach MOŻE być postprzątany przez garbage collecotra.

# Teraz odwołanie do zmiennej c kończy się błedem
print('a:', a)
print('b:', b)
#ERR print('c:', c)







