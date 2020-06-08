
#Used to iterate over a sequence ( list, tuple, string)
#traversal

"""
for val in sequence:
    body of for

"""
"""
numbers=[6,5,3,8,4,2,5,4,11]
sum=0
for val in numbers:
    sum=sum+val

print("The sum is", sum)
"""
#range(start, stop, step_size)

print(list(range(10))) # 0-9

#lazy object

numbers=[6,5,3,8,4,2,5,4,11]

#len(numbers), in numbers only support iterators
#range(10) wont store all the values in memory
#forcing range function to give all value by using list

print(range(10))
print(list(range(10)))
print(list(range(2,8)))
print(list(range(2,20,3)))

















