#Przewoźnik lotniczy ma następujące wymagania co do bagażu podręcznego:
# * żaden z trzech wymiarów nie może przekroczyć 50 cm
# * objętość bagażu nie może przekroczyć 100000 cm³

#Napisz program, który wczytuje trzy wymiary w cm i informuje czy bagaż spełnia normę, czy nie.

x = int(input('piwerwszy wymiar: '))
y = int(input('drugi wymiar: '))
z = int(input('trzeci wymiar: '))
print(f'objętość:  {x * y * z} cm3')

# wersja 1
if x <= 50 and y <= 50 and z <= 50 and (x * y * z) <= 100_000:
    print('bagaż spełnia normę')
else:
    print('bagaż nie spełnia normy')

# wersja 2
if x > 50: print('zbyt duży pierwszy wymiar')
elif y > 50: print('zbyt duży drugi wymiar')
elif z > 50: print('zbyt duży trzeci wymiar')
elif (x*y*z) > 100_000:
    print('zbyt duża objętość')
else:
    print('Bagaż spełnia normę')

# wersja 3

bledy = []
if x > 50: bledy.append('zbyt duży pierwszy wymiar')
if y > 50: bledy.append('zbyt duży drugi wymiar')
if z > 50: bledy.append('zbyt duży trzeci wymiar')
if (x*y*z) > 100_000: bledy.append('zbyt duża objętość')


if not bledy:
    print('Bagaż spełnia normę')
else:
    print('Bagaż nie spełnia normy z powodu błędów: ')
    for blad in bledy:
        print(' *', blad)