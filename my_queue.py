from typing import Any

from node import Node


class Queue:
    def add_to_head(self, node: Node) -> None:
        node.set_next(self.head)
        self.head = node

    def add_to_tail(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            return
        last_node = self.head
        for current_node in self:
            last_node = current_node
        last_node.set_next(node)

    def pop_head(self) -> None | Any:
        if self.head is None:
            return None
        result = self.head.val
        tmp = self.head.next
        self.head.next = None
        self.head = tmp
        return result


    def __init__(self) -> None:
        self.head: Node | None = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
