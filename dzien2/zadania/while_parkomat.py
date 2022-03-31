"""
Przyjmijmy, że godzina parkowania kosztuje 3 zł.

Program pyta użytkownika o liczbę godzin parkowania ("Ile godzin będziesz parkować").
Program oblicza i wypisuje kwotę do zapłaty.
Następnie W PĘTLI program:
- prosi o wrzucenie kolejnej monety (po prostu input)
- aż zostanie zebrana wymagana suma.
Na końcu, jeśli trzeba, parkomat powinien wydać resztę.
"""

from datetime import datetime, timedelta
cena = 3
czas = int(input('Czas parkowania: '))
money = int(input('moneta: '))
limit = datetime.now()
limit += timedelta(hours=czas)


while money < cena*czas:
    print(f'wpłacone: {money} PLN')
    money += int(input('moneta: '))

print(f'reszta: {money-(cena*czas)} PLN')
print(f'koniec parkowania: {limit.strftime("%H:%M:%S")}')