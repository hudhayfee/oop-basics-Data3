from oop_animal_class import Animal

# def sleep():
#     return 'Snoring'

# init. a Animal, then call method sleep
# print(Animal().sleep())
animal_instance_ringo = Animal('Ringo', 10)
animal_instance_hugo = Animal('Hugo', 2)
animal_instance_baltazar = Animal('Baltazar', 4)

print(animal_instance_hugo)
print(animal_instance_hugo.name)
animal_instance_hugo.name = 'filipe'
print(animal_instance_hugo.name)

print('//////////')
print(animal_instance_ringo.name)
print(animal_instance_baltazar.name)


animal_instance_hugo.eat('chicken')
print(animal_instance_hugo.number_of_animal_eaten)
animal_instance_hugo.eat('salad')
animal_instance_hugo.eat('taco')
print(animal_instance_hugo.number_of_animal_eaten)
