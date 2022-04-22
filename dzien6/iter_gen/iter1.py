# Jak wiemy, w Pythonie pętla for pozwala przeglądać listy, zbiory, linie z otwartgo pliku, elementy range...

# O tym czy dany obiekt może być użyty "po prawej stronie w pętli for" decyduje to, czy ten obiekt jest "iterowalny" (iterable).
# Iterowalne są te obiekty, które posiadają metodę __iter__(), która z kolei zwraca iterator.

# Iterator to jest taki obiekt, na który można wielokrotnie wywoływać metodę __next__()
# a ta metoda zwraca wtedy kolejne elementy, które idą do pętli for.

# W tym przykładzie IteratorParzystych pełi rolę iteratora
# Parzyste to jest klasa iterowalna (tak jak iterowalna jest np. lista)
# W tym przykładzie iterator jest nieskończony.

class IteratorParzystych:
   def __init__(self):
       self.liczba = 0

   def __next__(self):
       self.liczba += 2
       return self.liczba


class Parzyste:
   def __iter__(self):
       return IteratorParzystych()


obiekt = Parzyste()
for i in obiekt:
   print(i)





