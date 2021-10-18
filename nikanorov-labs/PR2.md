# Шаблони проєктування. Структурний патерн

## Мета

Навчитися працювати за структурними шаблонами в Python.

# Структурні шаблони

Структурні шаблони — шаблони проєктування, у яких розглядається питання про те, як із класів та об'єктів утворюються 
більші за розмірами структури. Структурні шаблони рівня класу використовують успадкування для утворення композицій із інтерфейсів та реалізацій.Структурні шалони 
рівня об'єкта компонують об'єкти для отримання нової функціональності. Додаткова гнучкість у цьому разі пов'язана з можливістю змінювати композицію об'єктів під час 
виконання, що є неприпустимим для статичної композиції класів.

# Шаблон Adapter 

Адаптер (Adapter) – надає можливість користуватися об’єктом, який не є прийнятним у нашій системі і який не можна змінити. Ми адаптуємо його функціональність 
через інший, відомий нашій системі, інтерфейс;

#Приклад коду

```python
from abc import ABC, abstractmethod


class IOven(ABC):
    """Вихідний інтерфейс плити,
    де одиниця виміру температури - F"""
    @abstractmethod
    def get_temperature(self) -> float:
        pass

    @abstractmethod
    def set_temperature(self, t: float) -> None:
        pass


class ICelsiusOven(ABC):
    """Інтерфейс плити з яким будемо здійснювати
    роботу в рамках розроблюваної системи,
    де одиниця виміру температури - C"""
    @abstractmethod
    def get_celsius_temperature(self) -> float:
        pass

    @abstractmethod
    def set_celsius_temperature(self, t: float) -> None:
        pass

    @abstractmethod
    def get_original_temperature(self) -> float:
        pass


class OriginalOven(IOven):
    """Клас кухонної плити, який адаптується"""
    def __init__(self, t: float):
        assert t >= 32 
        self.temperature = t

    def set_temperature(self, t: float) -> None:
        assert t >= 32
        self.temperature = t

    def get_temperature(self) -> float:
        return self.temperature


class OvenAdapter(ICelsiusOven):
    """Адаптер, що дозволяє працювати з плитою, де
     одиниця виміру температури Фаренгейта в
     градусах цельсія"""
    CELSIUS_TO_FAHRENHEIT: float = 9.0/5.0
    FAHRENHEIT_TO_CELSIUS: float = 5.0/9.0
    FAHRENHEIT_ZERO: float = 32.0

    def __init__(self, original_stove: IOven):
        self.stove = original_stove
        self.temperature = self._init_temperature()

    def get_original_temperature(self) -> float:
        return self.stove.get_temperature()

    def _init_temperature(self) -> float:
        return (OvenAdapter.FAHRENHEIT_TO_CELSIUS *
                (self.stove.get_temperature() -
                 OvenAdapter.FAHRENHEIT_ZERO))

    def get_celsius_temperature(self) -> float:
        return self.temperature

    def set_celsius_temperature(self, t: float) -> None:

        new_temperature_stove = (OvenAdapter.CELSIUS_TO_FAHRENHEIT * t +
                                 OvenAdapter.FAHRENHEIT_ZERO)
        self.stove.set_temperature(new_temperature_stove)
        self.temperature = t

if __name__ == "__main__":
    def print_temperature(stove: ICelsiusOven):
        print(f"Original temperature = {stove.get_original_temperature()}"
              f" F")
        print(f"Celsius temperature = {stove.get_celsius_temperature()}")

    fahrenheit_stove = OriginalOven(32)
    celsius_stove = OvenAdapter(fahrenheit_stove)
    print_temperature(celsius_stove)
    celsius_stove.set_celsius_temperature(180)
    print("----------------")
    print("New temperature")
    print("----------------")
    print_temperature(celsius_stove)
```
#Вивід
>Original temperature = 32 F
>Celsius temperature = 0.0
>----------------
>New temperature
>----------------
>Original temperature = 356.0 F
>Celsius temperature = 180


## UML-діаграма 

![Adapter](Adapter.jpg)

## Висновок

Адаптер надає можливість користуватися об’єктом, який не є прийнятним у нашій системі і який не можна змінити. Ми адаптуємо його функціональність 
через інший, відомий нашій системі, інтерфейс.

#### Переваги
- Відокремлює та приховує від клієнта подробиці перетворення різних інтерфейсів.
#### Недоліки
- Ускладнює код програми внаслідок введення додаткових класів.
