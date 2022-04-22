# W Pythonie istnieje jeszcze sposób pisania testów nazywany "doctest".
# Gdy w dokumentacji umieszczone są charakterystyczne linie z >>>
# to mogą one być potraktowane jako kod do wykonania, a linie poniżej podają oczekiwany wynik.
# W PyCharmie uruchamia się to jako doctest.
# Ten plik (nie ma tu innego kodu) można uruchomić Ctrl+Shift+F10

class Employee:
    """
    Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu
    pracy oraz wypłacanie pensji na podstawie zadanej stawki
    godzinowej. Jeżeli pracownik będzie pracował więcej niż 8 godzin
    (podczas pojedynczej rejestracji czasu) to kolejne godziny policz
    jako nadgodziny (z podwójną stawką godzinową).
    Przykład użycia:
    >>> employee = Employee('Jan', 'Nowak', 100.0)
    >>> employee.register_time(5)
    >>> employee.register_time(4)
    >>> employee.pay_salary()
    900.0
    >>> employee.pay_salary()
    0.0
    >>> employee.register_time(10)
    >>> employee.pay_salary()
    1200.0
    """

    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.kasa = 0

    def register_time(self, godziny):
        self.kasa += godziny * self.stawka
        if godziny > 8:
            self.kasa += (godziny - 8) * self.stawka

    def pay_salary(self):
        try:
            return self.kasa
        finally:
            self.kasa = 0.0
