pizzas = ['Margherita', 'Calzones', 'Marinara', 'Pepperoni', 'Capricciosa']
friend_pizzas = pizzas[:]
pizzas.append('Hawaiian')
friend_pizzas.append('Vegetarian')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)