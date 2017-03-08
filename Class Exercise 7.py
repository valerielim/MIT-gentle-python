# Valerie Lim
# Date started: 6 March 2017
# Completed: 9 March 2017 (!!!!!)
# Title: Class Exercise 7

# I HATED THIS SHIT

# Ex 4.4

class Shoe:
    def __init__(self, colour, brand):
        self.colour = colour
        self.brand = brand

    def __str__(self):
        return str(self.colour)+"-coloured "+str(self.brand)

    def mud(self):
        self.colour = "brown"
        print "Oh no, I stepped into mud!"
        print "Now my shoes are", str(self)

class schoolShoe(Shoe):
    def __init__(self, colour, highorlow, liningColour):
        Shoe.__init__(self, "White", "Bata")
        self.top = highorlow
        self.lining = liningColour

    def __str__(self):
        return str(self.colour)+"-coloured "+str(self.top)+" "+str(self.brand)+" shoe with "+str(self.lining)+"-coloured trimmings."

    def wash(self):
        self.colour = "white"
        print "---------Washed!"
        print "My shoes are back to being a", str(self)
    
# Test cases
s1 = Shoe("pink", "ballet flats")
s2 = schoolShoe("white", "low-cut", "black")        

print "My first pair of shoes are", s1
s1.mud()
print "My second pair of shoes are", s2
s2.mud()
s2.wash()
print
print "lol I had fun messing with this :-)"
print 



#### Ex 4.5
class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation
    def __str__(self):
        return self.name
    def get_description(self):
        return "No description"
    def execute(self):
        print self.incantation
class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, "Accio", "Summoning Charm")
    def __str__(self):
        return "This charm summons an object to the caster, potentially over a significant distance."

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, "Confundo", "Confundus Charm")
    def get_description(self):
        return "Causes the victim to become confused and befuddled."

def study_spell(spell):
    print spell
    
spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())


# 1.
# Parent class: Spell
# Chidl class: Accio, Confundo

# 2.
# Accio
# Summoning Charm
# Confundus Charm

# 3.
# The method from the instance of Confundo.
# This is called (not the parent class "Spell"-'s version)
# because the function study_spell calls the Confundo instance first

# 4.
#    def __str__(self):
#        return "This charm summons an object to the caster, potentially over a significant distance."
# Note: Solution has been added into code above :-)




##### Ex 4.6

class Address:
    def __init__(self, street_name, num):
        self.street = street_name
        self.number = num
    
class CampusAddress(Address):
    def __init__(self, office_number):
        Address.__init__(self, "Massachusetts Ave", 77)
        self.office_number = office_number

    def __str__(self):
        return self.street+" "+str(self.number)+" "+str(self.office_number)

# Testcases
Sarina_addr = CampusAddress("32-G904")
print "The full address is", Sarina_addr
print "The office number is", Sarina_addr.office_number
print "The street name is", Sarina_addr.street
print "The street number is", Sarina_addr.number
