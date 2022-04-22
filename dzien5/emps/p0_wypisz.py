from employees import wczytaj_plik

emps = wczytaj_plik('emps.csv')
print('Wczytane rekordy: ', len(emps))
for emp in emps:
    print(emp)


