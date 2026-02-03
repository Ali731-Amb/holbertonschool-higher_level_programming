#!/usr/bin/env python3



class CountedIterator():
    """
    An iterator that counts the number of items iterated over.
    """
    def __init__(self, argument):
        """
        Initialize the CountedIterator with an iterable argument.
        Args:
        argument (iterable): The iterable to wrap.
        """
        self.mon_iterateur = iter(argument)
        self.compteur = 0

    def __next__(self):
        """
        Return the next item from the iterator and increment the count.
        Returns:
        The next item from the wrapped iterator.
        Raises:
        StopIteration: If there are no more items.
        """
        item = next(self.mon_iterateur)
        self.compteur += 1
        return item

    def get_count(self):
        """
        Return the number of items that have been iterated over so far.
        Returns:
        int: The count of iterated items.
        """
        return self.compteur
