import locale

locale.setlocale(locale.LC_ALL, 'Polish')

with open('pan-tadeusz.txt', mode='r', encoding='utf-8') as wejscie,\
    open('posortowany_pol.txt', mode='w', encoding='utf-8') as wyjscie:
  linie = wejscie.readlines()
  linie.sort(key=locale.strxfrm)
  wyjscie.writelines(linie)

print('Gotowe')

