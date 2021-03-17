Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list
>>> # ordered collection of itom/elements
>>> # syntax is [ ]
>>> languages = ["Python", "C","C++","Java"]
>>> print(languages)
['Python', 'C', 'C++', 'Java']
>>> type(languages)
<class 'list'>
>>> # find the length of the list
>>> len(languages)
4
>>> #Access the element of the list
>>> #[ ] => Subscipt Oprator
>>> languages[0]
'Python'
>>> languages[-1]
'Java'
>>> languages[3]
'Java'
>>> languages[0][0]
'P'
>>> languages[0][-1]
'n'
>>> languages[0]
'Python'
>>> languages[0][-2:]
'on'
>>> languages[0][4:]
'on'
>>> languages[0:2]
['Python', 'C']
>>> #Append
>>> Add an element at the end of the list
SyntaxError: invalid syntax
>>> #Add an element at the end of the list
>>> languages.append("Ruby")
>>> languages
['Python', 'C', 'C++', 'Java', 'Ruby']
>>> len(languages)
5
>>> #insert
>>> languages.insert(1,"Pascal")
>>> languages
['Python', 'Pascal', 'C', 'C++', 'Java', 'Ruby']
>>> # Delete Operator
>>> #Remove
>>> languages.remove("Java")
>>> languages
['Python', 'Pascal', 'C', 'C++', 'Ruby']
>>> languages.remove('ruby')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    languages.remove('ruby')
ValueError: list.remove(x): x not in list
>>> languages.pop(1)
'Pascal'
>>> languages
['Python', 'C', 'C++', 'Ruby']
>>> languages.pop(-1)
'Ruby'
>>> languages
['Python', 'C', 'C++']
>>> numlist = [100, 200, 300]
>>> numlist
[100, 200, 300]
>>> languages.append(numlist)
>>> languages
['Python', 'C', 'C++', [100, 200, 300]]
>>> len(languages)
4
>>> languages.append(mylist)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    languages.append(mylist)
NameError: name 'mylist' is not defined
>>> languages
['Python', 'C', 'C++', [100, 200, 300]]
>>> anlist = [1, 2, 3, 4]
>>> languages.extend(anlist)
>>> languages
['Python', 'C', 'C++', [100, 200, 300], 1, 2, 3, 4]
>>> len(languages)
8
>>> len(anlist)
4
>>> teams = ["RCB", "CSK"]
>>> languages.insert(2, teams)
>>> languages
['Python', 'C', ['RCB', 'CSK'], 'C++', [100, 200, 300], 1, 2, 3, 4]
>>> s = "WELCOME"
>>> languages.append(s)
>>> languages
['Python', 'C', ['RCB', 'CSK'], 'C++', [100, 200, 300], 1, 2, 3, 4, 'WELCOME']
>>> languages.extend(s)
>>> languages
['Python', 'C', ['RCB', 'CSK'], 'C++', [100, 200, 300], 1, 2, 3, 4, 'WELCOME', 'W', 'E', 'L', 'C', 'O', 'M', 'E']
>>> len(languages)
17
>>> languages.append(12345)
>>> languages
['Python', 'C', ['RCB', 'CSK'], 'C++', [100, 200, 300], 1, 2, 3, 4, 'WELCOME', 'W', 'E', 'L', 'C', 'O', 'M', 'E', 12345]
>>> languages.extend(12345)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    languages.extend(12345)
TypeError: 'int' object is not iterable
>>> a = "56789"
>>> languages.append(a)
>>> languages
['Python', 'C', ['RCB', 'CSK'], 'C++', [100, 200, 300], 1, 2, 3, 4, 'WELCOME', 'W', 'E', 'L', 'C', 'O', 'M', 'E', 12345, '56789']
>>> languages.extend(a)
>>> languages
['Python', 'C', ['RCB', 'CSK'], 'C++', [100, 200, 300], 1, 2, 3, 4, 'WELCOME', 'W', 'E', 'L', 'C', 'O', 'M', 'E', 12345, '56789', '5', '6', '7', '8', '9']
>>> a = 1
>>> languages.append(a)
>>> numlist
[100, 200, 300]
>>> a ="1"
>>> numlist.append(a)
>>> numlist.extend(a)
>>> numlist
[100, 200, 300, '1', '1']
>>> teams = ["CSK", "RCB", "MI"]
>>> team.count("RCB")
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    team.count("RCB")
NameError: name 'team' is not defined
>>> teams.count("RCB")
1
>>> languages.count("E")
2
>>> languages.count(100)
0
>>> languages
['Python', 'C', ['RCB', 'CSK'], 'C++', [100, 200, 300, '1', '1'], 1, 2, 3, 4, 'WELCOME', 'W', 'E', 'L', 'C', 'O', 'M', 'E', 12345, '56789', '5', '6', '7', '8', '9', 1]
>>> len(languages)
25
>>> languages.pop(len(languages)-3)
'8'
>>> languages
['Python', 'C', ['RCB', 'CSK'], 'C++', [100, 200, 300, '1', '1'], 1, 2, 3, 4, 'WELCOME', 'W', 'E', 'L', 'C', 'O', 'M', 'E', 12345, '56789', '5', '6', '7', '9', 1]
>>> languages[4][0]
100
>>> del languages[1]
>>> languages
['Python', ['RCB', 'CSK'], 'C++', [100, 200, 300, '1', '1'], 1, 2, 3, 4, 'WELCOME', 'W', 'E', 'L', 'C', 'O', 'M', 'E', 12345, '56789', '5', '6', '7', '9', 1]
>>> languages.index("C++")
2
>>> del languages[-4:]
>>> languages
['Python', ['RCB', 'CSK'], 'C++', [100, 200, 300, '1', '1'], 1, 2, 3, 4, 'WELCOME', 'W', 'E', 'L', 'C', 'O', 'M', 'E', 12345, '56789', '5']
>>> del languages[:-5]
>>> languages
['M', 'E', 12345, '56789', '5']
>>> languages.clear()
>>> languages
[]
>>> languages = ["Golang", "Peri", "C#"]
>>> languages
['Golang', 'Peri', 'C#']
>>> languages[2] = "C-Sharp"
>>> languages
['Golang', 'Peri', 'C-Sharp']
>>> s
'WELCOME'
>>> s[0]=z
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    s[0]=z
NameError: name 'z' is not defined
>>> # MUTABLE VS IMUABLE
>>> #LISTS are MULABLE
>>> # MUTABLE => element can be change/modified
>>> #IMUTABLE => element can not be changed
>>> s
'WELCOME'
>>> s="modified the string"
>>> s
'modified the string'
>>> word = "aeioubcdfg"
>>> print(word[:3] + word[3:])
aeioubcdfg
>>> names = ['Amir', 'Bear', 'Charlton', 'Daman']

>>> names
['Amir', 'Bear', 'Charlton', 'Daman']
>>> names[-1][-1]
'n'
>>> s = "# comment"
>>> print()/s

Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    print()/s
TypeError: unsupported operand type(s) for /: 'NoneType' and 'str'
>>> print(s)
# comment
>>> s1 = "Hello"
>>> s2 = "How are you"
>>> print(s1 +s2)
HelloHow are you
>>> print(s1+','+'/"'+s2+"/"")
      
SyntaxError: EOL while scanning string literal
>>> s = 'Hello, "How are you"'
>>> print(s)
Hello, "How are you"
>>> print(s1+','+'/"'+s2+'/"')
Hello,/"How are you/"
>>> print(s1+','+'"'+s2+'"')
Hello,"How are you"
>>> 