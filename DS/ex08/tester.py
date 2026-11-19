from ft_filter import ft_filter

print(list(ft_filter(lambda x: x % 2 == 0, range(10))))
# [0, 2, 4, 6, 8]

print(list(ft_filter(None, [0, 1, "", "Hello", False])))
# [1, 'Hello']
