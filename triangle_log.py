import logging

logging.basicConfig(filename='triangle.log',
                    level=logging.ERROR,
                    format='%(asctime)s [%(levelname)s] - %(message)s')


class InvalidTriangleError(Exception):
    """Exception thrown when trying to create a triangle
    with invalid sides."""
    def __init__(self, message="Треугольник с данными сторонами не существует"):
        self.message = message
        super().__init__(self.message)


class TriangleTypeNotFoundError(Exception):
    """Exception thrown when trying to classify a triangle,
    which cannot be classified."""
    def __init__(self, message="Невозможно классифицировать треугольник"):
        self.message = message
        super().__init__(self.message)


class Triangle:
    """A class that represents a triangle."""
    def __init__(self, a: int, b: int, c: int):
        try:
            if ((a <= 0 or b <= 0 or c <= 0)
               or (a >= b + c or b >= a + c or c >= a + b)):
                raise InvalidTriangleError()
            self.side_a = a
            self.side_b = b
            self.side_c = c
        except InvalidTriangleError as e:
            logging.error("InvalidTriangleError: %s", e)

    def classify_triangle(self):
        """The method checks for the existence of a triangle and determines
        its type (equilateral, isosceles, or scalene),
        and then returns the appropriate description."""
        try:
            if self.side_a == self.side_b == self.side_c:
                return "Равносторонний треугольник"
            elif (self.side_a == self.side_b or self.side_b == self.side_c
                  or self.side_a == self.side_c):
                return "Равнобедренный треугольник"
            else:
                return "Разносторонний треугольник"
        except Exception as e:
            logging.error("Ошибка в classify_triangle: %s", e)


try:
    side_a = int(input("Введите длину стороны a: "))
    side_b = int(input("Введите длину стороны b: "))
    side_c = int(input("Введите длину стороны c: "))

    triangle = Triangle(side_a, side_b, side_c)
    classification = triangle.classify_triangle()
    print(classification)
except InvalidTriangleError as e:
    print(f"Ошибка: {e}")
except TriangleTypeNotFoundError as e:
    print(f"Ошибка: {e}")
except ValueError:
    print("Ошибка: Введите корректные значения для сторон треугольника\
          (целые числа больше нуля).")
    logging.error("Ошибка ValueError произошла при вводе сторон треугольника.")
except Exception as e:
    print(f"Необработанная ошибка: {e}")
    logging.error("Необработанная ошибка: %s", e)
