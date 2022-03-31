from  random import randrange, randint

#1
lista = []
N = randrange(100)
print('Wylosowany rozmiar: ', N)

for i in range(N):
    lista.append(randint(1, 10))

print(lista)

#2
suma=0
for l in lista:
    suma +=lista[l]

print(f'suma: {suma}')

#3

for i in range(len(lista)):
    lista[i] += 5

print(lista)

print(sorted(lista))
lista.sort()
print(lista)