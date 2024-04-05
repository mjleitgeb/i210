def check_age(age):
   if int(age) < 0:
       raise ValueError('Invalid age')
   return int(age)
ages = []
user_input = input("Enter an age: ")
while user_input:
   try:
       age = check_age(user_input)
       ages.append(age)
       print("Age added.")
   except ValueError as e:
       print(e)
       print("You'll need to try again.")
   user_input = input("Enter an age: ")
