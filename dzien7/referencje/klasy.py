class Osoba:
   def __init__(self, imie, nazwisko, wiek):
       self.imie = imie
       self.nazwisko = nazwisko
       self.wiek = wiek

   def przedstaw_sie(self):
       print(f'Jestem Osobą. Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek} lat.')

   def pelnoletnia(self):
       return self.wiek >= 18

   def __str__(self):
       return f'{self.imie} {self.nazwisko} ({self.wiek} lat)'

   def __repr__(self):
       return f'Osoba({repr(self.imie)}, {repr(self.nazwisko)}, {repr(self.wiek)})'


class BrakSrodkow(Exception):
   def __init__(self, numer, kwota, saldo):
       super().__init__(f'Brak środków na koncie nr {numer}. Próbowano wypłacić {kwota}, a na koncie jest {saldo}')
       self.numer = numer
       self.kwota = kwota
       self.saldo = saldo


class Konto:
   def __init__(self, numer, wlasciciel, saldo=0):
       if saldo < 0:
           raise ValueError('ujemne saldo')
       self._numer = numer
       self._wlasciciel = wlasciciel
       self._saldo = saldo

   def __str__(self):
       return f'Konto nr {self._numer}, saldo = {self._saldo}, wł. {self._wlasciciel}'

   def wplata(self, kwota):
       if kwota <= 0:
           raise ValueError('niedodatnia kwota we wplata')
       self._saldo += kwota

   def wyplata(self, kwota):
       if kwota <= 0:
           raise ValueError('niedodatnia kwota w wyplata')
       if kwota > self._saldo:
           raise BrakSrodkow(self._numer, kwota, self._saldo)
       self._saldo -= kwota

