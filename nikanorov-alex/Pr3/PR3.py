from abc import ABC, abstractmethod
from typing import List


class ICommand(ABC):
    """Інтерфейсний клас для виконуваних операцій"""
    @abstractmethod
    def execute(self) -> None:
        ...


class ChiefAssistant:
    def prepare_pizza_dough(self):
        print("Асистент готує тісто для піци")

    def prepare_topping(self):
        print("Асистент нарізає начинку для піци")


class Stove:
    def prepare_stove(self):
        print("Піч розігрівається")

    def cooking_pizza(self):
        print("Піца готується в печі")


class ChiefCooker:
    def make_pizza_base(self):
        print("Шеф розгортає основу для піци")

    def add_topping_to_pizza(self):
        print("Шеф додає начинку на піцу")


class PrepareStoveCommand(ICommand):
    """Клас команди для розігріву печі"""
    def __init__(self, executor: Stove):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_stove()


class PrepareDoughCommand(ICommand):
    """Класс для підготовки тіста для піцци"""
    def __init__(self, executor: ChiefAssistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_pizza_dough()


class PrepareToppingCommand(ICommand):
    """Клас команди для нарізки начинки піци"""
    def __init__(self, executor: ChiefAssistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_topping()


class CookingPizzaCommand(ICommand):
    """Клас команди для приготування піци в печі"""
    def __init__(self, executor: Stove):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.cooking_pizza()


class MakePizzaBaseCommand(ICommand):
    """Клас команди для приготування основи для піци"""
    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.make_pizza_base()


class AddToppingCommand(ICommand):
    """Клас команди для додавання начинки на піцу"""

    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.add_topping_to_pizza()


class Pizzeria:
    """Клас агрегації всіх команд для приготування піци пиццы"""
    def __init__(self):
        self.history: List[ICommand] = []

    def addCommand(self, command: ICommand) -> None:
        self.history.append(command)

    def cook(self) -> None:
        if not self.history:
            print("Не задана черговість виконання"
                  "Команд приготування піци")
        else:
            for executor in self.history:
                executor.execute()
        self.history.clear()


if __name__ == "__main__":
    chief = ChiefCooker()
    assistant = ChiefAssistant()
    stove = Stove()
    pizzeria = Pizzeria()
    # формируем последовательность команд для приготовления пиццы
    pizzeria.addCommand(PrepareDoughCommand(assistant))
    pizzeria.addCommand(MakePizzaBaseCommand(chief))
    pizzeria.addCommand(PrepareStoveCommand(stove))
    pizzeria.addCommand(PrepareToppingCommand(assistant))
    pizzeria.addCommand(AddToppingCommand(chief))
    pizzeria.addCommand(CookingPizzaCommand(stove))
    # запускаем процесс приготовления пиццы
    pizzeria.cook()