

ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list.append("World!")
ft_tuple = ft_tuple[:1] + ("Czech Republic!",)
ft_set.remove("tutu!")
ft_set.add("Prague!")
ft_dict["Hello"] = "42Prague!"

print(ft_list) 
print(ft_tuple)
print(ft_set)
print(ft_dict)