from evaluate import parse_expression_into_parts, infix_parts_to_postfix, evaluate_infix, \
    evaluate_infix_str


EXPR = "9 - ( 1 + 3 ) * 2"
INFIX_PARTS = [9, '-', '(', 1, '+', 3, ')', '*', 2]
POSTFIX_PARTS = [9, 1, 3, '+', 2, '*', '-']


def test_infix_parts_to_postfix():
    assert infix_parts_to_postfix(INFIX_PARTS) == POSTFIX_PARTS


def test_evaluate_order_operations():
    parsed_parts = parse_expression_into_parts('2 + 4 * 3')
    assert infix_parts_to_postfix(parsed_parts) == [2, 4, 3, '*', '+']
    assert evaluate_infix(parsed_parts) == 14


def test_evaluate_parens():
    parsed_parts = parse_expression_into_parts('4 * ( 3 + 2 )')
    assert infix_parts_to_postfix(parsed_parts) == [4, 3, 2, '+', '*']
    assert evaluate_infix(parsed_parts) == 20


def test_evaluate_infix_str():
    fancy7 = '12 - 3 * ( 2 + 4 / 2 ) + 7'
    assert infix_parts_to_postfix(parse_expression_into_parts(fancy7)) \
        == [12, 3, 2, 4, 2, '/', '+', '*', '-', 7, '+']
    assert evaluate_infix_str(fancy7) == 7
    assert evaluate_infix_str('1 - ( 3 + 2 ) + 6 * 3') == 14
