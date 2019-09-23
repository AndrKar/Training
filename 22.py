person = {'name' : 'Jehn', 'age' : 23}
sentence = 'My name is {0} and I am {1} years old.'.format(
    person['name'], person['age'])
print(sentence)

tag = 'hl'
title = 'This is a headline'
sentence = '<{0}><{1}></{0}>'.format(tag, title)
print(sentence)

sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jack', 33)
sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)

sentence = 'My name is {name} and I am {age} years old.'.format(name='Jerry', age=40)
print(sentence)

sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)

for i in range(1, 11):
    print('The value is {:03}'.format(i))

