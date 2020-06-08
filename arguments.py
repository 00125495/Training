
def greet(name,msg="Good night!" ):
    """
    This function greets you
    """
    print("Hello", name+','+ msg)

#greet("Ramana") # positional arguments 
#msg="Good night!"  default arguments 

#greet(name="Ramana", msg="How do you do?")
# keyword arguments 

greet(msg="How do you do?", name="Chandra")

#greet("Ramana", msg="how do you od?")
#1 positional arg, 1 keyword argument 

greet(name="Ramana", "how do you do?")





