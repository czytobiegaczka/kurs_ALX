lista = ['Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań']

print(lista)
print('Liczba elementów:', len(lista))
# Można odczytywać pojedyncze elementy:
print(lista[0])
print(lista[4])

# Po elementach kolekcji można "iterować" za pomocą pętli for
for m in lista:
   print(f' * {m}')
print()

# Zawartość listy można modyfikować.
# O listach mówi się, że są "mutowalne" (mutable).

lista[0] = 'Wawa'
print(lista)

#ERR lista[5] = 'Bydgoszcz'
# print(lista)

# append dodaje jeden element na końcu listy
lista.append('Bydgoszcz')
print(lista)

# insert dodaje nowy element na określonej pozycji
lista.insert(5, 'Toruń')
print(lista)

# extend dodaje wiele elementów (wziętych z innej kolekcji) na koniec
trojmiasto = ['Gdańsk', 'Sopot', 'Gdynia']
# lista.append(trojmiasto)
lista.extend(trojmiasto)
print(lista)
print(len(lista))

# usunięcie elementu z określonej pozycji - operator del
del lista[2]
print(lista)

# usunięcie elementu o podanej wartości - metoda remove
# usuwa pierwsze wystapięnie podanej wartości, a jeśli takiego nie ma, to błąd
lista.remove('Poznań')
print(lista)

# Sprawdzenie czy element należy do listy lub innej kolecji: operator in
if 'Toruń' in lista:
   print('Jest')
else:
   print('Nie ma')

# Można też odnaleźć pozycję, na której jest element
print(lista.index('Toruń'))

# [indeksowanie] posiada dodatkowe możliwości: zakresy ("slicing"), indeksy ujemne...

# elementy 1, 2, 3
print(lista[1:4])
print(lista[0:5:2])
print(lista[5:0:-1])
print(lista[::-1])


