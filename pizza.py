

def print_pizza_order(pizza):
    print("I would like a", pizza['size'], "pizza on a", pizza['crust'], "crust")
    print("With", pizza['toppings'], "on it")

monday = {'size': "small", 'crust': "traditional", 'toppings': "extra cheese"}
friday = {'size': "large", 'crust': "deep dish", 'toppings': "sausage"}

print_pizza_order(monday)

