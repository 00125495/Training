import copy
#copy.copy(x) # shallow copy
#copy.deepcopy(x) # deep copy
old_list=[[1,2,3], [4,5,6],[7,8,9],10]

new_list=copy.copy(old_list)

old_list[1][1] ='AA'

print('old list:', old_list)
print('ID of old list', id(old_list))

print('new_list:', new_list)
print('ID of new list', id(new_list))
