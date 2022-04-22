from funkcje import silnia

# Wygodniej będzie, gdy testowanie nie zostanie przerwane po znalezieniu jednego błędu.
# Biblioteki do testowania, takie jak unittest i pytest, pozwalają napisać wiele testów
# (w formie oddzielnych funkcji), które są uruchamiane niezależnie od siebie.
# Po wykonaniu wszystkich testów dowiemy się które z nich zakończyły się sukcesem, a które porażką.

# Tutaj użyjemy biblioteki pytest.
# Aby użyć tej biblioteki, należy ją zainstalować. Nie jest częścią biblioteki std. Pythona.
# Zainstalować można:
# - w konsoli pisząc pip install pytest
# - w PyCharm poprzez File > Settings > Project ??? > Python Interpreter


# Każda funkcja, której nazwa rozpoczyna się od "test", jest traktowana jak test.
# Funkcja jest przerywana przy pierwszym niespełnionym assercie, ale ine funkcje są uruchamiane mimo błędów.

# Zauważmy, że w tym pliku nigdzie nie uzywamy nazwy pytest.
# Czasami jest to potrzebne, gdy chcemy uzyć technik zaawansowanych,
# ale proste testy można napisać używając wyłącznie assert.

def test_silnia_0():
   assert silnia(0) == 1

def test_silnia_1():
   assert silnia(1) == 1

def test_silnia_5():
   assert silnia(5) == 120

