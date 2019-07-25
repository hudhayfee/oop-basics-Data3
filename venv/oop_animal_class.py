# Class are the basis of OOP - Object Orientated Programming
# They are cookie cutters for objects.***
# From classes you initilaise the individual instances of this class
# Classes hold method
# methods are function that depend on instances of classes
# They can ONLY be called on instances of a class

class Animal():

    def __init__(self): # constructor method runs whenever an instance is created
        self.name = 'Ringo' # property of the animal
        self.species = 'Lizard'
        self.age = 7

    #method for class object - instances
    def sleep(self): # self refers to the instances if gets called upon
# self populates the self with the instance.
        return 'zzzz'

    def eat(self, food):
        return 'nom NOM nom NOM this was some good ' + food

    def potty(self):
        return "... .... "


animal_1 = Animal()# creating 1 instance of class Animal
# print(animal_1)
# print(type(animal_1))

# calling methond on instance of Animal
print(animal_1.sleep())
print(animal_1.eat('meat salad'))
print(animal_1.potty())

# Accessing properties of instances of animal
print(animal_1.name)
print(animal_1.age)