# Поведінкові патерни

### Тема: навчитись працювати за поведінковими патернами проектування.

**Поведінкові патерни** піклуються про ефективну комунікацію між об’єктами. Ці патерни вирішують завдання ефективної та безпечної взаємодії між об'єктами програми.

**Знімок** — це поведінковий патерн проектування, що дає змогу зберігати та відновлювати минулий стан об’єктів, не розкриваючи подробиць їхньої реалізації.
Патерн Знімок дозволяє створювати будь-яку кількість знімків об’єкта і зберігати їх незалежно від об’єкта, з якого роблять знімок. Знімки часто використовують не тільки для реалізації операції скасування, але й для транзакцій, коли стан об’єкта потрібно «відкотити», якщо операція не була вдалою. Патерн пропонує виготовити знімок саме вихідному об’єкту, тому що йому доступні всі поля, навіть приватні.
#### Приклад коду

```python
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
```
**Output**
>[Поточний стан піци: ['base']<br>
********Добавляєм інгредієнти на піцу********<br>
В піцу добавлений інгредієнт: соус<br>
В піцу добавлений інгредієнт: гриби<br>
В піцу добавлений інгредієнт: салямі<br>
В піцу добавлений інгредієнт: сир<br>
Поточний стан піци: ['base', 'соус', 'гриби', 'салямі', 'сир']<br>
****Відміняєм попередні дії****<br>
Відміна попрердньої дії<br>
Поточний стан піци: ['base', 'соус', 'гриби', 'салямі']<br>
Відміна попрердньої дії<br>
Поточний стан піци: ['base', 'соус', 'гриби']<br>
Відміна попрердньої дії<br>
Поточний стан піци: ['base', 'соус']<br>
Піца повернулася в свій початковий стан!<br>
Поточний стан піци: ['base']<br>
*****Знову добавляєм інгредієнти на піцу*****<br>
В піцу добавлений інгредієнт: соус<br>
В піцу добавлений інгредієнт: 4 сира<br>
Поточний стан піци: ['base', 'соус', '4 сира']]<br>


## Висновок
Патерн **Знімок** ефективний у використанні коли потрібно зберігати миттєві знімки стану об’єкта (або його частини) для того, щоб об’єкт можна було відновити в тому самому стані, та коли пряме отримання стану об’єкта розкриває приватні деталі його реалізації, порушуючи інкапсуляцію. Тому перевагами даного патерну є: не порушує інкапсуляцію вихідного об’єкта та спрощує структуру вихідного об’єкта, йому не потрібно зберігати історію версій свого стану. А недоліком є: вимагає багато пам’яті, якщо клієнти дуже часто створюють знімки.
