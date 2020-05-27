

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee:
    def __init__(self, code, name, salary, department):
        self.__code = code
        self.__name = name
        self.__salary = salary
        self.department = department
        self.hours = 8

    def calc_bonus(self):
        pass

    def get_hours(self):
        return self.hours

    def get_salary(self):
        return self.__salary

    def set_employee(self, code, name, salary):
        self.code = code
        self.__name = name
        self.salary = salary

    def set_department(self, department):
        self.__department = department

    def get_department(self):
        return self.department.name


class Manager(Employee):
    def __init__(self, code, name, salary):
        department = Department('managers', 1)
        super().__init__(code, name, salary, department)

    def calc_bonus(self):
        return super().get_salary() * 0.15


class Seller(Employee):
    def __init__(self, code, name, salary):
        department = Department('sellers', 2)
        super().__init__(code, name, salary, department)
        self.__sales = 0

    def get_sales(self):
        return self.__sales

    def put_sales(self, sales):
        self.__sales += sales

    def calc_bonus(self):
        return self.__sales * 0.15
