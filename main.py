from typing import List
from BinaryTree import BinaryTree
from BinaryNode import BinaryNode


def visited(Node: 'BinaryNode') -> None:
    print(Node)


def path_finder(node: 'BinaryNode', path: List['BinaryNode'], paths: List[List['BinaryNode']]):
    path.append(node.value)
    if node.left_child is None and node.right_child is None:
        paths.append(path.copy())
    if node.left_child:
        path_finder(node.left_child, path, paths)
    if node.right_child:
        path_finder(node.right_child, path, paths)
    path.pop()


def all_paths(tree: 'BinaryTree') -> List[List['BinaryNode']]:
    path: List['BinaryNode'] = []
    paths: List[List['BinaryNode']] = []
    path_finder(tree.root, path, paths)
    return paths


if __name__ == '__main__':
    tree = BinaryTree(10)
    tree.root.add_left_child(9)
    tree.root.add_right_child(2)
    tree.root.left_child.add_left_child(1)
    tree.root.left_child.add_right_child(3)
    tree.root.right_child.add_left_child(4)
    tree.root.right_child.add_right_child(6)
    # print(tree)
    # print("\n")

    assert tree.root.value == 10

    assert tree.root.right_child.value == 2
    assert tree.root.right_child.is_leaf() is False

    assert tree.root.left_child.left_child.value == 1
    assert tree.root.left_child.left_child.is_leaf() is True

    # tree.root.traverse_in_order(visited)
    # print("\n")
    # tree.root.traverse_post_order(visited)
    # print("\n")
    # tree.root.traverse_pre_order(visited)
    # print("\n")

    project_tree = BinaryTree(1)
    project_tree.root.add_left_child(2)
    project_tree.root.add_right_child(3)
    project_tree.root.right_child.add_right_child(7)
    project_tree.root.left_child.add_left_child(4)
    project_tree.root.left_child.add_right_child(5)
    project_tree.root.left_child.left_child.add_left_child(8)
    project_tree.root.left_child.left_child.add_right_child(9)
    # print(project_tree)
    print(all_paths(project_tree))
