import sys


MORSE_CODE_DICT = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----."
}


def encode_to_morse(text):
    morse_code = ""
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + " "
        else:
            raise AssertionError("Unexpected character found")
    return morse_code.strip()


def check_input(string):
    # Ensure all characters are either alphabets, digits, or spaces
    if not all(char.isalnum() or char == ' ' for char in string):
        raise AssertionError("AssertionError: the arguments are bad")


def main():
    try:
        # Check for the correct number of arguments
        if len(sys.argv) != 2:
            raise AssertionError("AssertionError: the arguments are bad")
        
        st = sys.argv[1]
        # Validate the input
        check_input(st)
        # Encode to Morse
        code = encode_to_morse(st)
        print(code)
    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()