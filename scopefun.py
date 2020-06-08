def my_func():
    global x
    x=10 # Local NameSpace
    print("Value Inside function:", x)

x=20 # Global Namespace
my_func()
print("vlaue outside function:", x)