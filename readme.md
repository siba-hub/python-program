what is python ?

- python is simple, easy and portable.
- python is free and open source.
- python is high leve; interpreted language.
- python is devloped by guido van rosum.


- python us interpreted language means when we write python code its executed the code line by line thats why we called python is interpreted language.

- print is function to give output statement in python. simply we can tell "print" is output function.

character set of python language :-
1. letter -> A-Z, a-z
2. digits -> 0-9
3. speical character -> -,+,*,/ etc.....
4. whitespace -> blank space,tab,newline

what is variable in python :- a variable is a name given to memory location in a program or else we can simply say variable is container to store some data.

example -
nmae="shradha"
age= 23
salary= 23000.56

variable - name,age,salary
variables - "shradha" , 23,23000.56


rules for identifiers :-
1. identifiers - name of the variables
2. identifiers can be combination of uppercase and lowercase letter, digits and an underscores(_). ex. myVariable , variable_1
3. an identifiers can not start with digits.so while variable1 is valid but 1variable is not valid.
4. we cann't use speical characters or sumbol like !,#,@,%,etc..
5. identifiers can be of any length.
6. variables name should be small and meaningful like - when we give our age in that case we take the variable as "myAge".
myAge -> camle case letter.


- 'type' is operator is show the datatypes anme in our variables like which datatypes we use in our variables.


DATATYPES :-
- mainly datatypes of 5 types in python.
- these data types are unmuteable or bulid-in data types .
1. integer - +ve value,0,-ve value.
2. string - "hello" , "shradha" , etc..
3. float - 0.46,4.00, etc...
4. boolean -true, false
5. none - not assign


comments in python :-
  

- when we can write some code but don't want to execute it then we give the comment line to that place so that line of code will not executed.
- comments are of 2 types 
1. single line comment -
   when we give the single line comments in python we did it on "#".
   ex.
   # single line comment
   # this is a comment
2. multi line comment -
when we give the multi line comment in python we did it through """_""".
ex. 
"""
  multi line 
  comments
  """

  types of operator :-
  - simply we can say operator is symbol tha performs a certain operations between operands.
  ex. a + b
  a,b -> operands
  + -> operators
- there are 4 types of operators present in python
1. arithmatic operator. - (+,-,*,/)
2. relational operator. - (==,!=,>,<,>,<=,>=)
3. assignment operator. - (=,+=,-=,*=,/=,%=) 
4. logical operator. - (and, or, not)

Input in python :-
 
 - Input() statement is used to accept values(use keyboard) from user.

strings :-
 
 - string is datatype that stores a sequence of characters.


 str1 = "this is good day"
 str2 = 'this is beautiful day'
 str3 = """this is a bad day"""

all these string are real string because in python it supports all os these syntax like - "",'',""" """

- \n(new line) - when we want break our line into a new line then we can give the the new line symbol in that place so the line get breaked automatically.

basic operation of strings :-

1. concatination ->
      "hello" + "world" =
2. length of string ->
      len(str)  


indexing of string ->

- webbocket -> 012345678(indexing)
- always indexing start from '0'.


slicing of string ->

- accessing a part of string.
- ending index is not counting.
- syntax - str[starting_index : ending_index]

str = "webbocket"
str[0:3] - web
str[:3] - web
str[3:] - bocket


function of string ->

ex -
str = "i am a coder"
1. str.endswith("er.") - returs true if staring ends with substrings.
2. str.capitalize() - returns 1st character is capital.
3. str.replace(old,new) - replace all occurrences of old with new.
4. str.find(word) - returns 1st index of 1st occurrence.
5. str.count("am") - counts the occurrence of substring in string.

conditional statement:-
  - used to handle the condition in your program.
  - syntax(if-elif-else)
  - elif means else-if

  if(condition);
   statement1
   elif(condition);
   statement2
   else:
   statement(default)

HOMEWORK :-
1.write a program to check if a number entered by the user if odd or even.
2.write a program to find the greatest of 3 numbers enterd by the userd.
3.write a program to check if  a number is a multiple of 7 or not.

Lists in Python :-
-Lists is a built-in data type that stores set of values.
-it can store elements of different types like integer,float & string etc...
-in list we can make indexing'
-in list we can find length of the list also.
-in list we can also do the slicing activity.

ex-
marks =[87,45,67,83,45] - array and list
student =["hitesh",85,"kabisuryanagar"]-list


List slicing:-
-it similar to string slicing.
-syntax :-list_name[starting_idx : ending_idx]
-ending index is not included.

marks = [23,25,67,78,98]
marks[1:4] -> [25,67,78]
marks[:3] -> [23,25,67]
marks[]



list = Methods :-
list =[9,4,7,8,1]
list.append(6) - adds one element at the end of the list - [9,4,7,8,1,6]
list.sort() - sort the elements in assending order - [ 1,4,7,8,9]
list.sort(reverse=true) - sorts the element in decending order - [9,8,7,4,1]
list.reverse() - reversing the list - [1,8,7,4,9]
list.insert(idx,el) - insert the element at index
list.remove(1) - remove the first occurance of element - [9,7,8,1]
list.pop(idx) - remove element at index

git:-

- git is a open source repository system where we can save,manipulate,colaborate our code with any one else.
- in our software era, everyone can use git system for their software devlopment.
- we also called git is a version control system.
- git provides some tools to use their functionalitynand features ex - github, gitlab etc....

