# initialize the data structures
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# access and modify by index
ft_list[1] = "World!"

# since tuples are immutable,
# we have to use a workaround
# convert to list
ft_tuple = list(ft_tuple)

# modify with list method
ft_tuple[1] = "Malaysia!"

# convert back to tuple
ft_tuple = tuple(ft_tuple)

# since sets are immutable (as they use hashing for efficiency)
# we have to use a workaround
# remove the value
ft_set.remove("tutu!")

# add the new value to the set
ft_set.add("Kuala Lumpur")

# access and modify by key
ft_dict["Hello"] = "42KL!"

# print the data structures
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
