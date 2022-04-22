# zadanie: buty u szewca

dni={1: 'niedziela', 2: 'poniedziałek', 3: 'wtorek', 4: 'środa', 5: 'czwartek', 6: 'piątek', 7: 'sobota'}
d=0
while d>7 or d<1:
    d=int(input('w którym dniu tygodnia oddałeś buty do naprawy (od 1 (niedziela) do 7 (sobota): '))
print(f'to był: {dni[d]}')
czas=0
while czas <=0:
    try:
        czas=int(input('za ile dni buty będą do odbioru: '))
    except Exception:
        print('Wymagana całkowita ilość dni!!!!!')
if (d+czas)%7!=0:
    czas=(d+czas)%7
else:
    czas =7
print(f'to będzie: {dni[czas]}')