def give_bmi(
    height: list[int | float],
    weihgt: list[int | float]
) -> list[int | float]:
    bmi = []
    i = 0
    for j in weihgt:
        calc = j/(height[i]**2)
        bmi.append(calc)
        i += 1
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    checker = []
    for i in bmi:
        if i > limit:
            checker.append(True)
        elif i < limit:
            checker.append(False)
    return checker


def main():
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
