import sys
import string

def count_words(text: str) -> None:
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    digits = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in string.punctuation:
            punctuation += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main() -> None:
    try:
        if (len(sys.argv) > 2):
            raise AssertionError("more than one argument is provided")

        if (len(sys.argv) == 1 or sys.argv[1] == ""):
            print("What is the text to count?")
            text = sys.stdin.readline()
        else:
            text = sys.argv[1]

        count_words(text)

    except AssertionError as err:
        print(f"AssertionError: {err}")
        return
    except (OSError, UnicodeError) as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print()

if __name__ == "__main__":
    main()