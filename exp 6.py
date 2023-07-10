Grocery = {
    "Cornflakes": {"quantity": 15, "price": 100},
    "Muesli": {"quantity": 14, "price": 150},
    "Oats": {"quantity": 10, "price": 80},
    "Wheat Flakes": {"quantity": 5, "price": 75},
    "Granola": {"quantity": 8, "price": 125}
}

print("Item details before updating:")
print(Grocery)

choice = int(input("Display what you want to do?\n"
                   "1. Add additional quantity of cereals\n"
                   "2. Update the price of the grocery\n"
                   "3. Add a new item\n"
                   "Enter your choice: "))

if choice == 1:
    item_name = input("Enter the grocery item name: ")
    quantity_to_add = int(input("Enter the quantity of items to be added: "))
    
    if item_name in Grocery:
        Grocery[item_name]["quantity"] += quantity_to_add
    else:
        print("Item not found in the grocery list.")

elif choice == 2:
    item_name = input("Enter the grocery item name: ")
    new_price = int(input("Enter the new price of the item: "))
    
    if item_name in Grocery:
        Grocery[item_name]["price"] = new_price
    else:
        print("Item not found in the grocery list.")

elif choice == 3:
    item_name = input("Enter the name of the new item: ")
    quantity = int(input("Enter the quantity of the new item: "))
    price = int(input("Enter the price of the new item: "))
    
    Grocery[item_name] = {"quantity": quantity, "price": price}

else:
    print("Invalid choice.")

print("Item details after updating:")
print(Grocery)

