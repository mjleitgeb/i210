# make the imports you need here
from visit import *
from people import *
import data_handling as dh

class Animal():
    #Animals admitted to the shelter
    __adopted_list = []
    __all_animals_list = []

    @staticmethod
    def tracking():
        print("Total animals to be adopted: " + str(len(Animal.__all_animals_list) - len(Animal.__adopted_list)) + "\n")

    @staticmethod
    def get_all_animals():
        return Animal.__all_animals_list

    @staticmethod
    def get_adopted_animals():
        return Animal.__adopted_list

    @staticmethod
    def get_available_animals():
        available_list = []
        for animal in Animal.__all_animals_list:
            if not animal.__adopted:
                available_list.append(animal)              
                
        return available_list

    # Which animal kind is the most popular (i.e. gets adopted the most)?
    # Loop through all adoptions, adding animal kinds to a single master list
    # Initialize variables to hold the most popular animal and the number of times it appears
      
    @staticmethod
    def report_most_popular():
        most_popular = {}
        for animal in Animal.__adopted_list:
            if animal.get_kind() not in most_popular:
                most_popular[animal.get_kind()] = 1
            elif animal.get_kind() in most_popular:
                most_popular[animal.get_kind()] += 1

        pop_count = -1
        pop_animal = None
        for kind in most_popular:
            if most_popular[kind] > pop_count:
                pop_count = most_popular[kind]
                pop_animal = kind
                
        return 'Most popular kind: ' + pop_animal
      
    # Give a report of all of the animals of a given kind and lower than a certain age at the shelter that have not been adopted yet. 
    @staticmethod
    def report_not_adopted(kind, age):
        not_adopted = []
        for animal in Animal.get_available_animals():
            if animal.get_kind() == kind and animal.get_age() <= age:
                not_adopted.append((animal.get_name(), animal.get_kind(), animal.get_age()))
                dh.table_print(['Name', 'Kind', 'Age'], not_adopted, [10, 10, 10])
            else:
                print('There are no animals that fit these criteria')
                
        
    
    def __init__(self, name, age, kind, color, vaccinated = False):
        self.__name = name
        self.__age = age
        self.__kind = kind
        self.__color = color
        self.__vaccinated = vaccinated
        self.__adopted = False      
        Animal.__all_animals_list.append(self)

    def __str__(self):
        if not self.__adopted:
            reply = "A "
            reply += self.__color + " "
            reply += self.__kind + " named "
            reply += self.__name + ", who is "
            reply += str(self.__age) + " years old "
            reply += "is up for adoption.\n"
            reply += self.__name + " is "
            if not self.__vaccinated:
                reply += "not "
            reply += "vaccinated.\n"
        else:
            reply = self.__name + " has already been adopted.\n"
        return reply

    # compare two animal objects based on name, kind, age, and color
    def __eq__(self, other):
        if self.__name == other.__name and self.__kind == other.__kind and self.__age == other.__age and self.__color == other.__color:
            return True
        else:
            return False
            
        

    #getters and setters
    
    def adopt(self):
        print(self.__name + " got adopted.")
        Animal.__adopted_list.append(self)
        self.__adopted = True

    def is_adopted(self):
        return self.__adopted

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_age(self):
        return self.__age
    
    def get_kind(self):
        return self.__kind
    
    def vaccinate(self):
        self.__vaccinated = True

    def is_vaccinated(self):
        return self.__vaccinated

    

if __name__ == "__main__":
    
    animal1 = Animal('Harry', 10, 'dog', 'black')
    animal2 = Animal('Edward', 3, 'cat', 'orange')
    animal3 = Animal('Bob', 2, 'bunny', 'white')
    animal4 = Animal('Molly', 9, 'dog', 'brown')
    animal5 = Animal('Josh', 2, 'chicken', 'white')
    animal6 = Animal('Isaiah', 13, 'dolphin', 'gray')
    animal7 = Animal('Remy', 4, 'dog', 'white')
    animal8 = Animal('Max', 16, 'dog', 'brown')
    animal9 = Animal('Tom', 1, 'cat', 'red')
    animal10 = Animal('Eevee', 2, 'dog', 'brown')
    

    animal1.adopt()
    animal2.adopt()
    animal3.adopt()
    animal4.adopt()
    animal5.adopt()
    animal6.adopt()
    animal7.adopt()
    animal8.adopt()
    animal9.adopt()

    print(Animal.report_most_popular())
    

    user_kind = input('Enter a kind of animal')
    user_age = int(input('Enter in the age of the animal'))

    Animal.report_not_adopted(user_kind, user_age)

    print(Animal.__eq__(animal1, animal2))
    #create a test code here
    
