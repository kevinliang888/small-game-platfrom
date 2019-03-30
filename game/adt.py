"""
ADT which includes Queue and Tree.
"""
from typing import List


class Stack:
    """
     Last-in, first-out (LIFO) stack.
    """

    def __init__(self) -> None:
        """ Create a new, empty Stack self.

        >>> s = Stack()
        """
        self._contains = []

    def add(self, obj: object) -> None:
        """ Add object obj to top of Stack self.

        >>> s = Stack()
        >>> s.add(6)
        """
        self._contains.append(obj)

    def remove(self) -> object:
        """
        Remove and return top element of Stack self.

        Assume Stack self is not emp.

        >>> s = Stack()
        >>> s.add(6)
        >>> s.add(8)
        >>> s.remove()
        8
        """
        return self._contains.pop()

    def is_empty(self) -> bool:
        """
        Return whether Stack self is empty.

        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.add(6)
        >>> s.is_empty()
        False
        """
        return len(self._contains) == 0


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """
    highest_score: int
    value: object
    children: List['Tree']

    def __init__(self, value: object = None,
                 children: List['Tree'] = None) -> None:
        """
        Create Tree self with content value and 0 or more children
        """
        self.value = value
        # copy children if not None
        self.children = children.copy() if children else []


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
