from vending_machine import Vending_machine

vm = Vending_machine()


class customers_menu:

    def __init__(self):
        print("Hello There!! ")
        print("Select the drink you want to buy: ")
        vm.display_drink()
        name = input("Enter the name of the drink you want: ")
        vm.select_drink(name)
        print("Bye,Have a good day")
