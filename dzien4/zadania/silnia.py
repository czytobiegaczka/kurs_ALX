def silnia(liczba):
    iloczyn = 1
    for licznik in range(1, liczba+1):
        iloczyn *= licznik
    return iloczyn

while True:
    arg = int(input('Podaj liczbę '))
    if arg < 0:
        break
    wynik = silnia(arg)
    print(f'{arg}! = {wynik}')