from random import randint

zakres=10
l1 = randint(1, zakres)
l2 = randint(1, zakres)
licz=1
while True:
    try:
        wynik=int(input(f'podaj wynik operacji: {l1}*{l2} ='))
        if wynik==l1*l2:
            break
        else:
            print(f'odpowiedź: {wynik} jest niepoprawna!')
    except Exception:
        print('wynikiem jest liczba całkowita!!!')
    licz += 1
print(f'świetnie - poprawna odpowiedź w {licz} próbie')