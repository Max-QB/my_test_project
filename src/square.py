from src.base_figure import BaseFigure


class Square(BaseFigure):
    def get_perimeter_square(self):
        p_square = self.get_error(formula=lambda: self.a * 4)
        return p_square

    def get_area_square(self):
        s_square = self.get_error(formula=lambda: self.a ** 2)
        return s_square
