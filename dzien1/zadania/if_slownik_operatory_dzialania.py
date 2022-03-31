import operator

# słownik zawiera funkcje indeksowane znakami działań.
# dla znaku + zapamiętana jest funkcja add itd.
operacje = {
   '+': operator.add,
   '-': operator.sub,
   '*': operator.mul,
   '/': operator.floordiv,
   '^': operator.pow,
}

while True:
   op = input('Podaj operację (Q aby zakończyć): ')
   if op.upper() == 'Q':
       break
   if op not in operacje:
       print(f'Nieznana operacja {op}')
       continue
   try:
       x = int(input('Podaj pierwszą liczbę: '))
       y = int(input('Podaj drugą liczbę: '))
       operacja = operacje[op]
       wynik = operacja(x, y)
       print(f'{x} {op} {y} = {wynik}')
   except Exception as e:
       print(e)
   print()
