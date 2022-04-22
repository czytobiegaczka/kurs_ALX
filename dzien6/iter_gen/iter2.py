# W tej wersji w obiekcie Parzyste będziemy pamiętać limit górny.
# Iterator będzie generował liczby do tego limitu wyłączając (analogia do range).

class IteratorParzystych:
   def __init__(self, poczatek, limit):
       self.liczba = poczatek-2
       self.limit = limit

   def __next__(self):
       self.liczba += 2
       if self.liczba >= self.limit:
           # gdy chcemy powiadomić Pythona, że iterator już nie da więcej elementów, że to już koniec
           # wtedy wyrzucamy wyjątek StopIteration
           raise StopIteration
       return self.liczba


class Parzyste:
   def __init__(self, limit = 1000):
       self.limit = limit

   def __iter__(self):
       return IteratorParzystych(0, self.limit)


obiekt = Parzyste()
for i in obiekt:
   print(i)
print()


obiekt = Parzyste(100)
for i in obiekt:
   print(i)
print('----')
# kolejna pętla dla tego samego obiektu - od nowa jest tworzony iterator
for i in obiekt:
   print(i)
