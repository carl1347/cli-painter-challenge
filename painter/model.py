# TODO: Add code here
import matplotlib.pyplot as plt
import pickle
class point:
    def __init__(self, x: float, y: float ):
        self.x: float = x
        self.y: float = y

        class circle:
            def __init__(self, center: point, radius: float):
                self.center: point = center
                self.radius: float = radius

            def area(self) -> float:



                return 3.14159 * self.radius ** 2

            def draw(self):
                circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
                plt.gca().add_patch(circle)
                plt.axis("scaled")
                plt.show()

            def __str__(self):
                return f"Circle with center at (x, y) and radius r"

class triangle:
    def __init__(self, point_1: point, point_2: point, point_3: point):
        self.point_1: point = point_1
        self.point_2: point = point_2
        self.point_3: point = point_3
    def area(self):

        a = self.point_1(self.point_1, self.point_2)
        b = self.point_2(self.point_2, self.point_3)
        c = self.point_3(self.point_3, self.point_1)
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
    def draw(self):
        x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]
        y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]
        plt.fill(x, y, color='b')
        plt.axis("scaled")
        plt.show()
    def __str__(self):
        return f"Triangle with vertices at (x1, y1), (x2, y2) and (x3, y3)"

class rectangle:
    def __init__(self, point_1: point, point_2: point):
        self.point_1: point = point_1
        self.point_2: point = point_2
    def area(self):

      width = abs(self.point_1.x - self.point_2.x)
      height = abs(self.point_1.y - self.point_2.y)
      return width * height
    def draw(self):
      x = [self.point_1.x, self.point_2.x, self.point_2.x, self.point_1.x, self.point_1.x]
      y = [self.point_1.y, self.point_1.y, self.point_2.y, self.point_2.y, self.point_1.y]
      plt.fill(x, y, color='g')
      plt.axis("scaled")
      plt.show()
    def __str__(self):
        return f"Rectangle with opposite vertices at (x1, y1) and (x2, y2)"


class Painter:
    FILE = ".painter"

    def __init__(self) -> None:
        self.shapes: list = []
        self._load()

    def _load(self) -> None:
        try:
            with open(Painter.FILE, "rb") as f:
                self.shapes = pickle.load(f)
        except (EOFError, FileNotFoundError):
            self.shapes = []

    def _save(self) -> None:
        with open(Painter.FILE, "wb") as f:
            pickle.dump(self.shapes, f)

    def add_shape(self, shape) -> None:
        self.shapes.append(shape)
        self._save()

    def total_area(self) -> float:
        return sum(shape.area() for shape in self.shapes)

    def clear(self) -> None:
        self.shapes = []
        self._save()












