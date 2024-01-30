from .State import State
from typing import List
from Coin import Coin
from .DispenseState import DispenseState
from Item import Item


class SelectionState(State):

    def __init__(self):
        print("Currently Vending machine is in SelectionState")

    def click_on_insert_coin_button(self, machine):
        raise Exception("you can not click on insert coin button in Selection state")

    def click_on_start_product_selection_button(self, machine):
        return

    def insert_coin(self, machine, coin: 'Coin'):
        raise Exception("you can not insert Coin in selection state")

    def choose_product(self, machine, code_number: int):

        # 1. get item of this codeNumber
        item = machine.get_inventory().get_item(code_number)

        # 2. total amount paid by User
        paid_by_user = sum(coin.value for coin in machine.get_coin_list())

        # 3. compare product price and amount paid by user
        if paid_by_user < item.get_price():
            print(f"Insufficient Amount, Product you selected is for price: {item.get_price()} and you paid: {paid_by_user}")
            self.refund_full_money(machine)
            raise Exception("insufficient amount")
        elif paid_by_user >= item.get_price():

            if paid_by_user > item.get_price():
                self.get_change(paid_by_user - item.get_price())
            machine.set_vending_machine_state(DispenseState(machine, code_number))

    def get_change(self, return_extra_money: int) -> int:
        print(f"Returned the change in the Coin Dispense Tray: {return_extra_money}")
        return return_extra_money

    def refund_full_money(self, machine) -> List['Coin']:
        from .IdleState import IdleState
        print("Returned the full amount back in the Coin Dispense Tray")
        machine.set_vending_machine_state(IdleState(machine))
        return machine.get_coin_list()

    def dispense_product(self, machine, code_number: int) -> 'Item':
        raise Exception("product can not be dispensed in Selection state")

    def update_inventory(self, machine, item: 'Item', code_number: int):
        raise Exception("Inventory can not be updated in Selection state")
