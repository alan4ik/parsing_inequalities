# -*- coding: utf-8 -*-
import csv
import sys
import codecs
import re


def eval_expression(input_string, first, second):
    allowed_names = {"x": first, "y": second}
    code = compile(input_string, "<string>", "eval")
    for name in code.co_names:
        if name not in allowed_names:
            raise NameError("Использование %s не разрешено." % name)
    return eval(code, {"__builtins__": {}}, allowed_names)


def parsing_inequalities(func):
    inequalities = [">=", "<=", "==", ">", "<"]
    find_inequalities = []
    arithmetic_operations = ["*", "/", "-", "+"]
    find_arithmetic_operations = []
    expression_without_inequality = ''

    for i in inequalities:
        if func.find(i) != -1:
            find_inequalities.append(i)
            expression_without_inequality = func.replace(i, "|||")
            break
    for i in inequalities:
        if expression_without_inequality.find(i) != -1:
            find_inequalities.append(i)
            expression_without_inequality = expression_without_inequality.replace(i, "|||")
            break
    expression_without_inequality = expression_without_inequality.split("|||")

    expression = ''
    if len(expression_without_inequality) == 2:
        expression = expression_without_inequality[0]
    elif len(expression_without_inequality) == 3:
        expression = expression_without_inequality[1]
    else:
        raise RuntimeError("Error parsing")

    inequality_without_arithmetic_operations = expression
    for i in arithmetic_operations:
        if expression.find(i) != -1:
            find_arithmetic_operations.append(i)
            expression = expression.replace(i, "|||")
    expression = expression.split("|||")

    old_expression = ''
    new_expression = ''
    if len(expression_without_inequality) == 2:
        old_expression = new_expression = expression_without_inequality[0]
    elif len(expression_without_inequality) == 3:
        old_expression = new_expression = expression_without_inequality[1]
    else:
        raise RuntimeError("Error parsing")

    print(expression)
    for i in range(len(expression)):
        if expression[i].find("(") != -1:
            expression[i] = expression[i].replace("(", "")
        elif expression[i].find(")") != -1:
            expression[i] = expression[i].replace(")", "")
    print(expression)
    for i in expression:
        if new_expression.find(i) != -1:
            if i.find("y.") != -1:
                new_expression = new_expression.replace(i, "y")
            elif i.find("x.") != -1:
                new_expression = new_expression.replace(i, "x")
    func = func.replace(old_expression, new_expression)
    return func
    # print(func)
    # int(eval(func, {"x": x, "y": y}))

x = 400
y = 100
fun = parsing_inequalities("y.t*(y.t+y.t)-x.heat_Q>=450")
print(eval_expression(fun, x, y))

