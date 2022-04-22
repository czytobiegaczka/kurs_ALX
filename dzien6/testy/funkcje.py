# W tym pliku umieszczamy przykładowe funkcje, np. silnia
# aby w innych plikach zobaczyć różne podejścia do testowania tych funkcji.

def silnia(n):
   wynik = 1
   for i in range(1, n+1):
      wynik *= i
   return wynik
