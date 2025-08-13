menu = {'biriyani': 120, 'fried rice': 130, 'noodles': 80, 'borotta': 20, 'chicken 65': 70, 'mutton chops': 95, 'fish fry': 30}

cart = []
total = 0

print("-------MENU--------")
for key, value in menu.items():
    print(f"{key:15}: Rs.{value}")
print("-------------------")

while True:
    food = input("Select an item(q to quit): ").lower()
    if food == 'q':
        break

    elif menu.get(food) is not None:
        cart.append(food)

    else:
        print("Invalid choice. Please select a valid item from the menu.")

for food in cart:
    total += menu[food]

print("-------------------")
print(f"Your order: {cart}")
print(f"Total: Rs.{total}")
print("-------------------")