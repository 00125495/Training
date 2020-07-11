#Object - Attributes and behaviour
# Parrot 
# Attributes - name, age, color
# Behavior - Singing , dancing 

# focus on creating resuasable code

# class - blueprint of object, sketch
# sketch of parrort contains all the details about name, color
#size
#from class, we construct instances 

class Parrot:

    #class attributes
    species = "bird"

    #instance attributes #intializer method
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantaite the parrot class

blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)


# access the class attributes
 
print("Blu is a {}".format(Parrot.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes

print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))
