from funkcje import silnia

# Aby program sam sprawdził czy funkcja daje poprawny wynik, możemy porówać ten wynik z oczekiwaną wartością.
# Tutaj użyjemy po prostu if.
# Chociaż zapis jest brzydki i prymitywny, to funkcjonalnie to są już testy jednostkowe:

if silnia(0) == 1:
   print('0 : OK')
else:
   print('0 : FAIL')

if silnia(1) == 1:
   print('1 : OK')
else:
   print('1 : FAIL')

if silnia(5) == 120:
   print('5 : OK')
else:
   print('5 : FAIL')