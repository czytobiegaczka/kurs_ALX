'''
ogólne definicje służące do obsługi plikó emps.csv
'''


class Employee:
    '''
    obiekt tej klasy reprezentuje jednego pracownika
    '''
    def __init__(self, employee_id, first_name, last_name, job_title, salary, hire_date, department_name, address,
                 postal_code, city, country):

        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.salary = salary
        self.hire_date = hire_date
        self.department_name = department_name
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.country = country

    def __str__(self):
        return f'Employee {self.employee_id}: {self.first_name} {self.last_name} ({self.job_title}) {self.salary} USD'


def wczytaj_plik(sciezka):
    '''
    wczytanie danych z pliku .csv
    :param sciezka: ścieżka do pliku
    :return: lista obiektów Employee
    '''
    with open(sciezka, mode='r', encoding='utf-8') as plik:
        plik.readline()
        lista = []
        for linia in plik:
            t = linia.split(';')
            emp = Employee(int(t[0]), t[1], t[2], t[3], float(t[4]), t[5], t[6], t[7], t[8], t[9], t[10])
            lista.append(emp)
    return lista
