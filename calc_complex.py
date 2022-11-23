def swap_mark(expr: str):

    start = ""
    new_expression = ""

    if expr[0].isdigit():
        start = "-"
    elif expr[0] == "+":
        expr = expr[1:]
        start = "-"

    for i, mark in enumerate(expr):
        if mark == "-" and i == 0:
            new_expression += "+"
        elif mark == "-":
            new_expression += "+"
        elif mark == "+" and i != 0:
            new_expression += "-"
        else:
            new_expression += mark

    return start + new_expression


# parenthesis_handling_addition method handles parenthesized expressions. if before brackets
# is a minus sign, then the signs "+" and "-" are reversed in brackets. Example: -(-4 + 2j) => +(+4 -2j)
def parenthesis_handling_addition(data: str):

    data = data.replace(" ", "")
    start = False
    index_start = None
    result = ""

    for i, mark in enumerate(data):
        if mark == "-" and data[i+1] == "(":
            index_start = i + 2
            start = True
            result += "+("
        elif mark == ")" and start:
            index_end = i
            replacement_data = data[index_start:index_end]
            start = False
            result += swap_mark(replacement_data) + ")"
        elif not start:
            result += mark
    return result


def calc_complex(data):
    # The written part. If there are no multiplication or division signs in the expression.
    # You can count different types of addition and subtraction
    if "/" not in data and "*" not in data:

        data = parenthesis_handling_addition(data)
        data = data.replace("(", "").replace(")", "").replace(" ", "").replace("-", "+-")
        data = data.split("+")

        reals = []
        nums_j = []

        for num in data:
            if "j" not in num and num != "":
                reals.append(num)
            elif "j" in num:
                nums_j.append(num)

        sum_reals = 0
        for i, num in enumerate(reals):
            sum_reals += int(reals[i])

        sum_nums_j = 0
        for i, num in enumerate(nums_j):
            sum_nums_j += int(num[:-1])

        if sum_nums_j >= 0:
            return f'{sum_reals} + {sum_nums_j}i'
        return f'{sum_reals}{sum_nums_j}i'

    # The part uses a built-in function (eval)
    elif "/" in data or "*" in data:
        return eval(data)

    else:
        return "Hmm..You are not supposed to be here"
