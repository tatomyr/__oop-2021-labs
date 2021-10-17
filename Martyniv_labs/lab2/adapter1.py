
# JSON - str
# XML - int

class Old:
    def get(self):
        return "12345"

class New:
    def get_int(self):
        return 67890

class Adapter(New):
    def get(self):
        return str(self.get_int())


def main(obj):
    print("Rezult: " + obj.get())


if __name__ == "__main__":
    obj = Adapter()
    main(obj)