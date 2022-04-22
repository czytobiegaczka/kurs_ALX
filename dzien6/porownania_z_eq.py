class Osoba:
   def __init__(self, imie, nazwisko):
       self.imie = imie
       self.nazwisko = nazwisko

   def __eq__(self, other):
       return self.imie == other.imie and self.nazwisko == other.nazwisko


# W tej wersji definiujemy metodę eq tak, aby porównywała zawartość obiektów, pola imię i nazwisko

a = Osoba('Ala', 'Kowalska')
b = Osoba('Ala', 'Kowalska')
c = a
o = Osoba('Ola', 'Malinowska')

print(a == a) # T
print(a == b) # T
print(a == c) # T
print(a == o) # F
print()

# Operator is ZAWSZE porównuje adresy
print(a is a) # T
print(a is b) # F
print(a is c) # T
print(a is o) # F