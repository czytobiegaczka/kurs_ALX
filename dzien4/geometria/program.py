from  funkcje_geometryczne import *

while True:
    print('wybierz figurę: ')
    print('K - kwadrat')
    print('O - koło')
    print('P - prostokąt')
    print('Z - koniec programu')

    wybor = input('> ').upper()

    if wybor == 'Z':
        break
    elif wybor == 'K':
        a = float(input('podaj długość boku: '))
        pole = pole_kwadratu(a)
        obwod = obwod_kwadratu(a)
    elif wybor == 'O':
        a = float(input('podaj długość promienia: '))
        pole = pole_kola(a)
        obwod = obwod_kola(a)
    elif wybor == 'P':
        a = float(input('podaj długość boku a: '))
        b = float(input('podaj długość boku b: '))
        pole = pole_prostokata(a, b)
        obwod = obwod_prostokata(a, b)
    else:
        print('nie ma takiej opcji')
        continue

print(f'pole = {pole:.2f}, obwod = {obwod:.2f}')