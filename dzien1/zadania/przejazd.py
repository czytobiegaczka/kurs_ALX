miasto_a = input('Miasto A: ')
miasto_b = input('Miasto B: ')
dystans=int(input(f'Dystans {miasto_a} - {miasto_b}: '))
cena = float(input('Cena paliwa: '))
spalanie = float(input('Spalanie na 100 km: '))

print(f'Koszt przejazdu {miasto_a} - {miasto_b} to {dystans * cena * spalanie/100:.0f} PLN')