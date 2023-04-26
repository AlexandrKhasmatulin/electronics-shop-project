from src.item import Item
class Mixin:
    def __init__(self, language="EN"):
        self.language = language

    def change_lang(self):
        list_lan = ["EN", "RU"]
        if self.language not in list_lan:
            raise AttributeError
        elif self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"
        return self

class Keyboard(Item, Mixin):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name
    def __repr__(self):
        return f'{self.language}'
