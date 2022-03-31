tekst = input('Wprowadź tekst:')

alfabet = {}

for znak in tekst:
    if znak in alfabet:
        alfabet[znak] +=1
    else:
        alfabet[znak] =1

alfabet_get = {}
for znak in alfabet_get:
    ile_było = alfabet_get.get(znak, 0)
    alfabet_get[znak] = ile_było + 1

alfabet_start = {znak: 0 for znak in tekst}
for znak in tekst:
    alfabet_start[znak] += 1

from collections import defaultdict
alfabet_default = defaultdict(int)
for znak in tekst:
    alfabet_default[znak] += 1


print(alfabet)
print(alfabet_get)
print(alfabet_start)
print(alfabet_default)