#ERR funkcja()

# Funkcja to jest fragment programu, któremu nadajemy nazwę
def funkcja():
   print('AAA')
   print('BBB')
   print('CCC')


# który można później "wywołać"
print('Początek programu')
print('Wywołuję funkcję po raz pierwszy:')
funkcja()

print('Po raz drugi:')
funkcja()
print()

# Funkcja może przyjmować parametry
def porownaj(x, y):
   if x < y:
       print("mniejsza")
   elif x > y:
       print("większa")
   else:
       print("równa")


# Wówczas podczas wywołania należy podać wartości parametrów
porownaj(3, 4)
x = 5
porownaj(2*10, 4*x)

