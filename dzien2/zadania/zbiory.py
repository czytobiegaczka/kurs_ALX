zbior = set()

print('Podaj liczby (Q - koniec wprowadzania ):  ')

while True:
    tekst = input()
    if tekst.upper() == 'Q':
        break

    zbior.add(int(tekst))

print(zbior)

parzyste = set(range(0, 101, 2))

print(parzyste)

print(len(zbior & parzyste))
print(zbior & parzyste)