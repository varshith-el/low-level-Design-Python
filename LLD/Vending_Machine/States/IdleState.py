from .State import State
from typing import List
from Coin import Coin
from Item import Item
from .HasMoneyState import HasMoneyState

class IdleState(State):

    def __init__(self, machine):
        print("Currently Vending machine is in IdleState")
        if machine is not None:
            machine.set_coin_list([])

    def click_on_insert_coin_button(self, machine):
        machine.set_vending_machine_state(HasMoneyState())

    def click_on_start_product_selection_button(self, machine):
        raise Exception("first you need to click on insert coin button")

    def insert_coin(self, machine, coin: 'Coin'):
        raise Exception("you can not insert Coin in idle state")

    def choose_product(self, machine, code_number: int):
        raise Exception("you can not choose Product in idle state")

    def get_change(self, return_change_money: int) -> int:
        raise Exception("you can not get change in idle state")

    def refund_full_money(self, machine) -> List['Coin']:
        raise Exception("you can not get refunded in idle state")

    def dispense_product(self, machine, code_number: int) -> 'Item':
        raise Exception("product can not be dispensed in idle state")

    def update_inventory(self, machine, item: 'Item', code_number: int):
        machine.get_inventory().add_item(item, code_number)
