from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):
    name = "Triangle"

    def noofsides(self):
        print(f"I am a {self.name} and I have 3 sides")


class Pentagon(Polygon):
    name = "Pentagon"

    def noofsides(self):
        print(f"I am a {self.name} and I have 5 sides")


class Hexagon(Polygon):
    name = "Hexagon"

    def noofsides(self):
        print(f"I am a {self.name} and I have 6 sides")


class Quadrilateral(Polygon):
    name = "Quadrilateral"

    def noofsides(self):
        print(f"I am a {self.name} and I have 4 sides")


class Rectangle(Polygon):
    name = "Rectangle"

    def noofsides(self):
        print(f"I am a {self.name} and I have 4 sides")


# Example usage:
R = Triangle()
R.noofsides()  # Output: "I have 3 sides"
K = Quadrilateral()
K.noofsides()  # Output: "I have 4 sides"
R = Pentagon()
R.noofsides()  # Output: "I have 5 sides"
K = Hexagon()
K.noofsides()  # Output: "I have 6 sides"
R = Rectangle()
R.noofsides()  # Output: "I have 4 sides"
