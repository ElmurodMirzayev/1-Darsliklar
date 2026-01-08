def func(num1, num2=None):
    if not num2:
        return "Kamida 2 ta qiymay kiritish kerak"
    if num1 > num2:
        return num1
    elif num2 == num1:
        return "Teng"
    return num2

print(func(1, 2))