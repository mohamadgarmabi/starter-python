import datetime

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

user_info = {
  "name":"mohammad",
  "age": 31,
  "is_married": False,
  "favorite_list": ["reyhaneh", 7,"python"],
  "location_info":{
    "country": "iran",
    "city": "tehran",
    "address": "tehran, iran"
  },
  "last_login": now,
  "last_comment": "hello world"
}

print("user_info", user_info)

# print the name of the user
print("name", user_info["name"])

# print the age of the user
print("age", user_info["age"])

# print the is_married of the user
print("is_married", user_info["is_married"])

# print the favorite_list of the user
print("favorite_list", user_info["favorite_list"])

# get city from location_info
print("city", user_info["location_info"]["city"])

# print last login
print("last_login", user_info["last_login"])

# print last comment
print("last_comment", user_info["last_comment"])

# get keys
print("keys", user_info.keys())

# get values
print("values", user_info.values())

# get items
print("items", user_info.items())

# get length
print("length", len(user_info))

# add new item to user_info
user_info["new_item"] = "hello world"
print("user_info", user_info)

# remove item from user_info
user_info.pop("new_item")
print("user_info", user_info)

# update item in user_info
user_info["name"] = "mohammad garmabi"
print("user_info", user_info)

# get item from user_info
print("get", user_info.get("name"))

# update item in user_info
user_info.update({"name": "Mohammad"})

print("user_info", user_info)