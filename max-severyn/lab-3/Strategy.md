
# Шаблони проектування. Поведінкові шаблони

## Мета

Освоїти роботу з поведінковими шаблонами в Python3.

## Поведінкові шаблони

 Поведінкові шаблони вирішують завдання ефективної та безпечної взаємодії між об'єктами програми. Поведінкові шаблони пов’язані з розподілом обов’язків між об’єктами. Їх відмінність від структурних шаблонів полягає в тому, що вони не просто описують структуру, але також описують шаблони для передачі повідомлень / зв’язку між ними. Або, іншими словами, вони допомагають відповісти на питання “Як запустити поведінку в програмному компоненті”?

## Шаблон стратегія (Strategy)

Стратегія — це поведінковий патерн проектування, який визначає сімейство схожих алгоритмів і розміщує кожен з них у власному класі. Після цього алгоритми можна заміняти один на інший прямо під час виконання програми.

## Приклад коду

```python

from abc import ABCMeta, abstractmethod


class GameCharacter():
    "This is the context whose strategy will change"

    position = [0, 0]

    @classmethod
    def move(cls, movement_style):
        "The movement algorithm has been decided by the client"
        movement_style(cls.position)


class IMove(metaclass=ABCMeta):
    "A Concrete Strategy Interface"

    @staticmethod
    @abstractmethod
    def __call__():
        "Implementors must select the default method"


class Walking(IMove):
    "A Concrete Strategy Subclass"

    @staticmethod
    def walk(position):
        "A walk algorithm"
        position[0] += 1
        print(f"I am Walking. New position = {position}")

    __call__ = walk


class Running(IMove):
    "A Concrete Strategy Subclass"

    @staticmethod
    def run(position):
        "A run algorithm"
        position[0] += 2
        print(f"I am Running. New position = {position}")

    __call__ = run


class Crawling(IMove):
    "A Concrete Strategy Subclass"

    @staticmethod
    def crawl(position):
        "A crawl algorithm"
        position[0] += 0.5
        print(f"I am Crawling. New position = {position}")

    __call__ = crawl


# The Client
GAME_CHARACTER = GameCharacter()
GAME_CHARACTER.move(Walking())
# Character sees the enemy
GAME_CHARACTER.move(Running())
# Character finds a small cave to hide in
GAME_CHARACTER.move(Crawling())


```

## Вивід
>I am Walking. New position = [1, 0] </br>
>I am Running. New position = [3, 0] </br>
>I am Crawling. New position = [3.5, 0] 

## UML-діаграма 

![builder_diagram](../images/strategy_example.jpg)

## Висновок

Стратегія дозволяє варіювати поведінку об’єкта під час виконання програми, підставляючи до нього різні об’єкти-поведінки (наприклад, що відрізняються балансом швидкості та споживання ресурсів). Стратегія дозволяє ізолювати код, дані й залежності алгоритмів від інших об’єктів, приховавши ці деталі всередині класів-стратегій. Також стратегія дозволяє відокремити поведінку, що відрізняється, у власну ієрархію класів, а потім звести початкові класи до одного, налаштовуючи його поведінку стратегіями.
#### Переваги
* Гаряча динамічна заміна алгоритмів.
* Ізолює код і дані алгоритмів від інших класів.
* Заміна спадкування делегуванням.
* Реалізує принцип відкритості/закритості.
#### Недоліки
* Ускладнює програму внаслідок додаткових класів.
* Клієнт повинен знати, в чому полягає різниця між стратегіями, щоб вибрати потрібну.

## Список використаної літератури

* [Python Design Patterns](https://sbcode.net/python)
* [Refactoring Guru](https://refactoring.guru/uk/design-patterns/python)
* [Metanit.com](https://metanit.com)
