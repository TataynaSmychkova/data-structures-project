import collections


class Node:
    """Класс для узла очереди"""

    def __init__(self, data: str, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data: str = data
        self.next_node: Node | None = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.tail: Node | None = None
        self.head: Node | None = None

    def enqueue(self, data: str) -> None:
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node: Node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self) -> str | None:
        """
        Метод для удаления элемента из очереди и его возвращения

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        data: str = self.head.data
        self.head = self.head.next_node
        return data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head is None:
            return ''
        data = []
        head = self.head
        while head is not None:
            data.append(head.data)
            head = head.next_node
        return '\n'.join(data)


