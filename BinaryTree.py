from typing import Any, Callable
from BinaryNode import BinaryNode


class BinaryTree:
    root: BinaryNode

    def __init__(self, value: Any):
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[['BinaryNode'], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[['BinaryNode'], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[['BinaryNode'], None]):
        self.root.traverse_pre_order(visit)

    def __str__(self) -> str:
        show: str = str("|- " + str(self.root.value) + '\n')
        return show + self.root.tree_node()
