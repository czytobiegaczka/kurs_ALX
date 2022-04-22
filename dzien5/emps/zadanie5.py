from employees import wczytaj_plik
from collections import defaultdict

stanowiska = defaultdict(lambda:[0,0])

emps = wczytaj_plik('emps.csv')
print('Wczytane rekordy: ', len(emps))
for emp in emps:
    stanowiska[emp.job_title][0] += emp.salary
    stanowiska[emp.job_title][1] += 1

for stanowisko in stanowiska:
    print(f'średnia dla {stanowisko:40} - {stanowiska[stanowisko][0]/stanowiska[stanowisko][1]}')

