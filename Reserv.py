import random

# Reservation Lists
names = [
    "Alimamy Conteh",
    "Sahid Damien",
    "Kadiatu Koroma",
    "Fatmata Koroma",
    "Morgana Lefe"
]

menus = {
    "Pizza": 80,
    "Salad": 100,
    "Chicken Nuggets": 44,
    "Jollof Rice": 22,
    "Donuts": 15
}

drinks = {
    "Apple Cider": 35,
    "Tequila": 55,
    "Diet Coke": 22,
    "Fanta": 10,
    "Champagne": 120
}

# Define food_order_input and drink_order_input functions here
# (Same as before)

custom_menu = {}  # Initialize the custom menu
food_order = {}  # Initialize food_order
drink_order = {}  # Initialize drink_order

restaurant_name = "Adamawa_Bawenda"
print(
    f"Hello, and welcome to {restaurant_name}.\nWhat can I do for you today? 🙂")
reservation_status = input("Do you have a reservation? (y/n) ").lower()

if reservation_status == "y":
    customer_name = input("What's your name? ")
    if customer_name.lower() in [name.lower() for name in names]:
        table_number = random.randint(1, 52)
        print(
            f"Welcome {customer_name}, please find your way to table {table_number}.")
    else:
        print("Sorry, there seems to be a mix-up as we do not have a reservation under your name.")
        new_reservation = input(
            "Would you like to make a new reservation? (y/n) ").lower()
        if new_reservation == "y":
            names.append(customer_name)
            table_number = random.randint(1, 52)
            print(f"Reservation for {customer_name} has been added.")
            print(
                f"Welcome {customer_name}, please find your way to table {table_number}.")
        elif new_reservation == "n":
            print("I'm sorry for any inconvenience, have a nice day.")
            # Exit the program if the response is "n"
            exit()
        else:
            print("Invalid response. Please enter 'y' or 'n' for the new reservation.")
elif reservation_status == "n":
    print("I'm sorry, we are fully booked for today. Have a nice day.")
    # Exit the program if there are no reservations
    exit()
else:
    print("Invalid response. Please enter 'y' or 'n' for the reservation status.")

# Check if the response to having a reservation is "no," and if so, don't ask about the menu
if reservation_status != "n":
    menu_request = input("Do you want to see our menu? (y/n) ").strip().lower()

    if menu_request == "y":
        # Display the menu with prices
        print("Here's the menu")
        print("\nFood Menu:")
        for menu, cost in menus.items():
            print(f"{menu.capitalize():<20} Le{cost}")

        print("\nDrinks Menu:")
        for drink, cost in drinks.items():
            print(f"{drink.capitalize():<20} Le{cost}")

        # Now, ask for food and drink orders
        # Call the function and store the result in food_order
        food_order = food_order_input()
        # Call the function and store the result in drink_order
        drink_order = drink_order_input()
    elif menu_request == "n":
        # Capitalize the input
        custom_item = input("What can we offer you? ").strip().title()
        custom_price = random.randint(5, 20)

        # Add the custom item to the custom_menu
        custom_menu[custom_item] = custom_price

        print(f"Sure, we will get your order for {custom_item} ready for you.")

    # Initialize variables to keep track of the total cost for food, drinks, and custom items
    food_total_cost = 0
    drink_total_cost = 0
    custom_total_cost = 0

    # Loop through the customer's food order and accumulate the costs
    for food_item, food_cost in food_order.items():
        food_total_cost += food_cost

    # Loop through the customer's drink order and accumulate the costs
    for drink_item, drink_cost in drink_order.items():
        drink_total_cost += drink_cost

    # Loop through the custom menu and accumulate the costs for custom items
    for custom_item, custom_cost in custom_menu.items():
        custom_total_cost += custom_cost

    # Calculate the total bill by adding the total cost for food, drinks, and custom items
    total_bill = food_total_cost + drink_total_cost + custom_total_cost

    # Print the customer's bill
    print(f"\nYour Bill, {customer_name.capitalize()}:\n")
    if food_order:
        print("Food:")
        for menu, cost in food_order.items():
            print(f"{menu.capitalize():<20} Le{cost}")
    if drink_order:
        print("\nDrinks:")
        for drink, cost in drink_order.items():
            print(f"{drink.capitalize():<20} Le{cost}")
    if custom_menu:
        print("\nCustom Items:")
        for custom_item, custom_cost in custom_menu.items():
            print(f"{custom_item:<20} Le{custom_cost}")
    print(f"Total Bill: Le{total_bill}")
