# while loop
"""
while test_expression:
    body of while
"""
# python interprets any non-zero value as true
# None and 0 are intrepreted as False 

n= int(input("Enter n: "))
sum=0; i=1

while i <= n:
    sum = sum + i
    i= i+1

print("sum is ", sum)

