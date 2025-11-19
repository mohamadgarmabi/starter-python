new_tuple = (1,2,3,4,"mohammad", 3.14, True, False)

print("new_tuple", new_tuple)

print("first item", new_tuple[0])
print("last item", new_tuple[-1])
print("length of tuple", len(new_tuple))

# convert tuple to list
new_list = list(new_tuple)
print("new_list", new_list)
convert_tuple = tuple(new_list)
print("convert_tuple", convert_tuple)


# new_tuple for user_info
new_user_info = ("mohammad", 31, "tehran", "iran")

name, age, city, country = new_user_info

print("name", name)
print("age", age)
print("city", city)
print("country", country)


# best performance tuple
# immutable