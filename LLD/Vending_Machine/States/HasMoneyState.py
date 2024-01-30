
from .State import State
from typing import List
from Coin import Coin
#from .IdleState import IdleState
from Item import Item
from .SelectionState import SelectionState

class HasMoneyState(State):

    def __init__(self):
        print("Currently Vending machine is in HasMoneyState")

    def click_on_insert_coin_button(self, machine):
        return

    def click_on_start_product_selection_button(self, machine):
        machine.set_vending_machine_state(SelectionState())

    def insert_coin(self, machine, coin: 'Coin'):
        print("Accepted the coin")
        machine.get_coin_list().append(coin)

    def choose_product(self, machine, code_number: int):
        raise Exception("you need to click on start product selection button first")

    def get_change(self, return_change_money: int) -> int:
        raise Exception("you can not get change in hasMoney state")

    def dispense_product(self, machine, code_number: int) -> 'Item':
        raise Exception("product can not be dispensed in hasMoney state")

    def refund_full_money(self, machine) -> List['Coin']:
        from IdleState import IdleState
        print("Returned the full amount back in the Coin Dispense Tray")
        machine.set_vending_machine_state(IdleState(machine))
        return machine.get_coin_list()

    def update_inventory(self, machine, item: 'Item', code_number: int):
        raise Exception("you can not update inventory in hasMoney state")
