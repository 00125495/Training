"""
Function
1. Function Header
2. Docstrings
3. args
    3.1 Postional
    3.2 Default
    3.3 Keyword
    3.4 Arbitary args ( *names)
4. Return values
5. Built-in/Global/Local Namespace
6. variable scope vs namespace
7. Global keyword--> how to use
8. Recursive Functions
"""

def function_name([para]):
    docstring
    stats(s)
    return [optional] -- None

function_name()

print(function_name.__doc__)
"""
def absolute_value(num):
    """ this function returns absolute
    value of the entered number
    """
    if num >= 0:
        return num
    else:
        return -num

print(absolute_value(2))
print(absolute_value(-4))
