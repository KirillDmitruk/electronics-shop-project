from src.item import Item


class Mixin:

    def __init__(self):
        self._language = None

    def install_lang(self):
        self._language = 'EN'

    def change_lang(self) -> None:
        if self._language == 'EN':
            self._language = 'RU'
        elif self._language == 'RU':
            self._language = 'EN'


class Keyboard(Item, Mixin):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        Mixin.install_lang(self)

    def __repr__(self):
        return f"Keyboard({self.name}, {self.price}, {self.quantity}, {self._language})"

    @property
    def language(self):
        return self._language