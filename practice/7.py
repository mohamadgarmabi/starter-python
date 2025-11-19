max_price = 50000
min_price = 20000

try:
    purchase_amount = int(input("enter the purchase amount: "))
except ValueError:
    print("Invalid input: please enter a number for the purchase amount.")
else:
    if purchase_amount > max_price:
        discount_rate = 0.20
        final_price = purchase_amount * (1 - discount_rate)
        print(f"the final price after 20% discount: {int(final_price)}T")
    elif min_price <= purchase_amount <= max_price:
        discount_rate = 0.10
        final_price = purchase_amount * (1 - discount_rate)
        print(f"the final price after 10% discount: {int(final_price)}T")
    else:
        print(f"the discount does not include you. the final price: {purchase_amount}T")