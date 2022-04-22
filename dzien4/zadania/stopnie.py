# Zdefiniuj funkcje, które konwertują stopnie Fahrenheita na Celsjusza
# i napisz program

def fahrenheit_na_celsjusz(temperatura):
    return ((5/9) * (temperatura - 32))

def  celsjusz_na_fahrenheit(temperatura):
    return (32 + (9/5) * temperatura)

stopnie = float(input('Podaj ilość stopni do przeliczenia: '))
konwersja = input('w skali F / C ? ').upper()

if konwersja == 'F':
    print(f'{stopnie} stopni Fahrenheit to: {fahrenheit_na_celsjusz(stopnie)} stopni Celsjusza' )
else:
    print(f'{stopnie} stopni Celsjusza to: {celsjusz_na_fahrenheit(stopnie)} stopni Fahrenheit')