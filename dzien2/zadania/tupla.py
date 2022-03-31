lista = [10, 8, 9, 12, 14, 25, 33, 58, 159, 645]

print(lista[1])
print(lista[-2])
print(lista[2:7])
print(lista[::3])
print(lista[::-2])

lista=[]
for i in range(101):
    lista.append(i)

print(lista)

suma = 0
for i in range(len(lista)):
    if lista[i] % 5 == 0:
        print(lista[i])
        suma +=1

print(suma)