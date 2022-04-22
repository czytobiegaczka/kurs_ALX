def parzyste(limit):
   i = 0
   while i < limit:
       yield i
       i += 2

for x in parzyste(10):
   print(x)
print()

for x in parzyste(1000):
   print(x)
print()

lista = [x for x in parzyste(20)]
print(lista)

print(sum(parzyste(100)))
