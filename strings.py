long_text= "this is long text and i want to print it"
length_of_long_text = len(long_text)
last_character = long_text[-1]
slice_of_long_text = long_text[0:5]
slice_with_step = long_text[0:10:4]
number_of_spaces = long_text.count(" ")
string_of_numbers = "0123456789"
reversed_string_of_numbers = string_of_numbers[::-1]
new_long_text = """this is new long text and i want to print it
this is new long text and i want to print it
this is new long text and i want to print it
"""
my_name = "mohammad"
likes = "python,you,coding,reading,writing"



print("likes:", likes)
print("likes split:", likes.split(","))
print("length of long text:", length_of_long_text)
print("last character:", long_text[int(length_of_long_text-1)])
print("last character with other way:", last_character)
print("first character:", long_text[0])
print("slice_of_long_text:", slice_of_long_text)
print("slice_with_step:", slice_with_step)
print("number_of_spaces:", number_of_spaces)
#---------------------------------#
print("string_of_numbers:", string_of_numbers)
print("string_of_numbers length:", len(string_of_numbers))
print("string_of_numbers index of 5:", string_of_numbers.index("5"))
print("string_of_numbers count of 0:", string_of_numbers.count("0"))
print("string_of_numbers replace 0 with 1:", string_of_numbers.replace("0", "1"))
print("string_of_numbers slice with step 2:", string_of_numbers[0:4:2])
print("string_of_numbers slice with step 4:", string_of_numbers[1::4])
print("reversed_string_of_numbers:", reversed_string_of_numbers)
print("new_long_text:", new_long_text)
print("my_name:", my_name)
print("name with capital letter:", "M"+ my_name[1:])