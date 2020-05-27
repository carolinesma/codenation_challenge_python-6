

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee:
    def __init__(self, code, name, salary):
        self.__code = code
        self.__name = name
        self.__salary = salary

    def calc_bonus(self):
        pass

    def get_hours(self):
        pass

    def set_employee(self, code, name, salary):
        self.code = code
        self.__name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__department = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

    def get_departament(self):
        return self.__department


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.departament = Department('sellers', 2)
        self.__sales = 0

    def get_hours(self):
        return 6

    def get_sales(self):
        return self.__sales

    def put_sales(self, sales):
        self.__sales += sales
