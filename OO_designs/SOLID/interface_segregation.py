"""
deal with disadvantages of implementing big interface
"""


class IShape:
    def draw_square(self):
        raise NotImplementedError

    def draw_rectangle(self):
        raise NotImplementedError

    def draw_circle(self):
        raise NotImplementedError


"""
if you use this interface, subclasses must define all methods 
"""


class Circle(IShape):
    def draw_circle(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_square(self):
        pass


"""
if we add another method to the IShape interface => the classes must implement the new method or error will
be thrown
"""

