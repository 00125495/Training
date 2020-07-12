#self keyword is used to represent an instance 
#of the given class

class Point(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def distance(self):
        """Find distnace from origin"""
        return (self.x**2+self.y**2)**0.5

p1 = Point(6,8)
print(p1.distance())