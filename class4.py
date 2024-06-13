# example to apply condition for licence

# age=17
# if(age>=18):
#  print("can apply for licence")
# else:
#     print("you can't apply for licence")
    
#     # example of a trafic lights
    
#     light =input("enter the signal you see: ")
    
#     if(light=="red"):
#         print("stop")
#     elif(light=="green"):
#         print("go")
#     elif(light=="yellow"):
#         print("wait")
#     else:
#         print("you are fool")
        
    # example for student marksheet
    
# mark = float(input("enter your mark : "))
    
# if(mark >=90):
#         grade ="A"
# elif(mark >=80 and mark < 90):
#         grade ="B"
# elif(mark >=70 and mark < 80):
#         grade ="C"
# elif(mark >=60 and mark < 70):
#         grade ="D"
# elif(mark >=50 and mark < 60):
#         grade = "E"
# else:
#         grade ="F -> future chai wala"
# print("grade of the student is -", grade)
        
        
# list =[45,67,34,90,76,32]
# print(list)
# print(type(list))
# print(list[0]) 
# print(list[1]) 
# print(list[2])
# print(list[3])

# marks =[32,76,98,67,56,90]
# print(marks[1:5])
# print(marks[3:5])
# print(marks[:5])
# print(marks[3:])

# list = [2,1,3]
# list.append(5)
# print(list)
# print(list.sort())
# print(list)
# print(list.sort(reverse=true))
# print(list)
# print(list.reverse())
# print(list)
# print(list.insert(1,4))
# print(list)
# list.pop(4)
# print(list)

#check if a number entered by a user is even or odd

num = int(input("Enter a number:"))
if(num % 2 == 0):
    print("the number is an even number.")
else:
    print("the number is an odd number.")


#find the greatest of three numbers entered by the users

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))
if(num1 >= num2 and num1 >= num3):
    greatest = num1
elif(num2 >= num1 and num2 >= num3):
    greatest = num2
else:
    greatest = num3
print("the greatest number is:",greatest)


#To check if a number is multiple of 7 or not

num = int(input("Enter a number:"))
if(num % 7 == 0):
    print("number is multiple of 7")
else:
    print("number is not multiple of 7")