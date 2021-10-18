# Шаблони проєктування. Породжуючий патерн

## Мета

Навчитися працювати за породжуючими шаблонами в Python.

# Породжуючі шаблони

Породжуючі патерни піклуються про гнучке створення об’єктів без внесення в програму зайвих залежностей. Основним завданням таких
патернів є спростити створення об’єктів, які необхідні аплікації.

# Шаблон Singleton (Одинак)

Синглтон забезпечує існування єдиного екземпляру класу та єдиного доступу до нього. Тобто в системі має
існувати лише один екземпляр класу, до якого легко получити доступ з любої точки коду.

#Приклад коду

```python

class SingletonBaseClass(type):
    _instances = {}

    def __call__(cls):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonBaseClass, cls).\
                __call__()
        return cls._instances[cls]


class MySingleton(metaclass=SingletonBaseClass):
    def __init__(self):
        self.name = "Singleton"
        self.value_a = 3
        self.value_b = 5

    def add_a_b(self) -> int:
        return self.value_a+self.value_b

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name


if __name__ == "__main__":
    my_singleton1 = MySingleton()
    my_singleton2 = MySingleton()
    print("Singleton1 name: " + my_singleton1.get_name())
    my_singleton1.set_name("New Singleton")
    print("Singleton2 name: " + my_singleton2.get_name())
    print(my_singleton1)
    print(my_singleton2)
    print(id(my_singleton1) == id(my_singleton2))
```
## Вивід
>Singleton1 name: Singleton
>Singleton2 name: New Singleton
><__main__.MySingleton object at 0x000001E414863CD0>
><__main__.MySingleton object at 0x000001E414863CD0>
True

#UML - діаграма
![Singleton](Singleton.png)

## Висновки

Для деяких класів важливо, щоб існував тільки один екземпляр. Наприклад, хоча у системі може існувати декілька принтерів, може бути тільки один спулер. Повинна бути тільки одна файлова система та тільки один активний віконний менеджер.
Глобальна змінна не вирішує такої проблеми, бо не забороняє створити інші екземпляри класу.
Рішення полягає в тому, щоб сам клас контролював свою «унікальність», забороняючи створення нових екземплярів, та сам забезпечував єдину точку доступу. Це є призначенням шаблону Одинак.

####Переваги
-Singleton дозволяє звурнутизя із любої точки коду звернутися до його єдиного екземпляру
-Створення екземпляру проходить по принципу відложеної ініціалізації
####Недоліки
-Бездумне використання патерна Singleton може привести до поганого дизайну архітектури
