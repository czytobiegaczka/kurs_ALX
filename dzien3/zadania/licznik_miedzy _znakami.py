tekst = input('Wprowadź tekst:')

print(len(tekst[tekst.index('<')+1:tekst.index('>')]))
print(tekst.find('>')-tekst.find('<')-1)

czy_liczyc = False
licznik = 0
for znak in tekst:
    if znak == '<':
        czy_liczyc = True
    elif znak == '>':
        czy_liczyc = False
    elif czy_liczyc:
        licznik += 1

print(licznik)