class Animal():

    def __init__(self, name, age, alive = True):
        self.name = name
        self.age = age
        self.alive = alive

    def sleep(self):
        return 'zzzz'

    def eat(self, food):
        return 'nom NOM nom on' + food

    def potty(self):
        return "... ...."

    def shout_own_name(self):
        return 'MY NAME IS ' + self.name.upper()

    def amend_name(self, new_name):
        self.name = new_name

animal_1 = Animal('Bronco', 24, 'b')
print(animal_1.alive)
print(animal_1.name)
animal_1.name = 'Teresa'
print(animal_1.name)
