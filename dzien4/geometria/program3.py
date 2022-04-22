from funkcje_geometryczne import *


def obsluz_kwadrat():
    a = float(input('podaj długość boku: '))
    pole = pole_kwadratu(a)
    obwod = obwod_kwadratu(a)
    return pole, obwod


def obsluz_kolo():
    a = float(input('podaj długość promienia: '))
    pole = pole_kola(a)
    obwod = obwod_kola(a)
    return pole, obwod


def obsluz_prostokat():
    a = float(input('podaj długość boku a: '))
    b = float(input('podaj długość boku b: '))
    pole = pole_prostokata(a, b)
    obwod = obwod_prostokata(a, b)
    return pole, obwod


def main():
    operacje = {
        'K': obsluz_kwadrat,
        'O': obsluz_kolo,
        'P': obsluz_prostokat,
    }
    while True:
        print('wybierz figurę: ')
        print('K - kwadrat')
        print('O - koło')
        print('P - prostokąt')
        print('Z - koniec programu')

        wybor = input('> ').upper()

        if wybor == 'Z':
            break
        elif wybor in operacje:
            pole, obwod = operacje[wybor]()
            print(f'pole = {pole:.2f}, obwod = {obwod:.2f}')
        else:
            print('nie ma takiej opcji')



# Taki charakterystyczny if działa w następujący sposób:
# Gdy uruchamiamy ten plik bezpośrednio jako program → warunek jest prawdziwy i main się wykona
# Gdy importujemy ten plik z innego pliku → warunek jest nieprawdziwy i main się nie wykona

print('Zmienna __name__ ma wartość', __name__)
if __name__ == '__main__':
    main()

