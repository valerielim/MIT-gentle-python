# Valerie Lim
# Title: Class Exercise 4
# Date: 7 March 2017

#### SAMPLE

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


##### Ex 4.4
class Cup:
    def __init__(self, volume, colour):
        self.volume = volume        # in ml
        self.colour = colour

    def pourwater(self):
        water = input("How much water would you like to pour in?")
        if water > self.volume:
            print "Oh no! The cup is overflowing!!"
        print "The cup is now", str(float(water/self.volume *100))+"% full"

    def description(self):
        print "The cup is", str(self.volume)+"ml", "big and", self.colour, "in colour."

class tumbler(Cup):
    def __init__(self, waterproof, cost):
        Cup.__init__(self, 1000, colour)
        self.waterproof = waterproof    # yes or no
        self.cost = cost
        
class bottle(Cup):
    def __init__(self, material, age):
        Cup.__init__(self, 600, "transparent")
        self.material = material
        self.age = age      # days old cos gross mah

class jug(Cup):
    def __init__(self, owner, location):
        self.owner = owner
        self.location = location    # eg kept in kitchen

##### Test cases
starbucks = Cup(500, "white")



##### Ex 4.5

# 1. Parent class is Spell. Child classes are the instances of spells - Accio and Confundo.
# 2. spell = Acccio() prints nothing
#    spell.execute() prints the self-incantation for Accio, aka "Accio"
#    study_spell(spell) should print an error or the location of the Spell class
#    study_spell(Confundo()) will print "Confundo"
