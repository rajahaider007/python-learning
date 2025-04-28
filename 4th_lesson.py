
# info={
#     "name":"4th_lesson",
#     "description":"This lesson covers the basics of Python data structures",
#     "author":"Your Name",
#     "date":"2023-10-01",
#     "version":"1.0",
# }
# # print(info["version"])
# # null dictionary
# null_dict={}
# # putting values in dictionary
# null_dict["name"]="John"
# null_dict["age"]=30
# null_dict["city"]="New York"
# # print(null_dict) # {'name': 'John', 'age': 30, 'city': 'New York'}
# #nested dictionary
# nested_dict={
#     "person1":{
#         "name":"John",
#         "age":30,
#         "city":"New York"
#     },
#     "person2":{
#         "name":"Jane",
#         "age":25,
#         "city":"Los Angeles"
#     }
# }
# print(nested_dict["person2"]["name"]) # {'person1': {'name': 'John', 'age': 30, 'city': 'New York'}, 'person2': {'name': 'Jane', 'age': 25, 'city': 'Los Angeles'}}
# #keys method    
# print(nested_dict.keys()) # dict_keys(['person1', 'person2'])
# #values method
# print(nested_dict.values()) # dict_values([{'name': 'John', 'age': 30, 'city': 'New York'}, {'name': 'Jane', 'age': 25, 'city': 'Los Angeles'}])
# #items method
# print(nested_dict.items()) # dict_items([('person1', {'name': 'John', 'age': 30, 'city': 'New York'}), ('person2', {'name': 'Jane', 'age': 25, 'city': 'Los Angeles'})])
# #update method
# nested_dict.update({"person3":{"name":"Mike","age":35,"city":"Chicago"}}) # add person3 to nested_dict
# # print(nested_dict) # {'person1': {'name': 'John', 'age': 30, 'city': 'New York'}, 'person2': {'name': 'Jane', 'age': 25, 'city': 'Los Angeles'}, 'person3': {'name': 'Mike', 'age': 35, 'city': 'Chicago'}}
# # pop method
# nested_dict.pop("person3") # remove person3 from nested_dict
# # print(nested_dict) # {'person1': {'name': 'John', 'age': 30, 'city': 'New York'}, 'person2': {'name': 'Jane', 'age': 25, 'city': 'Los Angeles'}}

# #set
# # creating a set
# my_set={1,2,3,4,5}
# # print(my_set) # {1, 2, 3, 4, 5}
# # adding values to set
# my_set.add(6) # add 6 to my_set
# # print(my_set) # {1, 2, 3, 4, 5, 6}
# # removing values from set
# my_set.remove(6) # remove 6 from my_set
# # print(my_set) # {1, 2, 3, 4, 5}
# # union of sets
# set1={1,2,3}
# set2={4,5,6}
# # set3=set1.union(set2) # union of set1 and set2
# # print(set3) # {1, 2, 3, 4, 5, 6}
# # intersection of sets
# set4={3,4,5}
# # set5=set1.intersection(set4) # intersection of set1 and set4
# # print(set5) # {3}
# # difference of sets
# set6=set1.difference(set4) # difference of set1 and set4
# # print(set6) # {1, 2}
# # symmetric difference of sets
# set7=set1.symmetric_difference(set4) # symmetric difference of set1 and set4
# # print(set7) # {1, 2, 4, 5}
# # frozen set
# frozen_set=frozenset([1,2,3,4,5]) # create a frozen set
# # print(frozen_set) # frozenset({1, 2, 3, 4, 5})
# # frozen_set.add(6) # TypeError: 'frozenset' object has no attribute 'add' # frozen set is immutable
# # print(frozen_set) # frozenset({1, 2, 3, 4, 5})

#Example 1
# marks_dict={}
# x=int(input("Enter phy numbers : "))
# marks_dict.update({"Phy": x})
# x=int(input("Enter math numbers: "))
# marks_dict.update({"math": x})
# x=int(input("Enter english numbers: "))
# marks_dict.update({"english": x})
# print(marks_dict) # {'Phy': 'x', 'Math': 'x', 'English': 'x'}
#Example 2