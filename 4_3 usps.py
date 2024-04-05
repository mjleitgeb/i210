types_of_mail = {
    "postcard": 0.35,
    "letter": 0.55,
    "small package" : 7.5,
    "medium package" : 16.0,
    "large package" : 40.23
    }

distance = {
    "local" : 1,
    "in-state" : 1.5,
    "out-of-state" : 1.75,
    "international" : 2.25
    }

speed = {
    "standard" : 1,
    "priority" : 1.75,
    "first-class" : 3
    }

print("Welcome to the Post Office!")
typ = input("What are you shipping today? (postcard, letter, small package, medium package, large package)")
length = input("How far will it be shipped? (local, in-state, out-of-state, international)")
input_speed = input("How fast would you like that shipped (standard, priority, first-class)")

total = float(types_of_mail[typ] * distance[length] * speed[input_speed])

print("Alrighty! To ship a", typ, "to an adress that is", length, "with", input_speed, "shipping, the total cost will be $" +  '{:.2f}'.format(total))
