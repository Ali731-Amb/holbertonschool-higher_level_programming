#!/usr/bin/env python3


class SwimMixin:
    """
    Mixin class that adds swimming ability to a creature.
    """
    def swim(self):
        """
        Print a message indicating the creature swims.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that adds flying ability to a creature.
    """
    def fly(self):
        """
        Print a message indicating the creature flies.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Represents a dragon that can swim, fly, and roar.
    Inherits swimming and flying abilities from mixins.
    """
    def roar(self):
        """
        Print a message indicating the dragon roars.
        """
        print("The dragon roars!")


draco = Dragon()
draco.swim()
draco.fly()
draco.roar()
