#!/usr/bin/env python3


class Fish():
    """
    Represents a fish that can swim and has a water habitat.
    """
    def swim(self):
        """
        Print a message indicating the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print a message indicating the fish's habitat is water.
        """
        print("The fish lives in water")


class Bird():
    """
    Represents a bird that can fly and has a sky habitat.
    """
    def fly(self):
        """
        Print a message indicating the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print a message indicating the bird's habitat is the sky.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a flying fish, inheriting from both Fish and Bird.
    Can swim, fly, and has a dual habitat.
    """
    def swim(self):
        """
        Print a message indicating the flying fish is swimming.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Print a message indicating the flying fish is soaring.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Print a message indicating the flying fish's dual habitat.
        """
        print("The flying fish lives both in water and the sky!")
