from src.item import Item
class Mixin:
    def __init__(self, language="EN"):
        self.language = language


    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"
        return str(self.language)

class Keyboard(Item, Mixin):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name
