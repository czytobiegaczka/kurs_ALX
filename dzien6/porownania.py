class Osoba:
   def __init__(self, imie, nazwisko):
       self.imie = imie
       self.nazwisko = nazwisko


# Jeśli w klasie nie jest zdefiniowana metoda __eq__
# to porównanie == sprawdza czy to jest ten sam obiekt (czy adres w pamięci się zgadza)

a = Osoba('Ala', 'Kowalska')
b = Osoba('Ala', 'Kowalska')
c = a
o = Osoba('Ola', 'Malinowska')

print(a == a) # T
print(a == b) # F
print(a == c) # T
print(a == o) # F
print()

# Operator is ZAWSZE porównuje adresy, czyli tu da takie same wyniki
print(a is a) # T
print(a is b) # F
print(a is c) # T
print(a is o) # F