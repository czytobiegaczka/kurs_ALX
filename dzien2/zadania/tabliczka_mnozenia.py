#tabliczka mnożenia

kolumna = int(input('kolumna: '))
wiersz = int(input('wiersze: '))
szer = len(str(wiersz*kolumna))+1

for wie in range(1, wiersz+1):
    for kol in range(1, kolumna+1):
        print(f'{wie*kol:{szer}}', end=' ')
    print()