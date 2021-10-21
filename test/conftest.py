import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.fixture
def base_figure():
    square = Square(name="square", a=5)
    yield square
    del square


@pytest.fixture
def base_circle():
    circle = Circle(name="circle", a=5)
    yield circle
    del circle


@pytest.fixture
def base_rectangle():
    rectangle = Rectangle(name="rectangle", a=5, b=6)
    yield rectangle
    del rectangle


@pytest.fixture
def base_triangle():
    triangle = Triangle(name="triangle", a=5, b=6, c=7)
    yield triangle
    del triangle


