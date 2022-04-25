suma = 0
licznik = 0

stanowiska = {joby: 0 for stan in plik}


with open('emps.csv') as plik:
    plik.readline()
    for linia in plik:
        pola = linia.split(';')
        print(f'Pracownik: {pola[1]:20} {pola[2]:20} zarabia {pola[4]}')
        licznik +=1
        suma += int(pola[4])
        #job.add(pola[3])
        stanowiska[pola[3]] += 1

print(f'Srednia: {suma/licznik:.2f}')
print(job)

stanowisko = input('Stanowisko: ')
print(stanowisko)

sr_stanowisko=



