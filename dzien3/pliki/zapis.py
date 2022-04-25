# Aby zapisać coś do pliku tekstowego, należy plik otworzyć w trybie 'w' (lub ewentualnie 'a')

with open('nowy1.txt', mode='w', encoding='utf-8') as plik:
   plik.write('Abecadło z pieca spadło.')
   plik.write('Hahaha.')
   # write nie dodaje znaku nowej linii.
   # jeśli chcemy go wpisać, to trzeba jawnie \n
   # (albo użyć print - zobacz dalej...)
   plik.write('\n')

   linie = [
       'Ala ma kota',
       ' albo dwa\n',
       'Ola ma psa\n',
   ]
   plik.writelines(linie)

   # Można też użyć operacji print z dodatkową opcją file
   print('Ala', 2**8, 'Ela', file=plik)

