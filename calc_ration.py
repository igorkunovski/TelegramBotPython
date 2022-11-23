import re
import copy

ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}


def sub_calc(expression_list):
    i = - 1
    for el in expression_list[:]:
        i += 1
        if el[1] in {'*', '/'} and i + 1 != len(expression_list):
            expression_list[i + 1][0] = ops[el[1]](float(el[0]), float(expression_list[i + 1][0]))
            expression_list.pop(i)
            i -= 1
    i = - 1
    for el in expression_list[:]:
        i += 1
        if el[1] in {'+', '-'} and i + 1 != len(expression_list):
            expression_list[i + 1][0] = ops[el[1]](float(el[0]), float(expression_list[i + 1][0]))
            expression_list.pop(i)
            i -= 1
    return expression_list[0][0]


def simple_calc(expression):
    expression = expression.replace(' ', '')
    pattern = r"(\()?(\-?\d{1,}\.?\d{0,})(\))?([*/+-]?)"
    expression_list = list(map(list, re.findall(pattern, expression)))
    expression_list = [list(filter(lambda x: x != '', el)) for el in expression_list]
    expression_list[-1].append('')

    while True:
        start = []
        end = []
        for i, el in enumerate(expression_list):
            if '(' in el:
                start.append(i)
            elif ')' in el:
                end.append(i)
        if start and end:
            sub_expression_list = copy.deepcopy(expression_list[start[-1]:end[0] + 1])
            sub_expression_list[0].remove('(')
            sub_expression_list[-1].remove(')')
            sub_expression_list[-1].append('')
            sub_result = sub_calc(sub_expression_list)
            expression_list[end[0]][0] = sub_result
            count = 0
            for i in range(start[-1], end[0]):
                expression_list.pop(i - count)
                count += 1
        else:
            break

    return sub_calc(expression_list) if sub_calc(expression_list) % 1 != 0 else int(sub_calc(expression_list))