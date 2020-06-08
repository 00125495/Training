# Anonymous Function- Function without name
# Lambda function- Lambda keyword
# Normal FUnction - def keyword

# lambda *args: expression
# def function_name(args):
#    stmts(s)

# high-ordered functions
# Function which takes functions as args

# usually we pass lambda functions to high-ordered functions
# eg - Filter(), map()

# filter() - takes function and list as args

my_list = [1,5,4,6,8,11,3,12]
new_list1=list(filter(lambda x: (x%2 == 0), my_list))
print("filter output", new_list1)

my_list2=list(map(lambda x: (x%2 == 0 ), my_list))
print("map output", my_list2)
