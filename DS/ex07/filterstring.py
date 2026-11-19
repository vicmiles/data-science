import sys
from unittest import result

def select_word(words, condition):
    return([word for word in words if condition(word)])

def main() -> None:
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        txt = sys.argv[1]
        condition = int(sys.argv[2])

        res = select_word(txt.split(), lambda word: len(word) > condition)
        print(res)

    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")

if __name__ == "__main__":
    main()
    