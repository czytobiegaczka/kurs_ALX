class Employee:
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
           self.kasa = 0


# Tutaj dla wygody testy tej klasy umieszczamy w tym samym pliku, co samą klasę.
# Można też w innym pliku i zaimportować tam klasę.


# Osobne scenariusze powinniśmy testować w osobnych funkcjach.

def test_zero_godzin():
   emp = Employee('Jan', 'Kowalski', 100)
   salary = emp.pay_salary()
   assert salary == 0


def test_jedna_praca():
   emp = Employee('Jan', 'Kowalski', 100)
   emp.register_time(6)
   salary = emp.pay_salary()
   assert salary == 600


def test_dwie_praca():
   emp = Employee('Jan', 'Kowalski', 100)
   emp.register_time(6)
   emp.register_time(4)
   salary = emp.pay_salary()
   assert salary == 1000


def test_nadgodziny():
   emp = Employee('Jan', 'Kowalski', 100)
   emp.register_time(10)
   salary = emp.pay_salary()
   assert salary == 1200


def test_nadgodziny_plus_godzny():
   emp = Employee('Jan', 'Kowalski', 100)
   emp.register_time(10)
   emp.register_time(2)
   emp.register_time(10)
   emp.register_time(6)
   salary = emp.pay_salary()
   assert salary == 3200


def test_resetowanie():
   emp = Employee('Jan', 'Kowalski', 100)
   emp.register_time(10)
   emp.register_time(2)
   salary1 = emp.pay_salary()
   salary2 = emp.pay_salary()
   assert salary2 == 0


