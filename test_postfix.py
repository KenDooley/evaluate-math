from postfix import parse_expression_into_parts, evaluate_postfix

EXPR = "9 - ( 1 + 3 ) * 2"
INFIX_PARTS = [9, '-', '(', 1, '+', 3, ')', '*', 2]
POSTFIX_PARTS = [9, 1, 3, '+', 2, '*', '-']


def test_parse_expression_into_parts():
    assert parse_expression_into_parts(EXPR) == INFIX_PARTS


def test_evaluate_postfix():
    assert evaluate_postfix(POSTFIX_PARTS) == 1
