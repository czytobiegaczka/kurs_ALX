while True:
   dzialanie = input('Podaj całe działanie (pusty napis, aby zakończyć): ')
   if not dzialanie: break
   try:
       wynik = eval(dzialanie)
       print('Wynik:', wynik)
   except Exception as e:
       print('Błąd', e)
   print()