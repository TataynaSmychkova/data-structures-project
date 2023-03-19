import pytest

from src.stack import Stack, Node


def test_push():
    stack = Stack()
    stack.push('test_data')
    node = stack.top
    assert isinstance(stack.top, Node)
    assert stack.top.data == 'test_data'
    assert stack.top.next_node is None
    stack.push('test_data_1')
    assert isinstance(stack.top.next_node, Node)
    assert stack.top.data == 'test_data_1'
    assert stack.top.next_node is node


def test_pop():
    stack = Stack()
    stack.push('data')
    node_1 = stack.top
    stack.push('data_1')
    node_2 = stack.top
    assert stack.pop() is node_2
    assert stack.pop() is node_1


def test__str__():
    stack = Stack()
    assert str(stack) == 'None'
