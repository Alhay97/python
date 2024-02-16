import sys
from ft_filter import ft_filter


def main():
    try:
        st = sys.argv[1]
        x = int(sys.argv[2])
        if len(sys.argv) == 3:
            if isinstance(st, str) or isinstance(x, int):
                filtered_words = list(ft_filter(lambda word: len(word) > x,
                                                st.split()))
            else:
                raise AssertionError("AssertionError: invalid input")
        else:
            raise AssertionError("Exactly two arguments (string and integer) \
                                 are required.")
        print(filtered_words)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
