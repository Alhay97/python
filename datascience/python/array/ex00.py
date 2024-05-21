def give_bmi(height: list[int | float], weihgt: list[int | float]) -> list[int | float]:
    bmi =[]
    i = 0
    for j in weihgt:
        calc = j/(height[i]**2)
        bmi.append(calc)
        i+=1
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    checker = []
    for i in bmi:
        if i > limit:
            checker.append(True)
        elif i < limit:
            checker.append(False)
    return checker
