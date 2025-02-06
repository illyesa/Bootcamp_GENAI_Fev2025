
# #1
# print(("\033[32mHello\033[0m world\n" * 4).strip())

# #2
# print((99**3)*8)

# #3
# your_name=input("Your name :")
# my_name="my_name"
# if your_name == my_name:
#     print(f"we have the same {my_name}")
# else:
#     print("diff")


# #4
# tall=int(input("Your height in centimeters :"))
# if tall>145:
#     print("tall enough to ride")
# else:
#     print("too small")

# #5
# my_fav_numbers = {2, 10, 20}
# my_fav_numbers.add(26)
# my_fav_numbers.add(42)
# print(f"My favorite numbers after adding: {my_fav_numbers}")

# my_fav_numbers.remove(42)
# print(f"My favorite numbers after removing the last added number: {my_fav_numbers}")
# friend_fav_numbers = {3, 9, 27}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(f"Our favorite numbers combined: {our_fav_numbers}")

#6
# my_tuple = (1, 2, 3) # on ne peut pas ajouter a un tuple mais on peut en crée un nouveau
# new_tuple = my_tuple + (4, 5)
# print(new_tuple)

#7
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("kiwi")
# basket.insert(0, "Apples")
# print(basket)
# print(basket.count("Apples"))
# basket.clear()
# print(basket)

#8
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)
finished_sandwiches=[]
while sandwich_orders:
    s=sandwich_orders[0]
    sandwich_orders.remove(s)
    finished_sandwiches.append(s)
    print(f"I made your {s}")
