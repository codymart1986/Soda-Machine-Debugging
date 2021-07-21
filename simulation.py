from soda_machine import SodaMachine
from customer import Customer
from user_interface import User_Interface


class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        #"""The central method called in main.py."""
        customer = Customer()
        customer.wallet.fill_wallet()
        soda_machine = SodaMachine()
        soda_machine.fill_register()
        soda_machine.fill_inventory()
        will_proceed = True
        while will_proceed:
            user_option = User_Interface.simulation_main_menu()
            if user_option == 1:
                soda_machine.begin_transaction(customer)
            elif user_option == 2:
                customer.check_coins_in_wallet()
            elif user_option == 3:
                customer.check_backpack()
            else:
                will_proceed = False
