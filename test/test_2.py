from src.triangle import Triangle


def test_perimeter_square(base_figure):
    square = base_figure
    assert square.get_perimeter_square() == 20


def test_area_square(base_figure):
    square = base_figure
    assert square.get_area_square() == 25


def test_perimeter_rectangle(base_rectangle):
    rectangle = base_rectangle
    assert rectangle.get_perimeter_rectangle() == 22


def test_area_rectangle(base_rectangle):
    rectangle = base_rectangle
    assert rectangle.get_area_of_a_rectangle() == 30


def test_perimeter_triangle(base_triangle):
    triangle = base_triangle
    assert triangle.get_perimeter_triangle() == 18


def test_area_triangle(base_triangle):
    triangle = base_triangle
    assert triangle.get_area_of_a_triangle() == 14.7


def test_circumference(base_circle):
    circle = base_circle
    assert circle.get_circumference() == 31


def test_area_circle(base_circle):
    circle = base_circle
    assert circle.get_area_of_a_circle() == 15


def test_error_attribute():
    figure = Triangle(name="triangle", a=5)
    assert figure.get_perimeter_triangle() is None


def test_sum_area(base_figure, base_triangle):
    square = base_figure
    triangle = base_triangle
    assert square.get_area_square() + triangle.get_area_of_a_triangle() == square.get_add(
        first=square.get_area_square(),
        other=triangle.get_area_of_a_triangle()
    )
