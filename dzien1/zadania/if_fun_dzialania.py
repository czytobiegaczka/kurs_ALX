def oblicz(x, y, dzialanie:str) -> int:
    if dzialanie == '+': return x + y
    if dzialanie == '-': return x - y
    if dzialanie == '*': return x * y
    if dzialanie == '/': return x / y
    raise ValueError(f'Nieznane działanie {dzialanie}')


def main():
    while True:

        dzialanie = input('rodzaj działania (Q - aby zakończyć ): ')

        if dzialanie.upper() == 'Q': break
        try:
            x = float(input('pierwsza liczba: '))
            y = float(input('druga liczba: '))

            wynik = oblicz(x, y, dzialanie)
            print(f'{x} {dzialanie} {y} = {wynik}')
        except Exception as e:
            print(e)

if __name__ == '__main':
    main()