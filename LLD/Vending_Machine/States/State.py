from abc import ABC, abstractmethod
from typing import List
from Item import Item
from Coin import Coin


class State(ABC):

    @abstractmethod
    def click_on_insert_coin_button(self, machine):
        pass

    @abstractmethod
    def click_on_start_product_selection_button(self, machine):
        pass

    @abstractmethod
    def insert_coin(self, machine, coin: 'Coin'):
        pass

    @abstractmethod
    def choose_product(self, machine, code_number: int):
        pass

    @abstractmethod
    def get_change(self, return_change_money: int) -> int:
        pass

    @abstractmethod
    def dispense_product(self, machine, code_number: int) -> 'Item':
        pass

    @abstractmethod
    def refund_full_money(self, machine) -> List['Coin']:
        pass

    @abstractmethod
    def update_inventory(self, machine, item: 'Item', code_number: int):
        pass
