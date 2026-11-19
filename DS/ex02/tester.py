from find_ft_type import all_thing_is_obj

all_thing_is_obj(["Hello", "tata!"])
all_thing_is_obj(("Hello", "toto!"))
all_thing_is_obj({"Hello", "tutu!"})
all_thing_is_obj({"Hello": "titi!"})
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))