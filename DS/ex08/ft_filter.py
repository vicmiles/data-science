def ft_filter(function, iterable):
    for item in iterable:
        if function is None:
            if item:
                yield item
        elif function(item):
                yield item

def main():
    pass

if __name__ == "__main__":
     main()