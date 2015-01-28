from stack import Stack


def test_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert len(stack) == 3
    assert not stack.is_empty()

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1

    assert stack.is_empty()


def test_top():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.top() == 3
    assert stack.top() == 3
    stack.push(4)
    assert stack.top() == 4
    stack.pop()
    assert stack.top() == 3
    stack.pop()
    assert stack.top() == 2
    stack.pop()
    assert stack.top() == 1
    stack.pop()
    assert stack.top() is None

