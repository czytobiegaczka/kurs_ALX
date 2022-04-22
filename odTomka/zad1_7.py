from random import randint
tel = ['+4812300'+str(x)+str(y1)+str(y2)+str(y3) for x in range(1, 6) for y1 in range(0, 10) for y2 in range(0, 10) for y3 in range(0, 10)]
print(f'rozmiar listy: {len(tel)}')
print('dziesięć losowo wybranych numerów:')
print('='*23)
print('lp'+' '*5+'poz'+' '*8+'tel')
print('-'*23)
lic = {i: randint(1, 5000) for i in range(1,11)}
for i, cyk in lic.items():
    print(f'{i:2} -> {cyk:4} {tel[cyk]}')
print('='*23)