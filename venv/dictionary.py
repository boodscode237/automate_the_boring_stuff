myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
myCat['size']
phrase = 'My cat has ' + myCat['color'] + ' fur.'
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon)
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)
eggsKeys = list(eggs.keys())
eggsValues = list(eggs.values())
eggsItem = list(eggs.items())

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k,v in eggs.items():
    print(k,v)

for i in eggs.items():
    print(i)