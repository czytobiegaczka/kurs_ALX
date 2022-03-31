#choinka
def utw_cho(poz, kier, zakres):
    zdanie=''
    if kier>0:
        odwr=poz
    else:
        odwr=zakres-poz+1
    for i in range(1, odwr * 2):
        zdanie = zdanie + '*'
    i = zakres - odwr
    while i > 0:
        zdanie = " " + zdanie
        i -= 1
    return zdanie


while True:
    try:
        poziom=int(input('podaj liczbę poziomów choinki: '))
        if poziom != 0:
            break
    except Exception:
        print('Wymagana liczba całkowita różna od 0!!!!!')

kier=1
if poziom<0:
    kier=-1
    poziom=-poziom
print(f'poziom: {poziom}')
for i in range(1, poziom+1):
    zapis = utw_cho(i, kier, poziom)
    print(zapis)