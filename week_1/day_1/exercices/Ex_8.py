sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while True :
    if "Pastrami sandwich" in sandwich_orders :
        sandwich_orders.remove("Pastrami sandwich")
    else :
        break
finished_sandwiches = []
while sandwich_orders :
     item = sandwich_orders.pop(0)
     finished_sandwiches.append(item)
     print(f"I made your {item}")
     
print(finished_sandwiches)
print(sandwich_orders)