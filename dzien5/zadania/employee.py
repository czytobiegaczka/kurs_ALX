# Zadanie #2
# Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu
# pracy oraz wypłacanie pensji na podstawie zadanej stawki
# godzinowej. Jeżeli pracownik będzie pracował więcej niż 8 godzin
# (podczas pojedynczej rejestracji czasu) to kolejne godziny policz
# jako nadgodziny (z podwójną stawką godzinową).
# Przykład użycia:
# >>> employee = Employee('Jan', 'Nowak', 100.0)
# >>> employee.register_time(5)
# >>> employee.pay_salary()
# 500.0
# >>> employee.pay_salary()
# 0.0
# >>> employee.register_time(10)
# >>> employee.pay_salary()
# 1200.0

class Employee:
    def __init__(self, imie, nazwisko, stawka, saldo = 0):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self._saldo = saldo

    def __str__(self):
        return f'employee: {self.nazwisko} {self.imie} stawka wynagrodzenia: {self.stawka} aktualne saldo: {self._saldo}'

    def register_time(self, ilosc_godzin):
        if ilosc_godzin > 8:
            self._saldo += (8 * self.stawka) + ((ilosc_godzin - 8) * (2 * self.stawka))
        else:
            self._saldo += ilosc_godzin * self.stawka

        # self._saldo += self.stawka * ilosc_godzin
        # if ilosc_godzin > 8:
        #     self._saldo += self.stawka * (ilosc_godzin - 8)

    def pay_salary(self):
        salary = self._saldo
        self._saldo = 0
        return salary

        # wersja z try: i finally:
        # try:
        #     return salary
        # finally:
        #     self._saldo = 0

def main():
    employee = Employee('Jan', 'Nowak', 100.0)
    print(employee)
    employee.register_time(5)
    print(employee)
    employee.register_time(4)
    print(employee)
    print(employee.pay_salary())
    print(employee)
    print(employee.pay_salary())
    employee.register_time(10)
    print(employee)
    print(employee.pay_salary())
    print(employee)

if __name__ == '__main__':
   main()


