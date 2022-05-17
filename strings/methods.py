# String methods are functions that operate on strings.

# Examples:
"""
.capitalize()
Returns a copy of the string with its first character capitalized and the rest lowercased.

fruit = 'banana'
fruit.capitalize()
'Banana'

.casefold()
Returns a copy of the string with all the case-based characters converted to lowercase.

fruit = 'Banana'
fruit.casefold()
'banana'

.center(width[, fillchar])
Returns a centered string of length width. Padding is done using the specified fillchar (default is a space).

fruit = 'banana'
fruit.center(10)
'  banana  '
fruit.center(10, '*')
'**banana**'

.find(sub[, start[, end]])
Returns the lowest index in the string where substring sub is found, such that sub is contained in the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Returns -1 if sub is not found.

fruit = 'banana'
fruit.find('na')
2

.split(char)
Returns a list containing all the characters in the string split into sections with the given character
fruit = 'banana'
fruit.split('a')
['b', 'n', 'n']

.join([])
fruit = 'banana'
'*'.join(fruit.split('a'))
'b*n*n'
"""

# Assignment:
# List all the string methods with examples. Your code should be written from line 49.


"""
.upper()
cars = 'lexus'
print(cars.upper())

.isalnum()
cars = 'lexus'
print(cars.isalnum())

.islower()
cars = 'lexus'

.isprintable()
cars.isprintable()

.isupper()
cars.isuper()

.partition()
cars = 'lexus is a nice car'
x = cars.partition('nice')
print(x)

.replace()
cars = 'lexus is a nice car'
cars.replace('lexus', 'Toyota')

.rfind()   show the index of the last occurence
cars = 'lexus is luxury'
cars.rfind('is')

.startwith()
cars = 'lexus'

cars.startwith('L) >>>False
    
  .title()  
txt = 'I am a boy'
txt.title()

.ljust()
x = 'food'
x.ljust(10)


.splitlines() >>split items in a list
x = "we are going to school"
x.splitlines()

.zfill()
x = 'gun'
x.zfill(10) >>it fill the index to 10


"""

