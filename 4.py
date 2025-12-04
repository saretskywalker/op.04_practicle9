number = int(input("Введите число"))
number_3 = number
number_last_digit = number
number_even_digit = number
number_products_over_7 = number
number_sum_over_5 = number
number_0_5 = number


count_3 = 0
while number_3 > 10:
    new_last_digit = number_3 % 10
    if new_last_digit == 3:
        count_3 += 1
    number_3 //= 10
print("Колличество цифры 3 в числе:",count_3)


last_digit = number_last_digit % 10
count_last_digit = 0
while number_last_digit > 10:
    new_last_digit = number_last_digit % 10
    if last_digit == new_last_digit:
        count_last_digit += 1
    number_last_digit //= 10
print("Последнее цифра встречается:", count_last_digit, "раз")


count_even_digit = 0
while number_even_digit > 10:
    new_last_digit = number_even_digit % 10
    if new_last_digit % 2 == 0:
        count_even_digit += 1
    number_even_digit //= 10
print("Колличество четных цифр в числе равно:", count_even_digit)


count_sum_digit_over_5 = 0
while number_sum_over_5 > 10:
    new_last_digit = number_sum_over_5 % 10
    if new_last_digit > 5:
        count_sum_digit_over_5 += new_last_digit
    number_sum_over_5 //= 10
print("Сумма цифр больших 5 равна:", count_sum_digit_over_5)


count_product_digit_over_7 = 1
while number_products_over_7 > 10:
    new_last_digit = number_products_over_7 % 10
    if new_last_digit > 7:
        count_product_digit_over_7 *= new_last_digit
    number_products_over_7 //= 10
print("Произведение цифр больших 7:",count_product_digit_over_7)

count_digit_5_0 = 0
while number_0_5 > 10:
    new_last_digit = number_0_5 % 10
    if new_last_digit == 5 or new_last_digit == 0:
        count_digit_5_0 += 1
    number_0_5 //= 10
print("цифры 0 и 5 встречаются", count_digit_5_0, "раз")



