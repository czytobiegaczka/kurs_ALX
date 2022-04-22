class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.suma_godzin = 0
        self.suma_nadgodzin = 0

    def register_time(self, godziny):
        if godziny > 8:
            self.suma_godzin += 8
            self.suma_nadgodzin += (godziny - 8)
        else:
            self.suma_godzin += godziny

    def pay_salary(self):
        wyplata = self.suma_godzin * self.stawka + self.suma_nadgodzin * 2 * self.stawka
        self.suma_godzin = 0
        self.suma_nadgodzin = 0
        return wyplata


# W tej wersji obsługuję bonusy w podklasie nie zakładając żadnej konkretnej implementacji w nadklasie.
# Nie korzystam ze zmiennych zdefiniowanych w nadklasie.
# Wywołuję super().pay_salary() i do wyniku dodaję bonus.
class PremiumEmployee(Employee):
    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.bonusy = 0

    def give_bonus(self, bonus):
        self.bonusy += bonus

    def pay_salary(self):
        wynik = super().pay_salary() + self.bonusy
        self.bonusy = 0
        return wynik


emp = PremiumEmployee('Jan', 'Kowalski', 100)
emp.register_time(5)
emp.register_time(4)
emp.give_bonus(400)

print(emp.pay_salary())  # 1300
print(emp.pay_salary())  # 0

emp.register_time(10)
emp.give_bonus(200)
print(emp.pay_salary())  # 1400
