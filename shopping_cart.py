foods = []
prices = []
total = 0

while True:
    food = input("Enter the food item:")
    if food.lower() == 'q':
        break
    else:
        foods.append(food)
        price = float(input(f'Enter the price of {food}:'))
        prices.append(price)

for price in prices:
    total += price

print('-----Your Cart-----\nItems:')
for food in foods:
    print(food)

print(f"\nYour total is: {total}")