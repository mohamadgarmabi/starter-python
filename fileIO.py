file = open("./file/test.txt", "r")

read_file = file.read()
print(read_file)

file.seek(0)

read_file = file.read()
print(read_file)

read_lines = file.readlines()
print(read_lines)

file.close()

with open("./file/test.txt", "r") as text_file:
    read_file = text_file.read()
    print(read_file)
print("--------------------------------")

with open("./file/output.txt", "a") as output_file:
    output_file.write("this is new text for output file")

with open("./file/output.txt", "r") as output_file:
    print(output_file.read())