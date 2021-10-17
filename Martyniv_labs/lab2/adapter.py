import sqlite3

__connection = None


# функція підключення до таблиці
def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect("agro.db")
    return __connection


# ініціалізація таблиці
def init_db():
    connect = get_connection()
    curs = connect.cursor()

    curs.execute("""
        CREATE TABLE IF NOT EXISTS users(
            name    TEXT NOT NULL,
            email       TEXT NOT NULL,
            price    REAL NOT NULL,
            age     INTEGER NOT NULL
            );
        """)

    connect.commit()


class CreateSQLUser:

   def __init__(self, name, email, price, age):
      self.name = name
      self.email = email
      self.price = price
      self.age = age

   # функція запису в таблицю
   def setUser(self):
      connect = get_connection()
      curs = connect.cursor()
      print("--------------------------\n"
               "Підключення успішне")
      curs.execute(
            'INSERT INTO users (name, email, price, age) VALUES (?,?,?,?)',
            (self.name, self.email, self.price, self.age))
      connect.commit()
      print("Дані додано успішно\n"
               "--------------------------")

   @staticmethod
   def reg():
      print("--------------------------\n"
            "       РЕЄСТРАЦІЯ          ")
      name = input("Введіть Name:")
      email = input("Введіть Email:")
      price = input("Введіть Price:")
      age = input("Введіть Age:")

      try:
         new_user = CreateSQLUser(name, email, price, age)
         CreateSQLUser.setUser(new_user)

      except sqlite3.Error as error:
         print("Помилка при роботі з БД", error)


class View:

    def get_tuple(self):
        connect = get_connection()
        curs = connect.cursor()
        curs.execute('SELECT * FROM users')
        data = curs.fetchall()
        for row in data:
            print(row)
        return data


class Adapter(View):
    def get(self):
        return str(self.get_tuple())


def main(obj):
    print("Rezult: " + obj.get())
    print(type(obj.get()))


if __name__ == '__main__':
   init_db()
   # CreateSQLUser.reg()
   obj = Adapter()
   main(obj)


