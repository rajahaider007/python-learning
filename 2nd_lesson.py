# Strings in Python
# Concatenation of strings
# str1="apna"
# str2="school"
# str3=str1+str2  #apnaschool
# print(str3) #apnaschool                                          

# #slicing of strings
# str="apna school"
# print(str[0:4]) #apna
# print(str[0:2]) #apna
# print(str[0:]) #apnas
# print(str[:4]) #apna
# print(str[:-3]) #apna

# #endswith() method  
# string = "I am learning Python from apna college"  
# print(string.endswith("ege")) #True
# #capitalize() method
# string = "i am learning python from apna college"
# print(string.capitalize()) #I am learning python from apna college
# #replace() method
# string = "I am learning Python from apna college"   
# print(string.replace("apna", "my")) #I am learning Python from my college
# #find() method
# string = "I am learning Python from apna college"
# print(string.find("n")) #5
# #count() method
# string = "I am learning Python from apna college"
# print(string.count("a")) #4

# Example 1:
# name = input("Enter you name: ")
# print("The length of the string is:", len(name)) #Length of the string
# Example 2:
# string = "I am $learning Python from$ apna college$"
# print(string.count("$"))

# age=21
# if age>=18: 
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

#Example 1:
# age = int(input("Enter your age: "))
# if age >= 18: 
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")
# #Example 2
# light = "red"
# if light == "green":
#     print("Go")
# elif light == "yellow":
#     print("Get ready to stop")
# elif light == "red":
#     print("Stop")
# else:
#     print("Invalid light color")

# Example 3
# marks = int(input("Enter your marks: "))

# if type(marks) == int:
#     if marks >= 90:
#         print("Grade A")
#     elif marks >= 80 and marks < 90:
#         print("Grade B")
#     elif marks >= 70 and marks < 80:
#         print("Grade C")
#     elif marks < 70:
#         print("Grade D")
#     else:
#         print("Invalid marks")
# else:
#     print("Please enter a valid number")
# Example 4
# num = int(input("Enter a number: "))
# if num %2 == 0:
#     print("Even")
# else:
#     print("Odd")
# Example 5
a = int(input("Enter first number:"))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
elif c > a and c > b:
    print("c is greater")
else:
    print("All are equal")


