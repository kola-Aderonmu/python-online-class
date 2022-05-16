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

