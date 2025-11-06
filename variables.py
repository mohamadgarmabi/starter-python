"""
Variables and Calculations for Group Stay & Lunch Expenses

This script helps calculate the total and per-person cost for a group staying in a hotel (or peer location) and eating pizza, including a discount.

Variables:
    people_count (int): Number of people in the group.
    pizza_price (int): Price of one pizza (in local currency).
    pizza_count (int): Number of pizzas ordered.
    reservation_peer_night_price (int): Price of one night stay at the location.
    stay_at_hotel_count (int): Number of nights the group will stay.
    discount_percentage (float): Percentage discount to be applied.

Calculated Values:
    total_price (int): Sum of food and accommodation without applying the discount.
    total_price_without_discount (int): Redundant with total_price; kept for clarity if modifications are made.
    total_discount (float): Amount of discount based on total_price_without_discount and given percentage.
    total_price_peer_person (float): Price per person, calculated as total_cost divided by number of people.

Output:
    The script prints all the calculated values in a labelled output.
"""

# Number of people in the group
people_count = 4  # int

# Pizza lunch parameters
pizza_unit_price = 100000      # int: price per pizza
pizza_ordered_count = 12          # int: quantity of pizzas ordered

# Accommodation parameters
reservation_unit_price = 100000  # int: price per night for location
stay_at_location_count = 3                # int: number of nights staying

# Discount on total price (in percent)
discount_percentage = 10.5  # float

# Store the total price without discount (currently same as total_price)
total_price_without_discount = (pizza_unit_price * pizza_ordered_count) + (reservation_unit_price * stay_at_location_count)

# Calculate the discount value
total_price_with_discount = total_price_without_discount * discount_percentage / 100

# Calculate price per person
total_price_peer_person = total_price_with_discount / people_count

print(
    "total_price_without_discount :", total_price_without_discount,
    "total_price_with_discount :", int(total_price_with_discount),
    "total_price_peer_person :", int(total_price_peer_person)
)