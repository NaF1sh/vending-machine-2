from vending_machine import Vending_machine

vm = Vending_machine()


def owner_display_menu():
    print("\nOwner Operations:")
    print("1. Add Drink")
    print("2. Restock Drink")
    print("3. Display Stock")
    print("4. Exit to Main Menu")


def owner_operations():
    while True:
        owner_display_menu()
        try:
            choice = int(input("Enter Choice (1-4): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            new_drink_name = input("Enter Drink Name: ")
            try:
                drink_price = float(input("Enter Drink Price: "))
                drink_quantity = int(input("Enter Drink Quantity: "))
                vm.adding_drink(new_drink_name, drink_price,
                                drink_quantity)

            except ValueError:
                print("Invalid price or quantity. Try again.")

        elif choice == 2:
            vm.display_drink()

            drink_name = input("Enter the Name of drink to Retock")
            found = False

            for drink in vm.drinks:
                if drink["name"].lower() == drink_name.lower():
                    print(
                        f"Currently there are {drink['stock']} units of {drink['name']} in stock.")
                    try:
                        restock_amount = int(
                            input("How many do you want to add? "))
                        if drink['stock'] + restock_amount > drink['max_stock']:
                            print("Cannot restock beyond max stock.")
                        else:
                            drink['stock'] += restock_amount
                            print(
                                f"{drink['name']} restocked. New stock: {drink['stock']}")
                    except ValueError:
                        print("Please enter a valid number.")
                    found = True
                    break

            if not found:
                print("Drink not found.")

        elif choice == 3:
            vm.display_drink()

        elif choice == 4:
            print("Exiting to main menu...")
            break

        else:
            print("Invalid choice. Please select 1-4.")


def owner_login():
    password = input("Please Enter Password: ")
    if password == "12345678":
        print("Login Success! Welcome, owner.")
        owner_operations()
    else:
        print("Incorrect password.")
