#other things are same as 2nd lesson
#append method
# list1 = [1,2,3,4,5]
# list1.append(6)
# print(list1) # [1, 2, 3, 4, 5, 6]
# #sort method
# # list1.sort()
# # print(list1) # [1, 2, 3, 4, 5, 6]
# #sort desc method
# # list1.sort(reverse=True)    
# # print(list1) # [1, 2, 3, 4, 5, 6]
# #reverse method
# list1.reverse()
# print(list1) # [6, 5, 4, 3, 2, 1]
# #insert method
# list1.insert(0, 0) # insert 0 at index 0
# print(list1) # [0, 6, 5, 4, 3, 2, 1]
# #remove method
# list1.remove(0) # remove 0 from list1
# print(list1) # [6, 5, 4, 3, 2, 1]
# #pop method
# list1.pop() # remove last element from list1
# print(list1) # [6, 5, 4, 3, 2]
# #clear method
# list1.clear() # remove all elements from list1
# print(list1) # []
# #copy method
# list2 = list1.copy() # copy list1 to list2
# print(list2) # []
#tuple
# tuple is immutable/
# tuple1 = (1,2,3,4,5)
# print(tuple1) # (1, 2, 3, 4, 5)
# tuple1[0] = 0 # TypeError: 'tuple' object does not support item assignment
# print(tuple1) # (1, 2, 3, 4, 5)
# set
# set1 = {1,2,3,4,5}
# print(set1) # {1, 2, 3, 4, 5}
# set1[0] = 0 # TypeError: 'set' object does not support item assignment
# print(set1) # {1, 2, 3, 4, 5}
# set1.add(6) # add 6 to set1
# print(set1) # {1, 2, 3, 4, 5, 6}
# set1.remove(6) # remove 6 from set1
# print(set1) # {1, 2, 3, 4, 5}
# set1.clear() # remove all elements from set1
# print(set1) # set()
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8}
# print(set1.intersection(set2)) # {4, 5}
# print(set1.difference(set2)) # {1, 2, 3}
# print(set2.difference(set1)) # {8, 6, 7}
# print(set1.issubset(set2)) # False
# print(set1.issuperset(set2)) # False
# print(set1.isdisjoint(set2)) # False
# print(set1.symmetric_difference(set2)) # {1, 2, 3, 6, 7, 8}
# print(set1.pop()) # remove and return an arbitrary element from set1
# print(set1) # {2, 3, 4, 5}
# touple count method
# count the number of times 1 appears in tuple1
# tuple1 = (1,2,3,4,5,1,1,1)
# print(tuple1.count(1)) # 4
#index method
# find the index of 1 in tuple1
# print(tuple1.index(1)) # 0


#Exercise 1
# first_movie=input("Enter the name of your first fav movie: ")
# second_movie=input("Enter the name of your second fav movie: ")
# third_movie=input("Enter the name of your third fav movie: ")
# list1=[first_movie,second_movie,third_movie]
# print("Your fav movies are: ",list1)
#Exercise 2
# palindrome in string
# list1 = ["m","a","a","m"]
# copy_list1=list1.copy()
# copy_list1.reverse()
# if list1==copy_list1:
#     print("The list is palindrome")
# else:
#     print("The list is not palindrome")
# #Exercise 3
# grade=("A","B","C","D","E","A","C","A","D","B","C","A","D","E")
# print(grade.count("A")) # 4
#Exercise 4
grade=["A","B","C","D","E","A","C","A","D","B","C","A","D","E"]
grade.sort()
print(grade) # ['A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'E', 'E']
