"""
Найдите сумму цифр трехзначного числа.

Пример:

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""
while True:
    number = int(input ('Введите трехзначное число'))
    if number > 99 and number < 1000:
        print (number//100 + number//10%10 + number%10)
        break
    else:
        print ('Число должно быть > 99 и < 1000')
