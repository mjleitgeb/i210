# make the imports you need here
from animal import *
from people import *
import data_handling as dh

class Visit:

    # define your class attributes here 
    __visit_list_num = 1
    # Creates a visitlist list object. pay attention to attributes you need.
    def __init__(self, person):
        self.__person = person
        Visit.__visit_list_num += 1
        self.__visit_list = []
        self.__id = Visit.__visit_list_num
        self.__completed = False
        

    # format a visitlist object for printing visit lists. Make sure all important
    # attributes are printed and properly formatted 
    def __str__(self):
        reply += self.__id + '\n'
        reply += self.__person + '\n'
        for visit in self.__visit_list:
            reply += 'Name: ' + animal.get_name() + '\n'
            reply += 'Color: ' + animal.get_color() + '\n'
            reply += 'Age: ' + animal.get_age() + '\n'
            reply += 'Kind: ' + animal.get_kind() + '\n'
            reply += 'Vaccinated: ' + animal.is_vaccinated() + '\n'
        return reply

    # Write a method that can display all animals in a visitlist.
    # When a person wants to make a visit, call this method to
    # print all the animals in their visitlist, and also print the customer’s
    # name and the visitlist number.
    def print_visit_list(self):
        attributes = []
        for animal in self.__visit_list:
            attributes.append((animal.get_name(), animal.get_age(), animal.get_kind()))          
        dh.table_print(['Name', 'Age', 'Kind'], attributes, [10, 10, 10])
        

    # Allows people to add new animal objects to their visitlist, as long as:
    #  - The object we’re trying to add really is a Animal
    #  - The exact same animal isn’t already in the list
    #  - The animals has not been adopted yet
    #  - The person has not adopted an animal yet
    
    def add_animal(self, animal):
        if isinstance(animal, Animal):
            if animal not in self.__visit_list:
                if not animal.is_adopted():
                    if self.__completed == False:
                        self.__visit_list.append(animal)
                        print('animal added')
        

    # Write a method that allows people to delete an existing animal object from the visitlist.
    #  - The animal must be in the list to be removed
    def remove_animal(self, animal):
        if animal in self.__visit_list:
            self.__visit_list.remove(animal)
            print('animal removed')
        
    
    # Write a method to to allow a person to make an adoption of an animal object
    # (setting the animal as adopted, and setting the visitlist as completed
    # adoption), as long as:
    #  - The adoption has not been completed yet for that visitlist
    #  - The animal is in the visitlist
    #  - The animal has not been adopted yet

    def adopting(self, animal):
        if animal.is_adopted() == False:
            if self.__completed == False:
                if animal in self.__visit_list:
                    animal.adopt()
                    self.__completed = True
                    print('animal adopted')
                
        

    # define getters and setters as needed here

    def get_person():
        return self.__person

    def get_id():
        return self.__id

    def is_completed():
        return self.__completed

    def completed():
        self.__completed = True
                    



if __name__ == "__main__":
    
    # create 4 Person objects
    person1 = Person("Taylor", "trolls@aol.com")
    person2 = Person("Ray", "bvree@yahoo.com")
    person3 = Person("Carmen", "carlow@live.com")
    person4 = Person("Lena", "lekali@gmail.com")
    
    # create 5 Adoption objects
    visitlist1 = Visit(person1)
    visitlist2 = Visit(person2)
    visitlist3 = Visit(person3)
    visitlist4 = Visit(person4)
    visitlist5 = Visit(person2)

    # create 3 animal objects
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

    # test add_animal()
    visitlist1.add_animal(animal1)
    visitlist2.add_animal(animal2)
    visitlist3.add_animal(animal3)
    visitlist4.add_animal(animal4)
    visitlist5.add_animal(animal5)
    visitlist1.add_animal(animal6)
    visitlist2.add_animal(animal7)
    visitlist3.add_animal(animal8)
    visitlist4.add_animal(animal9)
    visitlist5.add_animal(animal10)
    
    

    # test remove_animal()
    
    
    # test print_visit_list()
    visitlist1.print_visit_list()
    visitlist2.print_visit_list()
    visitlist3.print_visit_list()
    visitlist4.print_visit_list()
    visitlist5.print_visit_list()
    
    # test adopting(animal)
    visitlist1.adopting(animal1)
    visitlist2.adopting(animal2)
    visitlist3.adopting(animal3)
    visitlist4.adopting(animal4)
    visitlist5.adopting(animal5)

    
    


