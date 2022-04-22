from employees import wczytaj_plik

emps = wczytaj_plik('emps.csv')
for emp in emps:
    print(f'{emp.first_name:20} {emp.last_name:20} {emp.salary:20} {emp.city:20}')