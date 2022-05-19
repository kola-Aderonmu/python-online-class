# fruit1 = {'name': 'Mango', 'color': 'orange',
#           'taste': 'sweet', 'status': 'available'}

# print(fruit1['name'])

# fruit1['price'] = 1500

# print(fruit1)

# Assignment:

"""
1. Write all the methods available in the dictionary class with examples
2. Create a dictionary that holds information about a product with the following properties:
    name, color, price, hasDiscount, stores, availability.
    Please note that stores here means the stores where the product can be purchased from.
"""
####################################################
#1. .clear
cars = {'name': 'Lexus', 'model' : 'IS 460', 'color' : 'dark brown'
    
}
# print(cars)

# print(cars.clear())  << returns a None

#2. .copy
# cars = {'name': 'Lexus', 'model': 'IS 460', 'color': 'dark brown'

#         }
# x = cars.copy()

# print(x)  <<<<return a copy of the ItemsView

#3. get
# cars = {'name': 'Lexus', 'model': 'IS 460', 'color': 'dark brown'

#         }
# print(cars.get('model'))
# print(cars.get('engine'))  <<< returns a None

#4. items
# cars = {'name': 'Lexus', 'model': 'IS 460', 'color': 'dark brown'

#         }
# print(cars.items())  <<returns a set of items in the dict

#5. keys
# cars = {'name': 'Lexus', 'model': 'IS 460', 'color': 'dark brown'

#         }
# print(cars.keys()) <<<<<return a list of keys 

####======NOTICE=======##############
#6. pop
# cars = {'name': 'Lexus', 'model': 'IS 460', 'color': 'dark brown'

#         }
# print(cars.pop()) << <<TypeError: pop expected at least 1 argument, got 0

#7. popitem
# cars = {'name': 'Lexus', 'model': 'IS 460', 'color': 'dark brown'

#         }
# print(cars.popitem()) <<<<remove the last item(both key and value) LIFO method
# print(cars)

#8.setdefault
# cars = {'name': 'Lexus', 'model': 'IS 460', 'color': 'dark brown'
# }
# v = cars.setdefault('color', 'Grey')
# print(v)            <<<it adds key and value to the list 
# print(cars)

#9. update
# cars = {'name': 'Lexus', 'model': 'IS 460', 'color': 'dark brown'}
# cars.update({'engine':'V6', 'Fuel':'PMS'})
# print(cars) <<<this will update the dict

#10. values
cars = {'name': 'Lexus', 'model': 'IS 460', 'color': 'dark brown'}
print(cars.values())  #<<<return back the values to the Keys.


