cennik = {
    'długopis': 5,
    'zeszyt': 8,
    'ekierka': 15,
    'plastelina': 20,
}

while True:
    print('\nWybierz operacje:')
    print(' Q - zakończ program')
    print(' P - wypisz cennik')
    print(' K - zakupy')
    print(' C - wprowadź cenę towaru')
    print(' D - usuń towar z cennika')
    print(' I - dodaj towar do cennika')
    wybor = input(": ").strip().upper()
    if wybor == 'Q':
        break
    elif wybor == 'P':
        print('Cennik:')
        for produkt, cena in cennik.items():
            print(f'{produkt:15} : {cena:6} PLN')
        print()
    elif wybor == 'K':
        suma = 0
        print('Podaj listę zakupów (ENTER -  koniec zakupów): ')

        while True:
            produkt = input('nazwa towaru: ')

            if not produkt:
                break

            if produkt not in cennik:
                print('Towaru nie ma w cenniku. Podaj inny towar')
                continue

            ilosc = int(input('Ile sztuk: '))
            suma += cennik[produkt]*ilosc

        print('Do zapłaty: ', suma)

    elif wybor == 'C':
        produkt = input('Podaj nazwę towaru: ')
        cena = int(input('Podaj nową cenę: '))
        cennik[produkt] = cena
        print('Cennik po zmianie:')
        for produkt, cena in cennik.items():
            print(f'{produkt:15} : {cena:6} PLN')
        print()
    elif wybor == 'D':
        produkt = input('Podaj nazwę towaru do usunięcia: ')

        if produkt in cennik:
            del cennik[produkt]
        else:
            print('Brak wskazanego towaru w sklepie')

        print('Cennik po zmianie:')
        for produkt, cena in cennik.items():
            print(f'{produkt:15} : {cena:6} PLN')
        print()
    elif wybor == 'I':
        produkt = input('Podaj nazwę towaru do dodania: ')
        if produkt in cennik:
            print('Towar już jest w cenniku')
        else:
            cena = int(input('Podaj cenę: '))
            cennik[produkt] = cena
            print('Cennik po zmianie:')
            for produkt, cena in cennik.items():
                print(f'{produkt:15} : {cena:6} PLN')
            print()