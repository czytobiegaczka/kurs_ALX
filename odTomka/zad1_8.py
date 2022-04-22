praca={}
czas={}
with open('logs.txt', mode='r', encoding='utf-8') as plik:
    for linia in plik:
        pola = linia.split(';')
        if pola[1]=='LOGIN':
            czas[pola[0]]=int(pola[2])
        else:
            if pola[0] in praca:
                praca[pola[0]]=praca[pola[0]]+int(pola[2])-czas[pola[0]]+1
            else:
                praca[pola[0]] = int(pola[2])-czas[pola[0]]+1
for u, c in praca.items():
    print(f'{u:7} -> {c:6} cykli')
