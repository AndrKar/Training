student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student['courses'][0])
student[0] = 'startline'
print(student[0])
for key, value in student.items():
    print(key, value)
print(student)
print(student.get('phone', 'Not found'))
print(student)
del student[0]
print(student.popitem())
student.pop('name')
print(student)
print(student.items())
for key in student:
    print(key, student[key], sep='---')
