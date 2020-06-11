#list copy
#1. shallow copy
#2. deep copy

# python everything is class and object
#"=", creates reference 
old_list=[[1,2,3], [4,5,6], [7,8,'a']]

new_list = old_list

new_list[2][2] = 9

print('old list:', old_list)
print('ID of old list', id(old_list))

print('new_list:', new_list)
print('ID of new list', id(new_list))
