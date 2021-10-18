Виконав: Махно Юрій (Іт-22Сп)




                                Тема: Структуровані шаблони
                        Мета: Вивчити принцип структурованого шаблону


Стан — це шаблон проєктування, що реалізує скінченний автомат в обʼєктно-орієнтованому програмуванні.

Він реалізується шляхом створення для кожного стану скінченного автомата класу-спадкоємця інтерфейсу (або абстрактного класу) та дозволяє об'єктові варіювати свою поведінку залежно від внутрішнього стану.
Він надає модуль для кінцевих автоматів, які реалізовані з використанням підкласів, похідних від зазначеного класу кінцевих автоматів. Методи не залежать від стану і викликають переходи, оголошені з використанням декораторів.


```python


from __future__ import annotations


class Facade:

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:

        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:

        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1:

    def operation1(self) -> str:
        return "Subsystem1: Ready!"

    def operation_n(self) -> str:
        return "Subsystem1: Go!"


class Subsystem2:

    def operation1(self) -> str:
        return "Subsystem2: Get ready!"

    def operation_z(self) -> str:
        return "Subsystem2: Fire!"


def client_code(facade: Facade) -> None:

    print(facade.operation(), end="")


if __name__ == "__main__":

    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)


```


Висновок: На цій практичній роботі я дізнався та вивчив принцип структурованого шаблону. 
Прочитав декілька документацій по даному шалону , і переглянув декілька інтернет сторінок.
В лістингу програми, задано дві системи, і  в  залежності  від якого  методу використовується буде виконано  певну дію.




