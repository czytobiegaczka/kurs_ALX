with open('pan-tadeusz.txt', mode='r', encoding='utf-8') as wejscie,\
     open('posortowany.txt', mode='w', encoding='utf-8') as wyjscie:
    linie = wejscie.readlines()
    linie.sort()
    wyjscie.writelines(linie)

print('Gotowe')