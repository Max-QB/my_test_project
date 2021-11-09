from src.base_figure import BaseFigure


class Rectangle(BaseFigure):
    def get_perimeter_rectangle(self):
        p_rectangle = self.get_error(formula=lambda: int((self.a + self.b) * 2))
        return p_rectangle

    def get_area_of_a_rectangle(self):
        s_rectangle = self.get_error(formula=lambda:  int(self.a * self.b))
        return s_rectangle
