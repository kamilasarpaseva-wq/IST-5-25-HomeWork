#dict - словари 

#key - value

student = {
    'name': 'Sam',
    'age': 21,
    True : 'education',
    183: 'height',
    False:True,
    'number': ['0312', '2345']
}

student['number'].append('qwerrt')

#добавление
student.update(kuznetsov=1234)

#изменение
student.update(age=22)

#удаление
del student['name']

#Преобразование пар ключ и значение
for key, value in student.items():
    print(f'{key} - {value}')

print(student)