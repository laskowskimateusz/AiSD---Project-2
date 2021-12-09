from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any):
        self.left_child = None
        self.right_child = None
        self.value = value

    def is_leaf(self):
        return False if self.left_child is None and self.right_child is None else True

    def add_left_child(self, value: Any) -> None:
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[['BinaryNode'], None]) -> None:
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[['BinaryNode'], None]) -> None:
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[['BinaryNode'], None]) -> None:
        visit(self)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.right_child.traverse_pre_order(visit)

    def tree_node(self, deep: int = 1):
        result: str = str()
        if self.left_child:
            for j in range(0, deep):
                result += '    '
            result += '|- ' + str(self.left_child.value) + '\n'
            tmp = self.left_child.tree_node(deep+1)
            if type(tmp) == str:
                result += tmp
        if self.right_child:
            for j in range(0, deep):
                result += '    '
            result += '|- ' + str(self.right_child.value) + '\n'
            tmp = self.right_child.tree_node(deep+1)
            if type(tmp) == str:
                result += tmp
        if self.left_child or self.right_child:
            return result

    def __str__(self) -> str:
        return str(self.value)
