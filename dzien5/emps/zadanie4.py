from employees import wczytaj_plik

emps = wczytaj_plik('emps.csv')
jakie_stanowisko = input('podaj stanowisko: ')
ilosc = 0
suma = 0
for emp in emps:
    if emp.job_title == jakie_stanowisko:
        ilosc += 1
        suma += emp.salary

srednia = suma / ilosc
print(f'średnia dla stanowiska {jakie_stanowisko} wynosi: {srednia:.2f}')

# średnia dla stanowiska Programmer wynosi: 5760.00