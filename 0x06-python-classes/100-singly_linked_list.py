#!/usr/bin/python3
"""
Module: 100-singly_linked_list

Description:
    Contains the definition of the Node and SinglyLinkedList classes.

Classes:
    Node
    SinglyLinkedList
"""


class Node:
    """
    Node class represents a node of a singly linked list.

    Attributes:
        __data (int): Private instance attribute representing the data of
                      the node.
        __next_node (Node): Private instance attribute representing the
                            next node in the linked list.

    Methods:
        __init__(self, data, next_node=None): Initializes a new Node
                                              instance.
        data(self): Getter method to retrieve the data of the node.
        data(self, value): Setter method to set the data of the node.
        next_node(self): Getter method to retrieve the next node.
        next_node(self, value): Setter method to set the next node.

    Raises:
        TypeError: If data is not an integer or if next_node is not None
                   or a Node.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Args:
            data (int): The data for the node.
            next_node (Node): The next node in the linked list
                              (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve the data of the node.

        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data of the node.

        Args:
            value (int): The data to set for the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve the next node.

        Returns:
            Node: The next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next node.

        Args:
            value (Node): The next node to set.

        Raises:
            TypeError: If value is not None or a Node.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class represents a singly linked list.

    Attributes:
        __head: Private instance attribute representing the head of the list.

    Methods:
        __init__(self): Initializes a new SinglyLinkedList instance.
        sorted_insert(self, value): Inserts a new Node into the correct sorted
                                   position in the list (increasing order).
        __str__(self): Returns a string representation of the linked list.

    Raises:
        TypeError: If value passed to sorted_insert is not an integer.
    """

    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list
        (increasing order).

        Args:
            value (int): The value to insert into the list.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")

        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string representation of the linked list.
        """
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip("\n")
