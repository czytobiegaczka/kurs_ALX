limit = int(input('limit: '))
szer1 = len(str(limit))
szer2 = len(str(limit**2))
szer3 = len(str(limit**3))

for liczba in range(1, limit+1):
    print(f'| {liczba:{szer1}} | {liczba**2:{szer2}} | {liczba**3:{szer3}} |')