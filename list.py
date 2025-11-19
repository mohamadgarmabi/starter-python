test_list = [0, 1, 2, 3, 4, 5]
# print the whole list
print(test_list)

# first item of the list
print(test_list[0])

# last item of the list
print(test_list[-1])

# slice the list
print(test_list[1:3])

# slice the list with step
print(test_list[1:3:2])

# first 4 items of the list
print(test_list[:4])

# length of the list
print(len(test_list))

## list plus list

age_list = [12,30,31,45, 55]
names_list = ["mohammad", "ali", "reyhaneh", "amir"]

# contact list
contact_list = age_list + names_list
print("contact_list", contact_list)

# pop of list 
print("pop of list", contact_list.pop())
print("contact_list", contact_list)

# append to list
contact_list.append("reza")
print("contact_list", contact_list)

# # sort list
# age_list.sort()
# print("age_list", age_list)

# # reverse list
# age_list.reverse()
# print("age_list", age_list)

# # clear list
# age_list.clear()
# print("age_list", age_list)

# sort and reverse list
age_list.sort(reverse=True)
print("age_list", age_list)