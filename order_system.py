# ordering_system.py

# Define the menu with item names and prices
menu = {
    1: {"name": "Espresso", "price": 1.50},
    2: {"name": "Coffee", "price": 2.00},
    3: {"name": "Latte", "price": 2.50},
    4: {"name": "Cappuccino", "price": 3.00},
    5: {"name": "Tea", "price": 1.75}
}

# Function to calculate the subtotal
def calculate_subtotal(order_list):
    subtotal = sum(item['price'] for item in order_list)
    return round(subtotal, 2)

# Function to calculate the tax (15% of the subtotal)
def calculate_tax(subtotal):
    tax = subtotal * 0.15
    return round(tax, 2)

# Function to summarize the order
def summarize_order(order_list):
    order_names = [item['name'] for item in order_list]
    subtotal = calculate_subtotal(order_list)
    tax = calculate_tax(subtotal)
    total = subtotal + tax
    return order_names, round(total, 2)

# Main function to run the menu ordering system
def main():
    print("Welcome to the Coffee Shop!")
    print("Menu:")
    for key, value in menu.items():
        print(f"{key}. {value['name']} - ${value['price']}")

    # Get user input for three menu items
    order = []
    for i in range(3):
        choice = int(input(f"Enter item {i+1} choice (1-5): "))
        if choice in menu:
            order.append(menu[choice])
        else:
            print("Invalid choice, please enter a number between 1 and 5.")

    # Summarize the order and display results
    order_names, total = summarize_order(order)
    print("\nYour order summary:")
    print("Items ordered:", ", ".join(order_names))
    print(f"Total (including tax): ${total}")

# Run the program
if __name__ == "__main__":
    main()