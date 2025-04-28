# # loops in python
# # for loop
# for i in range(10):
#    print(i) # 0 1 2 3 4 5 6 7 8 9
# # while loop
# i=0
# while i<20:
#    print("I love Code") # 0 1 2 3 4 5 6 7 8 9
#    i+=1
# # break statement
# for i in range(10):
#    if i==5:
#        break # break the loop when i=5
#    print(i) # 0 1 2 3 4
# # continue statement
# for i in range(10):
#    if i==5:
#        continue # skip the loop when i=5
#    print(i) # 0 1 2 3 4 6 7 8 9
# # pass statement
# for i in range(10):
#    if i==5:
#        pass # do nothing when i=5
#    print(i) # 0 1 2 3 4 5 6 7 8 9
# # # list comprehension
# # # creating a list using list comprehension
# # my_list=[x for x in range(10)] # create a list of numbers from 0 to 9
# # print(my_list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example 1
# i = 1
# while i < 101:
#     print(i)
#     i += 1
#     # Example 2
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1
#Example 2
# i=1
# n=int(input("Enter the number: "))
# while i<11:
#     print(n*i) 
#     i+=1
#Example 3
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length = len(nums)
i = 0
while i < length:
    print(nums[i])
    i += 1