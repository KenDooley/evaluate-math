import sys
from stack import Stack


def parse_expression_into_parts(expression):
    """
    Parse expression into list of parts
    :rtype : list
    :param expression: str # i.e. "2 * 3 + ( 2 - 3 )"
    """
    return [int(x) if x.isdigit() else x for x in expression.split(' ')]


def evaluate_expression(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        raise Exception("Invalid operator" % op)


def evaluate_postfix(parts):
    stack = Stack()
    for part in parts:
        if isinstance(part, int):
            stack.push(part)
        else:
            right = stack.pop()
            left = stack.pop()
            stack.push(evaluate_expression(left, right, part))

    if len(stack) == 1:
        return stack.pop()
    else:
        raise ArithmeticError("Illegal expression")


if __name__ == "__main__":
    expr = None
    if len(sys.argv) > 1:
        expr = sys.argv[1]
        parts = parse_expression_into_parts(expr)
        print "Evaluating %s == %s" % (expr, evaluate_postfix(parts))
    else:
        print 'Usage: python postfix.py "<expr>" -- i.e. python postfix.py "9 1 3 + 2 * -"'
        print "Spaces are required between every term."
