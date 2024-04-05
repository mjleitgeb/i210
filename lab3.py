
grocery = []

item = input('Add an item to the grocery list: ')


while item != '':
    grocery.append(item)
    item = input('Add an item to the grocery list: ')

print('Your grocery list has', len(grocery), 'items:')
print(grocery)
