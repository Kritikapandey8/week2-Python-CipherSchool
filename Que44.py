# fromkeys
d = dict.fromkeys(['name','age'], 'unknown')
print(d)

# get method(useful)
d = {'name' : 'Kritika', 'age' :  'unknown'}
print(d['name'])
print(d.get('name')) 

if 'name' in d:
    print('present')
else:
    print('not present')

if d.get('names'):
    print('present')
else:
    print('not present')

d.clear()
print(d)
d1 = d.copy()
# print(d1.popitem())
# print(d)
print(d1 is d)