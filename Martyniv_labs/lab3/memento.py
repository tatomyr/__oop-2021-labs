from typing import List


class Memento:
    """Клас Знімок, фіксуючий поточний
    стан інгредієнтів на піці"""
    def __init__(self, state: List[str]):
        self.__state = state

    def get_state(self) -> List[str]:
        return self.__state[:]


class Pizza:
    """Клас готується шеф-кухарем піци"""
    def __init__(self):
        self.__state: List[str] = ['base']

    def add_ingredient(self, ingredient: str) -> None:
        print(f"В піцу добавлений інгредієнт: {ingredient}")
        self.__state.append(ingredient)

    def create_memento(self):
        return Memento(self.__state[:])

    def set_memento(self, memento: Memento):
        self.__state = memento.get_state()

    def __str__(self):
        return f"Поточний стан піци: {self.__state}"


class Chief:
    def __init__(self, pizza: Pizza):
        self.pizza = pizza
        self.pizza_states: List[Memento] = []

    def add_ingredient_to_pizza(self, ingredient: str):
        self.pizza_states.append(self.pizza.create_memento())
        self.pizza.add_ingredient(ingredient)


    def undo_add_ingredient(self):
        if len(self.pizza_states) == 1:
            self.pizza.set_memento(self.pizza_states[0])
            print("Піца повернулася в свій початковий стан!")
            print(self.pizza)
        else:
            print("Відміна попрердньої дії")
            state = self.pizza_states.pop()
            self.pizza.set_memento(state)
            print(self.pizza)


if __name__ == "__main__":
    pizza = Pizza()
    chief = Chief(pizza)
    print(pizza)
    print("*" * 8 + "Добавляєм інгредієнти на піцу" + 8 * "*")
    chief.add_ingredient_to_pizza('соус')
    chief.add_ingredient_to_pizza('гриби')
    chief.add_ingredient_to_pizza('салямі')
    chief.add_ingredient_to_pizza('сир')
    print(pizza)
    print("*" * 4 + "Відміняєм попередні дії" + 4 * "*")
    chief.undo_add_ingredient()
    chief.undo_add_ingredient()
    chief.undo_add_ingredient()
    chief.undo_add_ingredient()
    print("*" * 5 + "Знову добавляєм інгредієнти на піцу" + 5 * "*")
    chief.add_ingredient_to_pizza('соус')
    chief.add_ingredient_to_pizza('4 сира')
    print(pizza)