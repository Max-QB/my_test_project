from src.base_figure import BaseFigure


class Triangle(BaseFigure):
    def get_perimeter_triangle(self):
        p_triangle = self.get_error(formula=lambda: int(self.a + self.b + self.c))
        return p_triangle

    def get_area_of_a_triangle(self):
        p = self.get_perimeter_triangle()/2
        s_triangle = self.get_error(formula=lambda: round((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5, 1))
        return s_triangle
