from find_ft_type import all_thing_is_obj

# initialize data structures
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# should print the types
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)

# should print easter egg
all_thing_is_obj("Brian")

# should print "Type not found"
# should return 42
print(all_thing_is_obj(10))
