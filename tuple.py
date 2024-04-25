from collections import namedtuple

Point = namedtuple('Letter', ['d', 'g'])
p1 = Point(1, 2)
print(p1.d, p1.g)


Guy = namedtuple('Guy', ['name', 'age', 'number_of_girlfriends'])
ch = Guy('Dodik', 23, '</>')
print(ch.name, ch.age, ch.number_of_girlfriends)


Car = namedtuple('Car', ['make', 'model', 'year'])
car = Car('BMW', 'Alpina B5 V8 Switch Tronic E60', 2006)
print(car.make, car.model, car.year)


Rectangle = namedtuple('Rectangle', ['width', 'height'])
rect = Rectangle(10, 20)
print(rect.width * rect.height)


Patient = namedtuple('Patient', ['name', 'age', 'gender', 'blood_type'])
patient = Patient('Sherali', 35, 'male', '1')
print(patient.name, patient.age, patient.gender, patient.blood_type)
