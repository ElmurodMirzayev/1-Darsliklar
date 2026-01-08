def swap_case(s):
    result = ""
    for char in s:
        if char != char.lower():
            result += char.lower()
        else:
            result += char.upper()
    return result

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)





# def count_substring(string, sub_string):
    
#     count = 0
#     i = 0
#     j = 0
#     len_2 = 0
#     while i <= len(string)-1:
#         if string[i] == sub_string[j]:
#             len_2 += 1
#             i += 1
#             j += 1
#         else:
#             i += 1
#             j = 0
#         if len(sub_string) == len_2:
#             count += 1
        
#     return count


# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)




#167 - betdagi amaliyotlar
def kopaytma(*sonlar):
    result = 1
    for son in sonlar:
        result *= son

    return result



def talaba_info(ism, familiya, **informations):
    royxat = {
        "ism": ism,
        "familiya": familiya
    }
    for key, info in informations.items():
        royxat[key] = info

    return royxat




kopaytir_10ga = lambda x: x*10
qosh = lambda a, b: a+b

# print(qosh(14, 2))
# print(kopaytir_10ga(10))




import random

# sonlar = random.sample(range(1000), 10)
# print(sonlar)
# kvadrat = list(map(lambda x: x**2, sonlar))
# print(kvadrat)
# toq_sonlar = list(filter(lambda x: x%2 != 0, sonlar))

# print(toq_sonlar)

#------------------------------------------------------


# def is_tup_son(son):
#     if son <= 1:
#         return False
#     for i in range(2, son):
#         if son % i == 0:
#             return False
        
#     return True

# tub_sonlar = list(filter(is_tup_son, range(1000)))

# print(tub_sonlar)



# lugat = {
#     "ism": "Elmurod",
#     "yosh": 20,
#     "yil": 2005,
# }

# g = lugat.items()
# print(g)


names = ["Erik", "Max", "Habib"]
yosh = [20, 35, 28]
skill = [80, 76, 56]

h = list(zip(names, yosh, skill))
print(h)

for ism, yosh, skill in h:
    print(skill)