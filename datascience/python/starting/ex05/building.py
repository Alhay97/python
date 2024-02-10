import sys


def is_punctuation(char):
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    return char in punctuation_chars


def analyze_string(s):
    counts = {
        "upper_case": sum(1 for char in s if char.isupper()),
        "lower_case": sum(1 for char in s if char.islower()),
        "punctuation": sum(1 for char in s if is_punctuation(char)),
        "digits": sum(1 for char in s if char.isdigit()),
        "spaces": s.count(' ')
    }
    return counts


def main():
    try:
        # Check if the correct number of arguments is provided
        if len(sys.argv) == 1:
            # Prompt user for input if no argument is provided
            input_str = input("What is the text to count?\n")
        elif len(sys.argv) == 2:
            # Use the provided argument
            input_str = sys.argv[1]
        else:
            # Raise an error if more than one argument is provided
            raise AssertionError("""AssertionError: more than one
                                 argument is provided""")

        # Analyze the provided string
        result = analyze_string(input_str)

        # Display the results
        print(f"Uppercase Characters: {result['upper_case']}")
        print(f"Lowercase Characters: {result['lower_case']}")
        print(f"Punctuation Characters: {result['punctuation']}")
        print(f"Digits: {result['digits']}")
        print(f"Spaces: {result['spaces']}")
    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
