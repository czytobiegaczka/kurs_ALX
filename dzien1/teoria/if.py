from random import randint

x = randint(1, 100)
y = randint(1, 100)
print('Wylosowane liczby:', x, y)

# Podstawowa forma if-a: dwie gałęzie if i else
if x < y:
   print('x jest mniejszy od y')
   print('111111')
else:
   print('x nie jest mniejszy od y')
   print('222222')

# Kiedy wrócimy na poprzedni poziom wcięć, oznacza to, że jesteśmy już poza if-em
# i te instrukcje wykonają się zawsze.
print('a kuku')

# Można napisać if bez towarzyszącego else'a
if (x + y) % 2 == 0:
   print('Suma liczb jest parzysta')

# Dzięki słowu kluczowemu 'elif' możemy tworzyć instrukcje warunkowe, które mają więcej niż 2 gałęzie
# Części elif może być dowolnie wiele. Wykonywana jest pierwsza gałąź z prawdziwym warunkiem.
if x < y:
   print('x < y')
elif x > y:
   print('x > y')
else:
   print('x = y')

# Przykład zastosowania:
if x <= 10:
   print('pierwsza dziesiątka')
elif x <= 20:
   print('druga dziesiątka')
elif x <= 30:
   print('trzecia dziesiątka')
elif x <= 40:
   print('czwarta dziesiątka')
elif x <= 50:
   print('piąta dziesiątka')
else:
   print('51+')

if x > 50:
   if y > 50:
       print('> >')
   else:
       print('> <')
else:
   if y > 50:
       print('< >')
   else:
       print('< <')

# W ekstremalnie prostych sytuacjach, można instrukcję wpisać bezpośrednio za ifem w tej samej linii
# (niektórzy uznają za zły styl)
if x == y: print('liczby są równe')
else: print('nie są równe')

# można też użyć if-a  jako wyrażenia
wieksza = x if x > y else y
print('Większa z liczb jest: ', wieksza)

# spójniki logiczne: and , or, not
if x >= 50 and y >= 50:
   print('obie liczby >= 50')
else:
   print('co najmniej jedna liczba < 50')

if x >= 50 or y >= 50:
   print('co najmniej jedna liczba >= 50')
else:
   print('obie liczby < 50')

# Spójniki logiczne są 'leniwe'
# przykładowo zmienna b nie istnieje, a warunek się wykona bez błędu:
a = 40
if a > 10 or b > 10:
   print('OK')

# W połączeniu z faktem, że inne wartości mogą być traktowane jak wartości logiczne, daje to ciekawe zastosowania:
a = ''
b = 'Python'
c = 'Java'
# wypisze się pierwsza z tych wartości, która nie jest pusta
print(a or b)
print(b or c)

# W Pythonie wartości wielu innych typów są automatycznie konwertowane na wartości logiczne
# Do if-a można przekazywać wartości typu bool, int, float, str, list, ...

# 0 → fałsz
# niezero → prawda
# None (czyli taki Pythonowy null) → fałsz
# pusty napis, pusta lista i inna kolekcja → fałsz
# niepusty napis, lista, kolekcja → prawda

#lista = []
lista = ['Ala', 'Ola', 'Ela']

if lista:
   print('są dane, a pierwszym elementem jest', lista[0])
else:
   print('brak danych')


