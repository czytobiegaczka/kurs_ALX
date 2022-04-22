from electriccar import ElectricCar

car = ElectricCar(100)


def test_przejazd70():
    assert car.drive(70) == 70


def test_przejazd50():
    assert car.drive(50) == 30


def test_przejazd_kolejne50():
    assert car.drive(50) == 0


def test_przejazd_50_po_ladowaniu():
    car.charge()
    assert car.drive(50) == 50

#### Tutaj kilka testów pytest ####

def test_drive1():
   car = ElectricCar(100)
   km = car.drive(70)
   assert km == 70

def test_drive_do_konca():
   car = ElectricCar(100)
   km = car.drive(70)
   km = car.drive(50)
   assert km == 30

def test_wyladowanie_do_zera():
   car = ElectricCar(100)
   km = car.drive(150)
   km = car.drive(50)
   assert km == 0

def test_charge1():
   car = ElectricCar(200)
   car.drive(150)
   car.drive(100)
   car.charge()
   km = car.drive(150)
   assert km == 150

def test_charge2():
   car = ElectricCar(500)
   car.drive(300)
   car.charge()
   km = car.drive(600)
   assert km == 500




