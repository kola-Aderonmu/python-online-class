# list_a = [1, 2, 3]
# list_b = [4, 5, 6]

# list_c = list_a + list_b

# print(list_c)

# list_d = [7, 8, 9]

# list_d.extend(list_a)
# list_d.extend(list_b)

# print(list_d)

# print(list_d[:4])

# Assignment:

"""
1. Write all the methods available in the list class with examples
"""
# 1. append()

# cars = ['lexus', 'toyota', 'hyundia', 'mazda', 'volkwagen',]
# print(cars)
# print(cars.append('g-wagon')) <<<<######check this#######


# # 2. .clear()
# Vin = ['lexus', 'toyota', 'hyundia', 'mazda', 'volkwagen', ]
# vin.clear()


# # 3. .copy()
# cars = ['lexus', 'toyota', 'hyundia', 'mazda', 'volkwagen', ]
# x = cars.copy()
# print(x)

# 4. .count()
cars = ['lexus', 'toyota', 'hyundia', 'mazda', 'volkwagen', ]
print(cars.count('toyota'))

# 5. .extend()
# cars = ['lexus', 'toyota', 'hyundia', 'mazda',]
# users = ['kola', 'john', 'ahmed','zarah']

# cars.extend(users) #<<<joins all the list together
# print(cars)

# # 6. .index()
# cars = ['lexus', 'toyota', 'hyundia', 'mazda', 'volkwagen', ]
# print(cars.index('hyundia')) #<<<<<gives me the index numb

# 7. .insert()
cars = ['lexus', 'toyota', 'hyundia', 'mazda', 'volkwagen', ]
cars.insert(2,'jeep') #<<<insert n item in any part of the list
print(cars)


# 8. .pop()
cars = ['lexus', 'toyota', 'hyundia', 'mazda', 'volkwagen', ]
cars.pop() #<<<<removes the last item on the list
print(cars)

# 9. .remove()
cars = ['lexus', 'toyota', 'hyundia', 'mazda', 'volkwagen', ]
cars.remove('toyota')  #<<<<removes a specefix items on the list
print(cars)

# 10. .reverse()
cars = ['lexus', 'toyota', 'hyundia', 'mazda', 'volkwagen', ]
cars.reverse() #<<<reverses the item LIFO
print(cars)
print(cars[: -1])#<<<last item
print(cars[: -2])#<<last two items
print(cars[: -3])#<<last three items
    

# 11. .sort()

cars = ['lexus', 'toyota', 'hyundia', 'mazda', 'volkwagen', ]
print(cars.sort())  #<<<<what does this do again?
