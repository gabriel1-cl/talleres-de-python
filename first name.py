Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Type "help", "copyright", "credits" or "license()" 
>>> firstName= input("what is your first name?")
what is your first name? Bob
>>> print("Hello" +fistName+"¡")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print("Hello" +fistName+"¡")
NameError: name 'fistName' is not defined
>>> firstName= input("what is your first name?")
what is your first name? Bob
>>> print("Hello" +firstName+"¡")
Hello Bob¡
