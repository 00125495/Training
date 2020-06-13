
pow2 = []
for x in range(10):
    pow2.append(2**x)
    

print(pow2)

# list comprehension

pow2=[2**x for x in range(10) if x>5]

