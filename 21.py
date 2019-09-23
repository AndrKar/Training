li = [9, 2, 5, 4, 6, 7, 8, 1, 3]
s_li = sorted(li, reverse=False)
print(li)
print(s_li)
li.sort(reverse=True)
print(li)

tup = (9, 2, 5, 4, 6, 7, 8, 1, 3)
s_tup = sorted(tup)
print(tup)
print(s_tup)
from operator import attrgetter


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 7000)
e2 = Employee('John', 43, 9000)
e3 = Employee('Sarah', 29, 8000)

employees = [e1, e2, e3]
print(employees)
s_employees = sorted(employees, key=lambda e: e.name, reverse=True)
s_employees = sorted(employees, key=attrgetter('age'), reverse=True)
print(s_employees)
