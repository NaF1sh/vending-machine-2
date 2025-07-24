class Vending_machine:

    def __init__(self):
        self.drinks = [
            {"name": "Pepsi", "price": 1.50, "stock": 20, "max_stock": 20},
            {"name": "Water", "price": 1.00, "stock": 15, "max_stock": 15},
            {"name": "Coke", "price": 1.75, "stock": 10, "max_stock": 10}
        ]

    def adding_drink(self, name, price, quantity):
        new_drink = {
            "name": name,
            "price": price,
            "stock": quantity,
            "max_stock": quantity
        }
        self.drinks.append(new_drink)
        print(f"{name} added successfully!")

    def display_drink(self):
        for drink in self.drinks:
            print(
                f"{drink['name']} - ${drink['price']:.2f} | {drink['stock']}/{drink['max_stock']}")

    def select_drink(self, name):
        for drink in self.drinks:
            if drink["name"].lower() == name.lower():
                self.Processing_buy(
                    drink["name"], drink["price"], drink["stock"])
                return  # Exit once found

    # If loop finishes and no match found:
    print("Drink not found.")

    def Processing_buy(self, name, price, quantity):
        if quantity == 0:
            print(f"Sorry, {name} is out of stock.")
            return

        print(f"{name} is available for ${price:.2f}.")
        try:
            payment = float(input("Please enter payment: $"))
        except ValueError:
            print("Invalid input. Transaction cancelled.")
            return

        if payment < price:
            print("Insufficient payment. Transaction cancelled.")
            return

        change = round(payment - price, 2)
        print(f"Thank you for purchasing {name}!")
        print(f"Your change is: ${change:.2f}")

        for drink in self.drinks:
            if drink["name"].lower() == name.lower():
                drink["stock"] -= 1
                break
        self.give_change(change)

    def give_change(self, change):
        coins = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
        count = {}

        remaining = round(change, 2)

        for coin in coins:
            coin_count = int(remaining // coin)
            if coin_count > 0:
                count[coin] = coin_count
                remaining = round(remaining - coin * coin_count, 2)

        if count:
            print("Change breakdown:")
            for coin, qty in count.items():
                print(f"{qty} x ${coin:.2f}")
