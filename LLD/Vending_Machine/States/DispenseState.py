
from .State import State
from typing import List
from Coin import Coin
from Item import Item

class DispenseState(State):

    def __init__(self, machine, code_number: int):
        print("Currently Vending machine is in DispenseState")
        self.dispense_product(machine, code_number)

    def click_on_insert_coin_button(self, machine):
        raise Exception("insert coin button can not clicked on Dispense state")

    def click_on_start_product_selection_button(self, machine):
        raise Exception("product selection button can not be clicked in Dispense state")

    def insert_coin(self, machine, coin: 'Coin'):
        raise Exception("coin can not be inserted in Dispense state")

    def choose_product(self, machine, code_number: int):
        raise Exception("product can not be chosen in Dispense state")

    def get_change(self, return_change_money: int) -> int:
        raise Exception("change can not returned in Dispense state")

    def refund_full_money(self, machine) -> List['Coin']:
        raise Exception("refund can not be happen in Dispense state")

    def dispense_product(self, machine, code_number: int) -> 'Item':
        from IdleState import IdleState
        print("Product has been dispensed")
        item = machine.get_inventory().get_item(code_number)
        machine.get_inventory().update_sold_out_item(code_number)
        machine.set_vending_machine_state(IdleState(machine))
        return item

    def update_inventory(self, machine, item: 'Item', code_number: int):
        raise Exception("inventory can not be updated in Dispense state")
