class VendingMachine:
    def __init__(self):
        print("WELCOME TO WYXGLE'S VENDING MACHINE!")
        self.beverages = {
            'Water': 1.00, 'Coconut Water': 2.00, 'Cocktail Juice': 3.00,
            'Lemonade': 4.00, 'Iced Tea': 4.00, 'Soy Milk': 5.00,
            'Gatorade': 5.00, 'Coca Cola': 2.00, 'Pepsi': 2.00, 'Sprite': 2.00
        }
        self.edibles = {
            'Mixed Nuts': 2.00, 'Energy Bar': 3.00, 'Dark Chocolate': 3.00,
            'Croissant': 2.00, 'Oreos': 3.00, 'Veggie Cookies': 4.00,
            'Takis': 4.00, 'Veggie Chips': 4.00, 'Pringles': 5.00, 'Pop Tarts': 10.00
        }
        self.balance = 0.0

        print("Available Beverages")
        for item, cost in self.beverages.items():
            print(f"{item}: ${cost:.2f}")

        print("\nAvailable Edibles:")
        for item, cost in self.edibles.items():
            print(f"{item}: ${cost:.2f}")
    def display_beverages(self):
        print("Available Beverages:")     
        for item, cost in self.beverages.items():
            print(f"{item}: ${cost:.2f}")

    def display_edibles(self):
        print("Available Edibles:")  
        for item, cost in self.edibles.items():
            print(f"{item}: ${cost:.2f}")

    def insert_coin(self, amount):
        self.balance += amount
        print(f"Inserted: ${amount:.2f}. Total Balance: ${self.balance:.2f}")

    def select_product(self, product):
        if product in self.beverages:
            category = "Beverage"
            products = self.beverages
        elif product in self.edibles:
            category = "Edible"
            products = self.edibles
        else:
            category = "Invalid"

        if category != "Invalid":
            price = products[product]
            if self.balance >= price:
                self.balance -= price
                print(f"Dispensing {category}: {product}. Remaining balance: ${self.balance:.2f}")
            else:
                print("Inadequate Cash. Please Insert the Right Amount.")
        else:
            print("Invalid Input Selection. Kindly Pick an Available Item.")


# Example Usage:
vending_machine = VendingMachine()
vending_machine.insert_coin(2.00)
vending_machine.select_product('Coca Cola')
vending_machine.select_product('Mixed Nuts')


