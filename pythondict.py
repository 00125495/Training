#Dict - Dict is an unordered collection of items and each element has 
#key value pairs
# dict are optimized to retrieve values 
#when the key is known
#1. get()
#2. pop(), popitem()
#3. clear(), del
#4. 
>>> #enumerate()- works with sets
... 
>>> #enumerate(iterable, start=0 )
... 
>>> g={'a','b','c'}
>>> 
>>> type(enumerate(g))
<class 'enumerate'>
>>> 
>>> 
>>> print(enumerate(g))
<enumerate object at 0x107a3df30>
>>> print(list(enumerate(g)))
[(0, 'c'), (1, 'b'), (2, 'a')]
>>> 
>>> for item in enumerate(g):
...  print(item)
... 
(0, 'c')
(1, 'b')
(2, 'a')
>>> for count, item in enumerate(g):
...  print(count, item )
... 
0 c
1 b
2 a
>>> 
>>> g={'a','b','c'}
>>> 
>>> print(list(enumerate(g, start=100)))
[(100, 'c'), (101, 'b'), (102, 'a')]
>>> 
>>> enumerate(g, start=10)
<enumerate object at 0x107a3df30>
>>> 
>>> list(enumerate(g, start=10))
[(10, 'c'), (11, 'b'), (12, 'a')]
>>> tuple(enumerate(g, start=10))
((10, 'c'), (11, 'b'), (12, 'a'))
>>> list(g)
['c', 'b', 'a']
>>> 
>>> tuple(g)
('c', 'b', 'a')
>>> 
>>> 







>>> #zip()- zip(*iterable)
... 
>>> number_list={1,2,3}
>>> str_set={'a','b','c'}
>>> 
>>> result=zip()
>>> 
>>> type(result)
<class 'zip'>
>>> 
>>> result=zip(number_list, str_set)
>>> 
>>> type(result)
<class 'zip'>
>>> 
>>> set(result)
{(3, 'a'), (1, 'c'), (2, 'b')}
>>> 
>>> list(result)
[]
>>> number_list=[1,2,3]
>>> str_set=[4,5,6]
>>> result=zip(number_list, str_set)
>>> list(result)
[(1, 4), (2, 5), (3, 6)]
>>> 
>>> number_list=[1,2,3]
>>> str_list=['a','b']
>>> number_tuple=('one','two','three','four')
>>> 
>>> 
>>> result=zip(number_list, number_tuple )
>>> 
>>> set(result)
{(3, 'three'), (2, 'two'), (1, 'one')}
>>> 
>>> 
>>> result=zip(number_list, str_list, number_tuple )
>>> 
>>> set(result)
{(1, 'a', 'one'), (2, 'b', 'two')}
>>> list(result)
[]
>>> 
>>> result=zip(number_list, str_list, number_tuple )
>>> list(result)
[(1, 'a', 'one'), (2, 'b', 'two')]
>>> 
>>> 
>>> result=zip(number_list, str_list, number_tuple )
>>> set(result)
{(1, 'a', 'one'), (2, 'b', 'two')}
>>> type(result)
<class 'zip'>
>>> 
>>> list(result)
[]
>>> 
>>> coordinate=['x','y','z']
>>> value=[3,4,5]
>>> result=zip(coordinate, value)
>>> result_list=list(result)
>>> 
>>> result_list
[('x', 3), ('y', 4), ('z', 5)]
>>> 
>>> c,v=zip(*result_list)
>>> 
>>> c
('x', 'y', 'z')
>>> v
(3, 4, 5)
>>> 
>>> set(c)
{'z', 'y', 'x'}
>>> 








>>> #frozenset
... 
>>> #tuples are immutable list
... #frozensets are immutable sets
... 
>>> #sets being mutable are unhasable -- key for dict
... 
>>> a={1,2,3}
>>> type(a)
<class 'set'>
>>> 
>>> b=frozenset([1,2,3])
>>> 
>>> type(b)
<class 'frozenset'>
>>> 
>>> d={a:'123'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
>>> 
>>> d={b:'123'}
>>> 
>>> d
{frozenset({1, 2, 3}): '123'}
>>> 
>>> A=frozenset([1,2,3,4])
>>> 
>>> B=frozenset([3,4,5,6])
>>> 
>>> a=set([1,2,3,4])
>>> 
>>> a.add(5)
>>> 
>>> A.add(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'add'
>>> 
>>> A.isdisjoint(B)
False
>>> 
>>> A|B
frozenset({1, 2, 3, 4, 5, 6})
>>> 
>>> type(A|B)
<class 'frozenset'>
>>> 
>>> 



>>> my_dict={}
>>> 
>>> type(my_dict)
<class 'dict'>
>>> 
>>> my_dict={1:'apple', 2:'ball'}
>>> 
>>> my_dict
{1: 'apple', 2: 'ball'}
>>> 
>>> my_dict={'name':'samba', 1:[2,4,3]}
>>> 
>>> my_dict=dict({1:'apple', 2:'ball'})
>>> 
>>> my_dict
{1: 'apple', 2: 'ball'}
>>> 
>>> my_dict=dict([(1,'apple'), (2,'ball')])
>>> 
>>> my_dict
{1: 'apple', 2: 'ball'}
>>> 
>>> my_dict=dict([[1,'apple'], [2,'ball']])
>>> 
>>> my_dict
{1: 'apple', 2: 'ball'}
>>> 
>>> 
>>> 
>>> #accessing the data
... 
>>> #dict--key access the data
... 
>>> my_dict={'name':'test', 'age':26}
>>> 
>>> print(my_dict['name'])
test
>>> 
>>> print(my_dict.get('age'))
26
>>> 
>>> print(my_dict.get('address'))
None
>>> 
>>> print(my_dict['adress'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'adress'
>>> 






>>> #changing and adding elements in dict
... 
>>> 
>>> my_dict={'name':'test', 'age':26}
>>> 
>>> my_dict['age']
26
>>> my_dict['age']=27
>>> 
>>> my_dict
{'name': 'test', 'age': 27}
>>> 
>>> my_dict['address']='KL'
>>> 
>>> my_dict
{'name': 'test', 'age': 27, 'address': 'KL'}
>>> #remove
... 
>>> 







>>> squares={1:1,2:4,3:9,4:16,5:25}
>>> 
>>> print(squares.pop(4))
16
>>> 
>>> squares
{1: 1, 2: 4, 3: 9, 5: 25}
>>> print(squares.popitem())
(5, 25)
>>> 
>>> print(squares.popitem())
(3, 9)
>>> print(squares.popitem())
(2, 4)
>>> print(squares.popitem())
(1, 1)
>>> squares={1:1,2:4,3:9,4:16,5:25}
>>> print(squares.pop())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pop expected at least 1 arguments, got 0
>>> print(squares.popitem())
(5, 25)
>>> 


>>> squares.clear()
>>> 
>>> squares
{}
>>> del squares
>>> 
>>> squares
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'squares' is not defined
>>> 
>>> 
KeyboardInterrupt
>>> 
>>> ^D
Rajendras-MacBook-Pro:~ rajendrakoniki$ 
Rajendras-MacBook-Pro:~ rajendrakoniki$ 
Rajendras-MacBook-Pro:~ rajendrakoniki$ 








Rajendras-MacBook-Pro:~ rajendrakoniki$ python3
Python 3.7.3 (default, Apr  7 2020, 14:06:47) 
[Clang 11.0.3 (clang-1103.0.32.59)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 




















>>> my_dict ={}
>>> 
>>> my_dict
{}
>>> 
>>> my_dict={1:'apple',2:'ball'}
>>> 
>>> my_dict
{1: 'apple', 2: 'ball'}
>>> 
>>> my_dict={'name':'samba', 1:[2,3,4]}
>>> 
>>> my_dict=dict({1:'apple',2:'ball'})
>>> 
>>> my_dict=dict([(1,'apple'), (2,'ball')])
>>> 
>>> my_dict
{1: 'apple', 2: 'ball'}
>>> 
>>> my_dict[1]
'apple'
>>> 
>>> my_dict.get(1)
'apple'
>>> 
>>> my_dict[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 3
>>> my_dict.get(3)
>>> print(my_dict.get(3))
None
>>> print(my_dict[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 3
>>> 
>>> 
>>> my_dict={'name':'Naga', 'age':28}
>>> 
>>> my_dict['age']=26
>>> 
>>> my_dict
{'name': 'Naga', 'age': 26}
>>> 
>>> my_dict['address']='KL'
>>> 
>>> my_dict
{'name': 'Naga', 'age': 26, 'address': 'KL'}
>>> 
>>> squares={1:1,2:4,3:9,4:16,5:25}
>>> 
>>> print(squares.pop(4))
16
>>> 
>>> squares
{1: 1, 2: 4, 3: 9, 5: 25}
>>> 
>>> print(squares.popitem())
(5, 25)
>>> #LIFO
... 
>>> 
>>> 
>>> print(squares.clear())
None
>>> 
>>> squares
{}
>>> del squares
>>> 
>>> squares
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'squares' is not defined
>>> 














>>> 
>>> #copy() -method doesn't take any params
... this method return shallow copy
  File "<stdin>", line 2
    this method return shallow copy
              ^
SyntaxError: invalid syntax
>>> 


















>>> orginal = {1:'one',2:'two'}
>>> new = orginal.copy()
>>> 
>>> new
{1: 'one', 2: 'two'}
>>> 
>>> orginal = {1:'one',2:'two'}
>>> new=original
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'original' is not defined
>>> 
>>> new=orginal
>>> 
>>> new.clear()
>>> 
>>> orginal
{}
>>> new
{}
>>> orginal = {[1,2,3]:'one',2:'two'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> 

>>> orginal = {(1,2,3):'one',2:'two'}
>>> 
>>> orginal = {{1,2,3}:'one',2:'two'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
>>> orginal = {frozenset([1,2,3]):'one',2:'two'}
>>> 
>>> 
>>> my_set={1,2,3,{2,3,4}}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
>>> 
>>> #set - mutable, set element- immutable, frozenset-immutable 
... 
>>> my_set={1,2,3,frozenset([2,3,4])}
>>> 
>>> my_set
{1, 2, 3, frozenset({2, 3, 4})}
>>> 
>>> my_set[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>> 
>>> my_set
{1, 2, 3, frozenset({2, 3, 4})}
>>> 
>>> 
>>> for letter in set("samba"):
...  print(letter)
... 
s
b
m
a
>>> for letter in my_set:
...  print(letter)
... 
1
2
3
frozenset({2, 3, 4})
>>> 
>>> list(my_set)
[1, 2, 3, frozenset({2, 3, 4})]
>>> 
>>> 



>>> 
>>> a={1:2,2:3}
>>> 
>>> b=a
>>> 
>>> b
{1: 2, 2: 3}
>>> 
>>> id(a)
4468543280
>>> id(b)
4468543280
>>> 
>>> #shallow copy and deep copy
... 
>>> #dict.copy() - shallow copy
... 
>>> c=dict(a)
>>> 
>>> id(a)
4468543280
>>> id(c)
4469587904
>>> 


>>> #dict.fromkeys(sequence[,value])
... # creates a new dict from the given squ of ele with value
... #provide 
... 
>>> keys={'a','e','i','o','u'}
>>> 
>>> type(keys)
<class 'set'>
>>> 
>>> vowels=dict.fromkeys(keys)
>>> 
>>> print(vowels)
{'o': None, 'i': None, 'u': None, 'a': None, 'e': None}
>>> 
>>> keys={'a','e','i','o','u'}
>>> value='vowel'
>>> 
>>> vowels=dict.fromkeys(keys, value)
>>> 
>>> print(vowels)
{'o': 'vowel', 'i': 'vowel', 'u': 'vowel', 'a': 'vowel', 'e': 'vowel'}
>>> 



>>> keys={'a','e','i','o','u'}
>>> value=[1]
>>> 
>>> vowels=dict.fromkeys(keys, value)
>>> 
>>> print(vowels)
{'o': [1], 'i': [1], 'u': [1], 'a': [1], 'e': [1]}
>>> 
>>> 
>>> value.append(2)
>>> 
>>> value
[1, 2]
>>> 
>>> print(vowels)
{'o': [1, 2], 'i': [1, 2], 'u': [1, 2], 'a': [1, 2], 'e': [1, 2]}
>>> 








>>> keys={'a','e','i','o','u'}
>>> value=[1]
>>> 
>>> vowels={ key : list(value) for key in keys }
>>> 
>>> print(vowels)
{'o': [1], 'i': [1], 'u': [1], 'a': [1], 'e': [1]}
>>> 
>>> value.append(2)
>>> 
>>> print(vowels)
{'o': [1], 'i': [1], 'u': [1], 'a': [1], 'e': [1]}
>>> 
>>> value
[1, 2]
>>> 
>>> vowels={ key : list(value) for key in keys }
>>> 
>>> print(vowels)
{'o': [1, 2], 'i': [1, 2], 'u': [1, 2], 'a': [1, 2], 'e': [1, 2]}
>>> 
>>> value.append(3)
>>> 
>>> print(vowels)
{'o': [1, 2], 'i': [1, 2], 'u': [1, 2], 'a': [1, 2], 'e': [1, 2]}
>>> 
>>> key={1,2,3,4,5}
>>> value="aeiou"
>>> 
>>> {1:'a', 2:'e',3:'i',4:'o',5:'u'}






















>>> #get(key[,value])
... 
>>> 























>>> person ={'name':'naga', 'age':22}
>>> 
>>> print('Name:', person.get('name'))
Name: naga
>>> print('Age:', person.get('age'))
Age: 22
>>> 
>>> print('Salary:', person.get('salary'))
Salary: None
>>> 
>>> print('Salary:', person.get('salary',0.0))
Salary: 0.0
>>> #items()
... 
>>> print(person.items())
dict_items([('name', 'naga'), ('age', 22)])
>>> result=print(person.items())
dict_items([('name', 'naga'), ('age', 22)])
>>> 
>>> result=person.items()
>>> type(result)
<class 'dict_items'>
>>> 



>>> sales={'apple':2,'orange':3,'grapes':4}
>>> 
>>> items=sales.items()
>>> print('original:',items)
original: dict_items([('apple', 2), ('orange', 3), ('grapes', 4)])
>>> 
>>> del[sales['apple']]
>>> 
>>> print('updated:',items)
updated: dict_items([('orange', 3), ('grapes', 4)])
>>> 
>>> dir(items)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'isdisjoint']
>>>




>>> items
dict_items([('orange', 3), ('grapes', 4)])
>>> 
>>> items[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict_items' object is not subscriptable
>>> list(items)
[('orange', 3), ('grapes', 4)]
>>> 
>>> items=sales.items()
>>> 
>>> items['orange']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict_items' object is not subscriptable
>>> 









>>> #keys()
... 
>>> person={'name':'samba','age':26,'salary':350000.0}
>>> 
>>> print(person.keys())
dict_keys(['name', 'age', 'salary'])
>>> 
>>> empty_dict={}
>>> print(empty_dict.keys())
dict_keys([])
>>> 
>>> person={'name':'samba','age':26,'salary':350000.0}
>>> person.update({'loc':'KL'})
>>> 
>>> print(person.keys())
dict_keys(['name', 'age', 'salary', 'loc'])
>>> 









>>> #pop(key[, default])
... 
>>> sales={'apple':2, 'orange':3, 'grapes':4}
>>> 
>>> element=sales.pop('apple')
>>> 
>>> element
2
>>> 
>>> sales
{'orange': 3, 'grapes': 4}
>>> 
>>> element=sales.pop('guava')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'guava'
>>> 
>>> element=sales.pop('guava','banana')
>>> 
>>> element
'banana'
>>> sales
{'orange': 3, 'grapes': 4}
>>> 


>>> #setdefault(key[,dafault_vale])
... 
>>> person={'name':'naga', 'age':22}
>>> 
>>> age=person.setdefault('age')
>>> 
>>> person
{'name': 'naga', 'age': 22}
>>> age
22
>>> person={'name':'naga'}
>>> 
>>> salary=person.setdefault('salary')
>>> 
>>> person
{'name': 'naga', 'salary': None}
>>> 
>>> salary
>>> 
>>> print(salary)
None
>>> salary=person.setdefault('age',22)
>>> person
{'name': 'naga', 'salary': None, 'age': 22}
>>> age
22
>>> age=person.setdefault('age',22)
>>> 
>>> person
{'name': 'naga', 'salary': None, 'age': 22}
>>> age
22
>>> 
>>> #update- dict.update([other])
... 
>>> d={1:"one",2:"three"}
>>> 
>>> d1={2:"two"}
>>> 
>>> d.update(d1)
>>> 
>>> print(d)
{1: 'one', 2: 'two'}
>>> 
>>> d1={3:"three"}
>>> 
>>> d.update(d1)
>>> 
>>> print(d)
{1: 'one', 2: 'two', 3: 'three'}
>>> 








>>> d={'x':2}
>>> 
>>> d.update(y=3,z=0)
>>> 
>>> print(d)
{'x': 2, 'y': 3, 'z': 0}
>>> 



















>>> #dict.values()
... 
>>> sales={'apple':2, 'orage':3, 'grapes':4}
>>> 
>>> print(sales.values())
dict_values([2, 3, 4])
>>> 
>>> sales.update('grapes'=5)
  File "<stdin>", line 1
SyntaxError: keyword can't be an expression
>>> sales.update('grapes',5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: update expected at most 1 arguments, got 2
>>> sales.update('grapes' = 5)
  File "<stdin>", line 1
SyntaxError: keyword can't be an expression
>>> sales.update(grapes = 5)
>>> 
>>> sales
{'apple': 2, 'orage': 3, 'grapes': 5}
>>> d1=[('grapes',6)]
>>> 
>>> sales.update(d1)
>>> 
>>> sales
{'apple': 2, 'orage': 3, 'grapes': 6}
>>> print(sales.values())
dict_values([2, 3, 6])
>>> 
>>> 
>>> 
>>> marks={}.fromkeys(['maths','english','science'],0)
>>> 
>>> print(marks)
{'maths': 0, 'english': 0, 'science': 0}
>>> 
>>> for item in marks.items():
...  print(item)
... print(list(sorted(marks.keys())))
  File "<stdin>", line 3
    print(list(sorted(marks.keys())))
        ^
SyntaxError: invalid syntax
>>> 
>>> for item in marks.items():
...  print(item)
... 
('maths', 0)
('english', 0)
('science', 0)
>>> 
>>> print(list(sorted(marks.keys())))
['english', 'maths', 'science']
>>> 



>>> 
>>> squares={x: x*x for x in range(6)}
>>> 
>>> print(squares)
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> 
>>> squares = {}
>>> for x in range(6):
...  squares[x]=x*x
... 
>>> print(squares)
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> 
>>> odd_squares={x:x*x for x in range(11) if x%2 == 1}
>>> 
>>> odd_squares
{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
>>> 
>>> 
>>> print(1 in squares)
True
>>> 
>>> odd_squares
{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
>>> 

>>> for in in odd_squares:
  File "<stdin>", line 1
    for in in odd_squares:
         ^
SyntaxError: invalid syntax
>>> 




















>>> for in odd_squares:
  File "<stdin>", line 1
    for in odd_squares:
         ^
SyntaxError: invalid syntax
>>> for i in odd_squares:
...  print(squares[i])
... 
1
9
25
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyError: 7
>>> for i in odd_squares:
...  print(odd_squares[i])
... 
1
9
25
49
81
>>> odd_squares
{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
>>> 

>>> len(odd_squares)
5
>>> 
>>> #all(), any(),sorted(),len()

