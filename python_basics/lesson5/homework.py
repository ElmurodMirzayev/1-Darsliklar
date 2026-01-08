"""Kalkulatorning mukammali"""

# calculate = input("Matimatik ifoda kiriting: ")

# def str_math_split(str_math):
#     numbers = "0123456789.()"
#     minus = "-"
#     plus = "+"
#     multiple_and_division = "*/"

#     if str_math[0] in numbers:
#         str_math = "+" + str_math

#     spliting_str_math = []
#     number = ""
#     number_sign = ""
#     starting_number = False
#     is_number_signed = False
#     to_multiple = False
#     i = 0
#     while i < len(str_math):
#         if to_multiple:
#             if str_math[i] == "-" and number_sign == "-":
#                 number_sign = "+"
#                 i += 1
#             elif str_math[i] == "-" and number_sign == "+":
#                 number_sign = "-"
#                 i += 1
            
#             to_multiple = False
            
#         if not starting_number:
#             if str_math[i] == plus:
#                 number_sign = "+"
#             elif str_math[i] == minus:
#                 number_sign = "-"

#             starting_number = True

#         elif starting_number:
#             if str_math[i] in numbers:
#                 number += str_math[i]
#             elif str_math[i] == plus or str_math[i] == minus:
#                 spliting_str_math.append(number_sign + number)
#                 number = ""
#                 number_sign = ""
#                 starting_number = False
#                 continue
#             elif str_math[i] in multiple_and_division:
#                 number += str_math[i]
#                 to_multiple = True


#         if i == len(str_math)-1:
#             spliting_str_math.append(number_sign + number)

#         i += 1
            

#     return spliting_str_math

# def calculating_splited_math(splited_math):
#     numbers = "0123456789."
#     arifmetiks = "-+"
#     multiple_and_division = "*/"

#     result = 1
#     number = ""
#     operation = "*"
#     is_there_mult_div = False
#     for i in range(len(splited_math)):
#         for j in range(len(splited_math[i])):
#             if splited_math[i][j] in numbers or splited_math[i][j] in arifmetiks:
#                 number += splited_math[i][j]
#             if splited_math[i][j] in multiple_and_division or j == len(splited_math[i])-1:
#                 is_there_mult_div = True
#                 if operation == "*":
#                     result *= float(number)
#                 elif operation == "/":
#                     result /= float(number)

#                 number = ""

#                 if splited_math[i][j] == "*":
#                     operation = "*"
#                 elif splited_math[i][j] == "/":
#                     operation = "/"

                

#         if is_there_mult_div:
#             splited_math[i] = result
#             result = 1

#     return sum(splited_math)

     
# splited_math = str_math_split(calculate)


# print(f"{calculate} = {calculating_splited_math(splited_math)}")

    

#-------------------------------------------------------------


# """Tup sonni topish"""
# son = int(input("Sonningizni kiriting: "))
# is_tub_son = False
# if son == 2:
#     is_tub_son = True
# else:
#     for i in range(2, son):
#         if son % i != 0:
#             is_tub_son = True
#         else:
#             is_tub_son = False
#             break

# if is_tub_son:
#     print("Bu tub son")
# else:
#     print("Bu tub son emas")

#------------------------------------------------------------------


# """Murakkab sonni topish"""
# son = int(input("soningizni kiriting: "))
# count = 0
# for i in range(1, son+1):
#     if son % i == 0:
#         count += 1

# if count >= 3:
#     print(f"{son} soni murakkab son hisoblanadi")
# else:
#     print(f"{son} soni murakkab son emas")


#--------------------------------------------------------------------



# n = int(input("n: "))
# numbers = "0123456789"
# level = ""
# level_index = 1
# result = ""
# count = 0
# for i in range(n+1):
#     if count == 10:
#         level = numbers[level_index]
#         level_index += 1
#         count = 0
#         if level_index == 10:
#             level_index = 1

#     result += level + numbers[count]
#     count += 1

# print(result)



#---------------------------------------------------------------------




