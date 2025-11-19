n = int(input("Enter a number: "))

while True:
    print(f"n is {n}")
    if n == 1: # if n is 1, break the loop
        print("n is 1, break the loop")   # print the message
        break   # break the loop
    if n % 2 == 0: # if n is even, divide n by 2
        print("n is even, divide n by 2")
        n //= 2   # divide n by 2
    else: # if n is odd, multiply n by 3 and add 1
        print("n is odd, multiply n by 3 and add 1")
        n = n * 3 + 1
