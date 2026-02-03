#!/usr/bin/python3
from abc import ABC, abstractmethod


class VerboseList(list):
    def append(self, item):
        """
        Add an item to the end of the list and print a message.
        Args:
            item: The item to be added.
        """
        super().append(item)
        print(f"Added [{item}] to the list")

    def extend(self, iterable):
        """
        Extend the list by appending elements from the iterable and print a message.
        Args:
            iterable: An iterable with items to add.
        """
        lenght = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{lenght}] items")

    def remove(self, item):
        """
        Remove the first occurrence of item from the list and print a message.
        Args:
            item: The item to be removed.
        """
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)


    def pop(self, index=-1):
        """
        Remove and return item at index (default last).
        Prints a message about the operation.
        Args:
            index (int, optional): The index of the item to remove. Defaults to -1.
        Returns:
            The item removed from the list.
        Raises:
            IndexError: If index is out of range.
        """
        if index < len(self) and index >= -len(self):
            i = self[index]
            print(f"Popped [{i}] from the list.")
            return super().pop(index)
        else:
            print("Index out of range: cannot remove item.")
            raise IndexError("pop index out of range")
