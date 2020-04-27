if __name__ == "__main__":
    summ
    minus
    mul
    div


def summ(*params):
    # print(a+b)
    result = 0
    for i in params:
        result += i
    return result


def minus(*params):
    result = params[0]
    for i in params[1:]:
        result -= i
    return result


def mul(*params):
    result = 1
    for i in params:
        result *= i
    return result


def div(*params):
    result = params[0]
    for i in params[1:]:
        if i == 0:
            print("Error, division by zero")
            return 0
        result /= i
    return result