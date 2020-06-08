x = 5 # Global Namespace

def foo():
    global x
    x = 10 # Local Namespace
    print("Local x:", x)

foo()
print("Global x:", x)

