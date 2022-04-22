from employees import wczytaj_plik

emps = wczytaj_plik('emps.csv')
suma = 0
for emp in emps:
    suma += emp.salary
srednia = suma / len(emps)
print(f'średnia pensja: {srednia:.2f}')

# średnia pensja: 6461.68