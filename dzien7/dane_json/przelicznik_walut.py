# Napisz program, który pozwala przeliczać kwotę z PLN na inną walutę i vice versa

# Kolejne funkcjonalności:
# - przeliczanie jednej waluty zgodne z dzisiejszym kursem
# - program raz pobiera kursy, a później działa w pętli i wielokrotnie prosi o podanie waluty i kwoty
# - przy uruchomieniu programu można podać datę i wtedy wczytywane są kursy archiwalne z podanej daty
#   a następnie można wypisać kurs lub przeliczyć kwotę dla wybranej waluty

import requests

ADRES='http://api.nbp.pl/api/exchangerates/tables/A/?format=json'

print('Pobieram dane...')

dane = requests.get(ADRES).json()

tabela = dane[0]

kursy_walut = {}

for rate in tabela["rates"]:
   kursy_walut[rate["code"]] = rate["mid"]

while True:
    try:
        waluta = input('symbol waluty: ').upper()
        if waluta == 'Q':
            break
        if waluta not in kursy_walut:
            print('Nieprawidłowy symbol waluty')
        else:
            ilosc = int(input('kwota PLN: '))
            print(f'dzisiejszy kurs {waluta} - {kursy_walut[waluta]} PLN')
            print(f'{ilosc} PLN = {ilosc * kursy_walut[waluta]} {waluta}')
    except Exception:
        print('Nieprawidłowy symbol waluty lub kwota PLN')







# for kurs in kursy_walut:
#     print(kurs)
#     print(kursy_walut[kurs])
