tekst = input('Wprowadź tekst:')

gloski = {'a', 'e', 'i', 'o', 'u', 'y'}
# gloski = 'aeiouy' - inna wersja
suma = 0

for litera in tekst.lower():
    if litera in gloski:
        suma +=1

print(f'Głoski: {gloski} występują w tekście: {suma} razy')

samo = [znak for znak in tekst.lower() if znak in 'aeiouy']
print(samo)
print(len(samo))

samo = ['*' for znak in tekst.lower() if znak in 'aeiouy']
print(samo)
print(len(samo))