name = ""
counter = 0
while name != "левон":
    name = input("Введите имя: ").lower()
    counter += 1
    if name == "александра":
        number_1 = counter
    elif name == "левон":
        number_2 = counter
print(number_2 - number_1 - 1)
        
