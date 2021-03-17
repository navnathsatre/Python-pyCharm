Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> i = 10
>>> print(i)
10
>>> type(i)
<class 'int'>
>>> i = 'WELCOME'
>>> PRINT(i)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    PRINT(i)
NameError: name 'PRINT' is not defined
>>> print(i)
WELCOME
>>> type(i)
<class 'str'>
>>> # hass is to specify comments
>>> #String
>>> #string can be specifified eithor double quotesor single quotes
>>> s="WELCOME"
>>> print(s)
WELCOME
>>> j = 'Python Programming'
>>> print(s)
WELCOME
>>> print(j)
Python Programming
>>> len(s)
7
>>> # indexing - subscipt operator
>>> print(s)
WELCOME
>>> # index always starts from zero (0) to length of string - 1
>>> s[0]
'W'
>>> s[3]
'C'
>>> s[6]
'E'
>>> s[7]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s[7]
IndexError: string index out of range
>>> s[-7]
'W'
>>> s[-1]
'E'
>>> s[2,6]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s[2,6]
TypeError: string indices must be integers
>>> # slicing
>>> a[0:3]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a[0:3]
NameError: name 'a' is not defined
>>> s[0:3]
'WEL'
>>> s[3:6]
'COM'
>>> s[3:7]
'COME'
>>> s[3:10]
'COME'
>>> s[3:]
'COME'
>>> s[:3]
'WEL'
>>> s[:]
'WELCOME'
>>> s[-7:-4]
'WEL'
>>> s[-4:]
'COME'
>>> s[-4:-]
SyntaxError: invalid syntax
>>> s[-4:-1]
'COM'
>>> s[-7:3]
'WEL'
>>> s[3:-1]
'COM'
>>> s[-1:3]
''
>>> msg = "Welcome to python Programming class"
>>> # Use slicing to print class
>>> msg[29:]
' class'
>>> msg[30:]
'class'
>>> msg[-5:]
'class'
>>> len(msg)
35
>>> msg[-5:len(msg)]
'class'
>>> folder = "c:\newfolder"
>>> print(folder)
c:
ewfolder
>>> folder = "c:\\newfolder"
>>> print(folder)
c:\newfolder
>>> folder = r"c:\newfolder"
>>> print(folder)
c:\newfolder
>>> #r is RAW string
>>> #Treat the string as it is. Don't escape any charachter
>>> 18+4
22
>>> 18-4
14
>>> 18/4
4.5
>>> 18//4
4
>>> 10%4
2
>>> #18/4 would give 4 in pyhton 2.7
>>> #18/4 would give 4.5 in python 3.x
>>> s = "WELCOME"
>>> s+10
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s+10
TypeError: can only concatenate str (not "int") to str
>>> s + "10"
'WELCOME10'
>>> s * 3
'WELCOMEWELCOMEWELCOME'
>>> # * operator has dual role
>>> # either it will act as multiplication operator or repetition operator
>>> "Hello"*3
'HelloHelloHello'
>>> 