import pytest
from src.queue import Node, Queue


def test__str__():
    assert str(Queue()) == ''
    queue = Queue()
    queue.enqueue(data='testdata1')
    queue.enqueue(data='testdata2')
    assert str(queue) == 'testdata1\ntestdata2'


def test_enqueue():
    queue = Queue()
    queue.enqueue(data='data1')
    assert queue.head.data == 'data1'
    queue.enqueue(data='data2')
    assert queue.head.next_node.data == 'data2'
    queue.enqueue(data='data3')
    assert queue.tail.data == 'data3'
    assert queue.tail.next_node is None


def test_dequeue():
    queue = Queue()
    assert queue.dequeue() is None
    queue.enqueue(data='testdata1')
    queue.enqueue(data='testdata2')
    assert queue.dequeue() == 'testdata1'
    assert queue.dequeue() == 'testdata2'
