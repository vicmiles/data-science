import sys


def main():
    if (len(sys.argv) == 1):
        print("AssertionError: no argument")
        return

    if (len(sys.argv) > 2):
        print("AssertionError: too many arguments")
        return
    
    try:
        num = int(sys.argv[1])
    except (ValueError):
        print("AssertionError: argument is not an integer")
        return

    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()