class Vector:
    '''
    Zaimplementuj klasę Vector dostarczającą funkcjonalność wektora
    swobodnego na dwuwymiarowej płaszczyźnie. Wektory powinny
    mieć możliwość dodawania, odejmowania, mnożenia (przez liczbę),
    porównywania (po długości) oraz powinny posiadać czytelną
    reprezentację napisową.
    Przykład użycia:
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    vector_3 = vector_1 + vector_2
    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def dlugosc(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f'Vector(x={self.x},y={self.y})'

    def __eq__(self, other):
        return self.dlugosc == other.dlugosc

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, liczba):
        return Vector(self.x * liczba, self.y * liczba)

    def __rmul__(self, liczba):
        return Vector(self.x * liczba, self.y * liczba)

    def __lt__(self, other):
        return self.dlugosc < other.dlugosc





a = Vector(3,4)
b = Vector(5,6)
c = a + b
d = a * 5
e = Vector(3,4)
f = b - a
g = 5 * a

print(a)
print(b)
print(a==e)
print(c)
print(d)
print(f)
print(g)

