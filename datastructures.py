# List Data Structure

my_list = ["Toyota", "BMW", "Nissan", "Audi", "Subaru", "Jeep"]
my_list.append("Mazda")
print(my_list)
print(my_list[0])
print(my_list[2])
print(my_list[1], "is manufactured in Germany")
my_list[1] = "Mercedes"  # It is Mutable
print(f"{my_list[1]} is manufactured in Germany")

print(type(my_list))

thislist = [7, 17, 37, 10, 8, 49, 20]
thislist.insert(3, 5)
print(thislist)

# Tuple Data Structure
#   Cannot change anything once it is crested

my_tuple = ("Banana", "Oranges", "Apples", "Mango", "Guava", "Orange")
print(my_tuple)
print(f"I like eating {my_tuple[2]}")
# my_tuple[2] = "Berries"
print(f"I like eating {my_tuple[2]}")
# my_tuple.insert(2, Berries)


# Set Data Structure

my_set = {"Red", "Blue", "Green", "Yellow", "Purple"}
print(my_set)

# Dictionaries Data Structure
my_dict = {"name": "Peter", "Age": 45, "Gender": "Male"}
print(my_dict)
print(my_dict["Age"])
print("His name is", {my_dict["name"]})
print("His name is", {my_dict["name"]})
# print(f"{my_dict["name"]} is his name")
print("His name is", {my_dict["name"]},
      "and he is ", {my_dict["Age"]})