#Napisz program wyliczający kwotę należną za zakupiony towar na
#podstawie ceny za kilogram oraz liczby zakupionych kilogramów. Do
#przechowywania informacji o cenie oraz liczbie kilogramów użyj
#zmiennych. Wypisz wszystkie informacje na konsolę.
#Przykładowy komunikat programu:
#Cena za kg: 10.0
#Waga: 2.5
#Należność: 25.0

cena = float(input('Podaj cenę: '))
ilosc = float(input('Podaj ilość: '))

print(f'Cena za kg: {cena}')
print(f'Waga: {ilosc}')
print(f'Należność: {ilosc*cena:.2f}')