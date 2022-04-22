# Napisz funkcję powtórz, która wypisuje podany tekst n razy.

def powtorz(tekst_do_powtorzenia, ilosc_powtorzen):
    for i in range(ilosc_powtorzen):
        print(tekst_do_powtorzenia)


def main():
    tekst = input('Podaj tekst: ')
    n = int(input('Ile razy powtórzyć? '))

    powtorz(tekst, n)


main()