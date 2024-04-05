##animals = []
##
##animals.append('dog')
##animals.append('cat')
##animals.append('fish')
##animals.append('turtle')
##animals.append('red panda')
##
##print('I have', len(animals), 'animals.')
##
##pandas = animals.count('red panda')
##
##print('Exactly', pandas, 'of the animals are red pandas.')
##
##print('The last animal in my list is a', animals[-1])
##
##print(animals)

## 3.3 Movie night

# Meet the dad. He owns several favorite movies. Some he likes so much he has multiple copies.
dad_movies = ["Die Hard", "Jaws", "Alien", "Princess Mononoke", "Die Hard", "Alien", "Jurassic World"]

# Meet the kid. He also owns some favorite movies.
kid_movies = ["Jurassic World", "Princess Mononoke", "Dragonball Z", "Kung Fu Panda", "How to Train Your Dragon"]

#1 Make each movie list only contain one copy of each movie by transforming them into sets
dad_set = set(dad_movies)
kid_set = set(kid_movies)
print('The dad likes:', dad_set)
print('The kid likes:', kid_set)

#2 What movies do the dad and kid have to select from? (List all movies in either list)
all_movies = dad_set.union(kid_set)
print('All movie choices:', all_movies)

#3 What movies are liked by either the dad or the kid, but not both?
specific_movies = dad_set.symmetric_difference(kid_set)
print('Movies only one of them like:', specific_movies)

#4 What movies does only the dad like?
only_dad = dad_set.difference(kid_set)
print('Movies only the dad likes:', only_dad)

#5 What movies do both the dad and the kid like?
both = dad_set.intersection(kid_set)
print('Movies they both like:' , both)

# (Still have two choices for movie night! Hope they can agree on one. ;-)
