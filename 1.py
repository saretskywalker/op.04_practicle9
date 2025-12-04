number = int(input("Введите конечное число"))
posledovatelnost = 1
while posledovatelnost <= number:

    if posledovatelnost == 5:
        posledovatelnost += 5
    elif posledovatelnost == 17:
        posledovatelnost += 21
    elif posledovatelnost == 78:
        posledovatelnost += 10
    print(posledovatelnost)
    posledovatelnost += 1
