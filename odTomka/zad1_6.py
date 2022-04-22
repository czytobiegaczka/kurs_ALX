from random import randint, choices


def przesun(krok, gdzie):
    if krok == 'A':
        gdzie = (gdzie[0] - 1, gdzie[1])
        return gdzie
    elif krok == 'D':
        gdzie = (gdzie[0] + 1, gdzie[1])
        return gdzie
    elif krok == 'W':
        gdzie = (gdzie[0], gdzie[1] + 1)
        return gdzie
    else:
        gdzie = (gdzie[0], gdzie[1] - 1)
        return gdzie

def ico(gdzie_n, gdzie, skarb):
    if abs(skarb[0]-gdzie_n[0])<abs(skarb[0]-gdzie[0]) or abs(skarb[1]-gdzie_n[1])<abs(skarb[1]-gdzie[1]):
        print('dobrze - zbliżasz się')
        return True
    else:
        print('kiepsko - oddalasz się')
        return False

def param_pocz(szukf):
    skarbi = (randint(1, 10), randint(1, 10))
    return skarbi, abs(skarbi[0]-szukf[0])+abs(skarbi[1]-szukf[1]), 0

szuk_p = (randint(1, 10), randint(1, 10))
skarb, min_krok, licz = param_pocz(szuk_p)
szuk=szuk_p
wybor = ['A', 'W', 'S', 'D']
los = [0, 1]
wyszlo = [.2, .8]
print('Szukasz skarbu na planszy o wymiarach 10 na 10.\nWylosowałem pozycję skarbu i Twoją.\nZnajdź skarb.')
print('\nSterowanie:\n\tA -> lewo\n\tD -> prawo\n\tW -> góra\n\tS -> dół')
while True:
    krok = input('Twój ruch: ')
    if krok.upper() in wybor:
        szuk_n = przesun(krok.upper(), szuk)
        if choices(los, wyszlo) == [1]:
            ico(szuk_n, szuk, skarb)
        szuk=szuk_n
        if szuk==skarb or szuk[0]>10 or szuk[0]<1  or szuk[1]>10 or szuk[1]<1:
            break
    else:
        print('nieznane polecenie 8(')
    licz+=1
    if licz>min_krok*2:
        print(f'Dwukrotnie przekroczyłeś minimalną liczbę kroków potrzebnych na dotarcie do skarbu. \n'
              f'Niestety skarb został przeniesiony do nowej lokalizacji\nRozpoczynasz poszukiwania od nowa')
        skarb, min_krok, licz = param_pocz(szuk)
        szuk_p=szuk

if szuk==skarb:
    print(f'Brawo po {licz} posunięciach znalazłeś skarb na współżędnych: {skarb}, twój punkt startowy: {szuk_p}')
else:
    print(f'Fatalnie po {licz} posunięciach wypadłeś poza planszę osiągając współżędne: {szuk}, twój punkt startowy: {szuk_p}')