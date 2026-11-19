import sys


def morse(txt: str) -> str:
    NESTED_MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/',
    }

    allowed = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789 "
    )
    codes = []

    for char in txt:
        if char not in allowed:
            raise AssertionError("the arguments are bad")
        codes.append(NESTED_MORSE[char.upper()])

    return " ".join(codes)

def main() -> None:
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        res = morse(sys.argv[1])
        print(res)
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()