from funkcje import silnia

# W tej wersji zamiast if użyjemy instrukcji assert.
# assert działa tak:
# - gdy warunek jest prawdziwy, to nie robi nic, program idzie dalej
# - gdy warunek jest fałszywy, to assert wyrzuca wyjątek AssertionError i przerywa działanie programu
# Poniższy program testujący zostanie przerwany dla pierwszego błędu

assert silnia(1) == 1
assert silnia(5) == 120

print('Wszystko OK')
