# dictionaries.py
# based on http://www.youtube.com/watch?v=daefaLgNkw0

student = {1: 'id', 'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

#print(student[1])
#print(student['name'])
#print(student['age'])
#print(student['courses'])

# better use this to not having a KeyError but None if key not found:
def printValues():
    print(student.get(1, 'Not Found'))
    print(student.get('name', 'Not Found'))
    print(student.get('phone', 'Not Found'))
    print(student.get('age', 'Not Found'))
    print(student.get('courses', 'Not Found'))
    print('\n')

printValues()

# change data inside the dictionary:
student['name'] = 'Jane'
student['phone'] = '077072772'
printValues()

# to update more then one value inside of the dictionary:
student.update({'name': 'Jack', 'age': 33, 'phone': '555-5555'})
printValues()

# removing key and value:
del student[1]
print(student)

print('\n')
# removing by pop with returning a value:
age = student.pop('age')
print(student)
print(age)

print('\n')
# looping trough dictionary:
print('Length: {}'.format(len(student)))
print('Keys: {}'.format(student.keys()))
print('Values: {}'.format(student.values()))
print('Items: {}'.format(student.items()))

print('\n')
# looping trough key:
for key in student:
    print(key)

print('\n')
# looping trough items:
for key, value in student.items():
    print(key, value)

print('\n')
# looping trough items more like generator:
for key, value in student.iteritems():
    print(key, value)

print('\n')
# looping trough items using generator:
def studentGenerator():
    for key, value in student.iteritems():
        yield 'Key: "{}", and its value: "{}"'.format(key, value)
        #yield key, value

new_student = studentGenerator()
for ns in new_student:
    print(ns)
