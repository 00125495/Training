#class functions that begin with double underscore
#__ special functions
# __init__() - constructors in OOP

class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i
    
    def get_data(self):
        print(f'{self.real}+{self.imag}j')

num1 = ComplexNumber(2,3)
num1.get_data()

num2 = ComplexNumber(5)
num2.attr = 10 # create a new attibute 'attr'

print(num2.real, num2.imag, num2.attr)

#print(num1.attr)
#del num1.imag
#num1.get_data()

del ComplexNumber.get_data
num1.get_data()

c1=ComplexNumber(1,3)
del c1

c2=ComplexNumber(3,5)

#garbage collection
# deleting objects in python removes the name binding

list=[1,2,3,4]

#reference count

#test code 









