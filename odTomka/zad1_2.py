def czy_tr(k):
    if k[0]+k[1]>k[2] and k[1]+k[2]>k[0] and k[0]+k[2]>k[1] and k[0]>0 and k[1]>0 and k[2]>0:
        return True
    else:
        return False
def daj_ramie(i):
    while True:
        try:
            a = float(input(f'długość - bok {i}: '))
            return a
        except Exception:
            print('liczbę poproszę!!')

while True:
    print('Podaj wymiary trójkąta')
    tr = []
    for i in range(1, 4):
        tr.append(daj_ramie(i))
    if czy_tr(tr):
        break
    else:
        print('z tego, to trójkąt nie wyjdzie!!!')
ob=(tr[0]+tr[1]+tr[2])/2
pole=(ob*(ob-tr[0])*(ob-tr[1])*(ob-tr[2]))**0.5
print(f'pole trójkąta o wymiarach {tr[0]}, {tr[1]}, {tr[2]} wynosi: {pole:.2f}')