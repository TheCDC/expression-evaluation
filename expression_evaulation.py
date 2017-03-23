"""An algebraic epxression evaluator.
TODO: handle negative number literals (preceding minus signs)
"""
from pudb import set_trace

numbers = set("1234567890.")
operators = "+-/*^"


def evaluate(expr):
    """Base case: an expr with no parens. If parens found, recursively call on
    the contents of those parens."""
    operand_stack = []
    operator_stack = []
    cur_number = None
    num_decimals = 0
    if expr.count("(") != expr.count(")"):
        raise ValueError("Unbalanced parentheses!")
    index = 0
    while index < len(expr):
        c = expr[index]
        # isolate a paren section
        if c == "(":
            # reset reading a literal
            if cur_number is not None:
                operand_stack.append(cur_number / 10**num_decimals)
                cur_number = None
                num_decimals = 0

            start_sub_expr = index
            end_paren = index
            open_parens = 1
            # identify sub expression while also skipping it
            while open_parens > 0:
                index += 1
                cc = expr[index]
                if cc == "(":
                    open_parens += 1
                elif cc == ")":
                    open_parens -= 1
            end_paren = index
            sub_expr = expr[start_sub_expr + 1: end_paren]
            # evaulate and store the result of the sub expr
            operand_stack.append(evaluate(sub_expr))
        elif c in numbers:
            # if a number has not been started yet
            if cur_number is None:
                cur_number = 0
            # shift
            cur_number *= 10
            if c == "." or num_decimals > 0:
                num_decimals += 1
            else:
                # concatenate
                cur_number += int(c)
        elif c in operators:
            # reset reading a literal
            if cur_number is not None:
                operand_stack.append(cur_number / 10**num_decimals)
                cur_number = None
                num_decimals = 0
            operator_stack.append(c)
        index += 1
    if cur_number is not None:
        operand_stack.append(cur_number / 10**num_decimals)
        cur_number = None
        num_decimals = 0
    while not len(operator_stack) == 0:
        op = operator_stack.pop()
        try:
            a = operand_stack.pop()
            b = operand_stack.pop()
        except IndexError:
            # handle leading minus sign
            if op == "-":
                b = 0
        if op == "+":
            operand_stack.append(a + b)
        elif op == "/":
            operand_stack.append(b / a)
        elif op == "-":
            operand_stack.append(b - a)
        elif op == "*":
            operand_stack.append(b * a)
        elif op == "^":
            operand_stack.append(b**a)
    try:

        assert len(operand_stack) == 1
    except AssertionError:
        raise ValueError("Expression contains no operands!")
    return operand_stack.pop()


def prettify(result):
    if result % 1 == 0:
        return int(result)

    if result != 0:
        # check if denominator is whole number
        if (1 / result) % 1 == 0:
            return "1/{}".format(prettify(1 / result))
    return str(result)
