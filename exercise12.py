def pizzas():
    pizza_num = 0
    print("How many pizzas do you want to order?")
    pizza_quantity = int(input())
    for pizza in range(pizza_quantity):
        pizza_num += 1
        print(f"How many toppings for pizza {pizza_num}?")
        topping_quantity = int(input())
        print(f"You have ordered a pizza with {topping_quantity} toppings")

pizzas() 