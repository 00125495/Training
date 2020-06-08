
def outer_function():
    global a
    a=20 # local name space of outer function
    def inner_function():
        global a
        a=30 #local NS of inner function
        print('a =', a)
    inner_function()
    print('a =', a)

a=10 # Global Name Space
outer_function()
print('a =', a)

# name, name spaces, variable scope
# flow controls -- if else, for, while, pass, break
# continue

