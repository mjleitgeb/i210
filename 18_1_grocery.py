file = open('messy_grocery_list.txt', 'r')
content = file.read()
file.close()

new_list = [item.strip() for item in content.split(',')]

print(new_list)

