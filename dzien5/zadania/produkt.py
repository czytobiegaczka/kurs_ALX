class Produkt:
    def __init__(self, id, nazwa, cena):
        self._id = id
        self._nazwa = nazwa
        self._cena = cena

    def __str__(self):
        return f'Produkt "{self._nazwa}", id: {self._id}, cena: {self._cena:.2f} PLN'

    def __repr__(self):
        return f'Produkt({self._id},{self._nazwa}",{self._cena:.2f})'

produkt = Produkt(1, 'Woda', 10.99)
print(produkt)
print(str(produkt))
print(repr(produkt))