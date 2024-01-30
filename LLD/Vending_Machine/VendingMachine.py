from States.State import State

from States.IdleState import IdleState
from Inventory import Inventory
from Coin import Coin


class VendingMachine:

    def __init__(self):
        self.vending_machine_state = IdleState(self)
        self.inventory = Inventory(10)
        self.coin_list = []

    def get_vending_machine_state(self):
        return self.vending_machine_state

    def set_vending_machine_state(self, vending_machine_state: 'State'):
        self.vending_machine_state = vending_machine_state

    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory: 'Inventory'):
        self.inventory = inventory

    def get_coin_list(self):
        return self.coin_list

    def set_coin_list(self, coin_list: list['Coin']):
        self.coin_list = coin_list
