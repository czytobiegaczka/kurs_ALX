class Employee:
    def __init__(self, imie, nazwisko, stawka, saldo=0):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.saldo = saldo

    def __str__(self):
        return f'employee: {self.nazwisko} {self.imie} stawka wynagrodzenia: {self.stawka} aktualne saldo: {self.saldo}'

    def register_time(self, ilosc_godzin):
        if ilosc_godzin > 8:
            self.saldo += (8 * self.stawka) + ((ilosc_godzin - 8) * (2 * self.stawka))
        else:
            self.saldo += ilosc_godzin * self.stawka

    def pay_salary(self):
        salary = self.saldo
        self.saldo = 0
        return salary


class PremiumEmployee(Employee):

    def give_bonus(self, bonus):
        self.saldo += bonus


def main():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    print(employee)
    employee.register_time(5)
    print(employee)
    employee.give_bonus(100)
    print(employee)
    employee.give_bonus(100)
    print(employee)
    print()
    print('wypłata: ', employee.pay_salary())


if __name__ == '__main__':
    main()
