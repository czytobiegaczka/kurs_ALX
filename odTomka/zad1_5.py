from random import randint
print('Wymyśliłem liczbę z zakresu od 1 do 999. Zgadnij jaka to liczba ;)')
l1 = randint(1, 999)
proba = 1
while True:
    try:
        wynik = int(input(f'Jaka jest Twoja propozycja: '))
        if wynik == l1:
            break
        elif wynik<l1:
            print(f'podana liczba jest za mała!')
        else:
            print(f'podana liczba jest za duża!')
    except Exception:
        print('podaj liczbę całkowitą!!!')
    proba += 1
print(f'Gratulacje. Zgadłeś w {proba} próbie')