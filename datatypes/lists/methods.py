"""
Methods available in the list class
___________________________________

"""

fruits = ['Apples', 'Mangoes', 'Oranges']

print(fruits)

fruits.append('Cashews')

print(fruits)

fruits.clear()

print(fruits)

x = fruits.copy()

print(x)

fruits = ['Apples', 'Mangoes', 'Oranges']

print(fruits.count('Apples'))

fruits.append('Apples')

print(fruits.count('Apples'))

people = ['Ahmad', 'Saad', 'Micheal', 'John']

students = ['Zara', 'Osofia', 'Hadiza']

print(people)
print(students)

students.extend(people)

print(students)

students.extend('cake')

print(students)

print(students.index('Ahmad'))

students.insert(1, 'Jordan')

print(students)

students.pop(8)
students.pop(8)
students.pop(8)
students.pop(8)

print(students)

students.remove('Ahmad')

print(students)

students.reverse()

print(students)

students.sort()
print(students)