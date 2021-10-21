import math

from src.base_figure import BaseFigure


class Circle(BaseFigure):
    def get_circumference(self):
        p_circle = self.get_error(formula=lambda: int(2 * self.a * math.pi))
        return p_circle

    def get_area_of_a_circle(self):
        s_circle = self.get_error(formula=lambda: int(self.a * math.pi))
        return s_circle
