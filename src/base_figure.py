class BaseFigure:
    def __init__(self, name, a=None, b=None, c=None):
        self.name = name
        self.a = a
        self.b = b
        self.c = c

    def get_error(self, formula):
        try:
            otvet = formula()
            return otvet
        except TypeError:
            print("None")

    def __add__(self, other):
        return self + other

    def get_add(self, first, other):
        return first + other
