firstname = "John"
lastname = "Doe"

name = firstname + " " + lastname

print(name)

print(firstname[0:2])

print(firstname[3])
print(firstname[-1])
print(firstname[-2])

print(lastname[1:3])


names = 'Adekola*Hashim*Kabirat*Idris*Micheal'
x = names.split('*')
print(x)
friends = ", ".join(x)

names = 'Adekola*Hashim*Kabirat*Idris*Micheal'
friends = names.replace("*", ", ")
print(friends)

print(friends)

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
jumped = alphabets[::3]
print(jumped)

backwards = alphabets[::-1]
print(backwards)

backwards = alphabets[::-3]
print(backwards)

# Assignment
# Write 10 string examples
# print out each string example written above
# use string operations to concatenante all the strings in one gaint string
# create one variable for each to hold all the strings above backwards

#################################
'A', 'boy', 'is', 'going,' 'to', 'be', 'late', 'by', '10am', 'today'

###############################################################
print('A')
print('boy')
print('is')
print('going')
print('to')
print('be')
print('late')
print('by')
print('10am')
print('today')
####################################################concatentate
sentence = ('A '  + 'boy ' + 'is ' + 'going ' + 'to ' + 'be ' + 'late ' + 'by ' + '10am ' + 'today ')
print(sentence)

###################################################################hold strings backwards
test = sentence[: : -1]
print(test)

#############################reversed using join
test1 = sentence
revs = "".join(reversed(test1))
print(revs)

