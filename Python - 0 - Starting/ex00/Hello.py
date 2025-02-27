ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# For List

ft_list[1] = "Word!"
ft_tuple_list = list(ft_tuple)

# For Tuple

ft_tuple_list[1] = "France!"
ft_tuple = tuple(ft_tuple_list)

# For Set

ft_set.remove("tutu!")
dummy = {"Paris!"}
ft_set.update(dummy)
ft_set = set(sorted(ft_set))

# For Dict

ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)