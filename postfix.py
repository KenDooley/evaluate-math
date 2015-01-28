import sys
from stack import Stack


def parse_expression_into_parts(expression):
    """
    Parse expression into list of parts
    :rtype : list
    :param expression: str # i.e. "2 * 3 + ( 2 - 3 )"
    """
    raise NotImplementedError("complete me!")


def evaluate_expression(a, b, op):
    raise NotImplementedError("complete me!")


def evaluate_postfix(parts):
    raise NotImplementedError("complete me!")


if __name__ == "__main__":
    expr = None
    if len(sys.argv) > 1:
        expr = sys.argv[1]
        parts = parse_expression_into_parts(expr)
        print "Evaluating %s == %s" % (expr, evaluate_postfix(parts))
    else:
        print 'Usage: python postfix.py "<expr>" -- i.e. python postfix.py "9 1 3 + 2 * -"'
        print "Spaces are required between every term."
