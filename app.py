class Product:
    # Define constructor with names (String), price (float), and sku (int).
    def __init__(self, name, price, sku):
        # Assign params to properties. 
        self.name = name
        self.price = price
        self.sku = sku
    
    # 9. Takes the object as an argument and returns a string printing out the information about the object. 
    def __str__(self):
        return f"{self.name} (SKU: {self.sku}) - ${self.price:.2f}"

class ShoppingCart:
    # Define constructor with items (list) that will hold a list of `Product` objects.
    def __init__(self):
        self.items = []

    # A `__str()__` method that prints out information about the `ShoppingCart` object. 
    def __str__(self):
        return f"Shopping Cart with {len(self.items)} items."
    
    # Method that takes the object, a product, and a quantity as an argument
    def add_items(self, product, quantity=1):
        # Adds the item to the object's `items` list.
        self.items.append({"product": product, "quantity": quantity})
    
    # Method that takes the object as an argument and returns the total.
    def get_total(self):
        # Initialize a variable called `total` with a value of zero.
        total = 0
        # Iterate through `items` and total up the cost of all the items in the cart
        for item in self.items:
            total += item["product"].price * item["quantity"]
        # 19d. - Return `total`
        return total
    
    # Takes the object as an argument displays the cart contents.
    def display_cart(self):
        # Iterates through the `items` in the cart and print out a string
        for item in self.items:
            print(f'{item["product"]} - Quantity: {item["quantity"]}')
        # When the iteration is complete, print the total cost of all the items in the format `"Total: $[TOTAL]"`.
        print(f"Total: ${self.get_total():.2f}")