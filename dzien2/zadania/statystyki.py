# Użytkownik w pętli podaje wiele liczb.
# Ustalamy jakiś sposób kończenia wprowadzania danych,
# np. gdy użytkownik zamiast liczby wpisze słowo koniec

# Na bieżąco dla wporwadzanych liczb są obliczan pewne statysyki, które zostaną wypisane na końcu:
# ilosc, suma, średnia, minimum, maksimum.

ilosc = 0
suma = 0
srednia = 0

print('Podaj liczby (Q - koniec wprowadzania ):  ')

while True:
    tekst = input()
    if tekst.upper() == 'Q':
        break

    liczba = int(tekst)
    ilosc +=1
    suma += liczba

    if ilosc == 1:
        minimum = liczba
        maksimum = liczba

    if liczba < minimum:
        minimum = liczba

    if liczba > maksimum:
        maksimum = liczba

print(f'Wyniki: ')
print(f'ilość: {ilosc}')
print(f'suma: {suma}')

if ilosc > 0:
    srednia = suma / ilosc
    print(f'średnia: {srednia:.2}')
    print(f'minimum: {minimum}')
    print(f'maksimum: {maksimum}')

