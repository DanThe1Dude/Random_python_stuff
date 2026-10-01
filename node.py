from typing import Any


class Node:
    def __init__(self, val: Any) -> None:
        self.val = val
        self.next: Node | None = None

    def set_next(self, node: "Node | None") -> None:
        self.next = node

    def __repr__(self) -> str:
        return self.val
