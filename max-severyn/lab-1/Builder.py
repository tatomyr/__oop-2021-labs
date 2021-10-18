from abc import ABCMeta, abstractmethod


class IBuilder():
    "The Builder Interface"
    @staticmethod
    @abstractmethod
    def build_part_wheels():
        "Build part wheels"

    @staticmethod
    @abstractmethod
    def build_part_doors():
        "Build part doors"

    @staticmethod
    @abstractmethod
    def build_part_windows():
        "Build part windows"

    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"


class CarBuilder(IBuilder):
    "CarBuilder"

    def __init__(self):
        self.product = Product()

    def build_part_wheels(self):
        self.product.parts.append('wheels')
        return self

    def build_part_doors(self):
        self.product.parts.append('doors')
        return self

    def build_part_windows(self):
        self.product.parts.append('windows')
        return self

    def get_result(self):
        return self.product


class Product():
    "The Product"

    def __init__(self):
        self.parts = []


class CarDirector:
    "The Director, building a complex representation."

    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return CarBuilder()\
            .build_part_wheels()\
            .build_part_doors()\
            .build_part_windows()\
            .get_result()


# The Client
Car1 = CarDirector.construct()
print(Car1.parts)
