#nonlocal - nested functions 
# neither in local nor the global scope

x="global" # Global Namespace

def outer():
    x = "local" # Local Namespace to outer()

    def inner():
        global x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()