tekst = input('Wprowadź tekst: ')
ilosc = int(input('Ilość powtórzeń: '))

for i in range(ilosc):
    print(f'{i+1}. {tekst}')