# Import the `Product` and `ShoppingCart` classes into the file. 
from app import Product, ShoppingCart

#  `main()` function that will hold all of our program runs. 

def main():
    # Two instances of the `Product` class
    laptop = Product("MacBook Pro", 1299.99, "123456")
    headphones = Product("AirPods", 159.99, "789012")
    print(laptop.name)
    print(headphones.price)

    # Printing out the object
    print("\nUsing __str__ method:")
    print(laptop)
    print(headphones)

    # Creates an instance of the shopping cart and prints it to the console.
    cart = ShoppingCart()
    print("\nUsing __str__ method:")
    print(cart)

    # Adds each of the `Product` objects you created to the `ShoppingCart` instance using the `add_items` method. 
    cart.add_items(laptop)
    cart.add_items(headphones, 2)


    # Display the cart contents
    print("\nUsing display_cart method:")
    cart.display_cart()

    # Call `get_total` to see the total cost of everything that you added to the cart.
    print("\nUsing get_total method:")
    print(f'TOTAL: ${cart.get_total()}')

# Call the main() function to run the code inside the function
main()