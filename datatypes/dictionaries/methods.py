"""
Dictionary Methods
"""

# .get

database = { "user":
        {
        "name": "Adekola", 
        "rank":"100", 
        "class":10, 
        "title":"Mr."
        }
}

print(database.get('user'))
print(database.get('user').get('name'))
print(database.get('user').get('rank'))
print(database.get('user').get('class'))
print(database.get('user').get('title'))

print("The user's name is "+database.get('user').get('title')+""+database.get('user').get('name')+", his rank is "+database.get('user').get('rank'))

book1 = {'name':'Cant Hurt Me', 'author':'David Goggins', 'year':'2016', 'publisher':'Random House', 'relatedbooks':[{'name':'12 Rules for life'}, {'name':'Man search for meaning'}]}

"The name of the book is Cant Hurt Me, the book is written by David Goggins. Some of the books similar to this are 12 Rules for life and Man search for meaning"

print("The name of the book is "+book1.get('name')+", the book is written by "+book1.get('author')+". Some of the books similar to this are "+book1.get('relatedbooks')[0].get('name')+" and "+book1.get('relatedbooks')[1].get('name'))

print(book1.items())
print(book1.keys())
book1.pop('year')
print(book1)

book1.popitem()

print(book1)

book1.setdefault('year', '2016')
book1.setdefault('relatedbooks', [{'name':'12 Rules for Life', 'author':'Jordan B. Peterson'}])

print(book1)

book1.update({'isPublic':True, 'isPremium':False})

print(book1)

print(book1.values())