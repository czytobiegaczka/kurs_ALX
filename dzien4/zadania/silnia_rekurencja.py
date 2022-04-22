def silnia(liczba):
    if liczba <= 1:
        return 1
    return liczba * silnia((liczba - 1))

while True:
    arg = int(input('Podaj liczbę '))
    if arg < 0:
        break
    wynik = silnia(arg)
    print(f'{arg}! = {wynik}')