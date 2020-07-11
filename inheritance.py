#way of creating anew class from using of an existing class
#without modifying it

#newly formed class is a derived class ( child class)
#existing class is a base class ( parent class)

#can we able to access parent class attributes
#after modifying at child class??

class Bird:
    def __init__(self):
        print("Bird is ready")
    
    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim Faster")

#child class

class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        super().whoisThis()
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()