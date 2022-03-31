while True:
    dzialanie = input('rodzaj działania (Q - aby zakończyć ): ')

    if dzialanie.upper() == 'Q': break

    x = float(input('pierwsza liczba: '))
    y = float(input('druga liczba: '))

    if dzialanie == '+': print(f'wynik: {x+y}')
    elif dzialanie == '-': print(f'wynik: {x-y}')
    elif dzialanie == '*': print(f'wynik: {x*y}')
    elif dzialanie == '/':
        if not y: print('nie mozna dzielić przez 0')
        else: (f'wynik: {x/y}')
    else: print('nieprawidłowy rodzaj działania')


    if dzialanie == '+': wynik =  x + y
    elif dzialanie == '-': wynik =  x - y
    elif dzialanie == '*': wynik =  x * y
    elif dzialanie == '/':
        if not y: wynik = 'nie mozna dzielić przez 0'
        else: wynik =  x / y
    else: wynik = 'nieprawidłowy rodzaj działania'

    print('Wynik: ', wynik)