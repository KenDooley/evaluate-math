import sys
from postfix import evaluate_postfix, parse_expression_into_parts
from stack import Stack

PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}


def infix_parts_to_postfix(terms):
    result = []
    stack = Stack()
    for elem in terms:
        if isinstance(elem, int):
            result.append(elem)
        elif elem == '(':
            stack.push(elem)
        elif elem == ')':
            while not stack.is_empty():
                top = stack.pop()
                if top != '(':
                    result.append(top)
                else:
                    break
        elif not stack or PRECEDENCE[elem] > PRECEDENCE[stack.top()]:
            stack.push(elem)
        else:
            while stack and PRECEDENCE[elem] <= PRECEDENCE[stack.top()]:
                result.append(stack.pop())
            stack.push(elem)
    while stack:
        result.append(stack.pop())
    return result


def evaluate_infix(terms):
    return evaluate_postfix(infix_parts_to_postfix(terms))


def evaluate_infix_str(exp):
    return evaluate_infix(parse_expression_into_parts(exp))


if __name__ == "__main__":
    expr = None
    if len(sys.argv) > 1:
        expr = sys.argv[1]
        print "Evaluating Postfix expr: %s == %s" % (expr, evaluate_infix_str(expr))
    else:
        print 'Usage: python evaluate.py "<expr>" -- i.e. python evaluate.py 9 - ( 1 + 3 ) * 2'
        print "Spaces are required between every term, even parenthesis."
