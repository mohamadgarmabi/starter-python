new_set = set()
ages = set()


# add item to set
new_set.add(1)
new_set.add(2)
new_set.add(3)
new_set.add(4)
new_set.add(50)

print("new_set", new_set)

# add item to set
ages.add(10)
ages.add(20)
ages.add(30)
ages.add(40)
ages.add(50)

print("ages", ages)

# union of sets
union_of_sets = new_set.union(ages)
print("union of sets", union_of_sets)

# intersection of sets
intersection_of_sets = new_set.intersection(ages)
print("intersection of sets", intersection_of_sets)

# difference of sets
difference_of_sets = new_set.difference(ages)
print("difference of sets", difference_of_sets)

# symmetric difference of sets
symmetric_difference_of_sets = new_set.symmetric_difference(ages)
print("symmetric difference of sets", symmetric_difference_of_sets)