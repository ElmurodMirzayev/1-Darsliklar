# sonlarni ketma-ket chiqarish.

# n = 150

# chegara = 10
# level = 1
# result = 0
# for i in range(1, n+1):
#     if i == chegara:
#         level += 1
#         chegara = chegara * 10

#     result = result * 10**level + i

# print(result)

#---------------------------------------------

# Endi shuni teskarisini chiqarish
# n = 14

#Nechchi xonaligini aniqlash
# level = 0
# N = n
# while N > 0:
#     N = N // 10
#     level += 1



# chegara = 10**(level-1)
# result = 0 #150
# for i in range(n, -1, -1):
#     if i == chegara-1:
#         level -= 1
#         chegara = chegara / 10

#     result = result * 10**level + i

# print(result)


#---------------------------------------------------------------

# 1.Uyga vazifa tub va murakkab sonlani alohida 
# listga chiqarish

# son = int(input("Son kiriting: "))
# tub_sonlar = []
# murakkab_sonlar = []
# for i in range(2, son+1):
#     bu_tub_son = True
#     for j in range(2, i):
#         if i % j == 0:
#             bu_tub_son = False
#             break

#     if bu_tub_son or i == 2:
#         tub_sonlar.append(i)
#     else:
#         murakkab_sonlar.append(i)

# print(f"Bu tub sonlar: {tub_sonlar}")
# print(f"Bu murakkab sonlar: {murakkab_sonlar}")

# -----------------------------------------------------


# 2.uyga vazifa user kritigan son necha 
# xonali ekanligini topish
# masalan: 12: 2 xonali, 5634: 4 xonali

# son = int(input("son kiriting: "))
# count = 0
# while son > 0:
#     son = son // 10
#     count += 1

# print(f"siz kiritgan son {count} xonali son")


#----------------------------------------------------------



# 3. kiritilgan sonni oxirgi raqamini topish

# son = int(input("son kiriting: "))
# oxirgi_raqam = son % 10
# print(f"Soningizni oxirgi raqami {oxirgi_raqam}")



#-----------------------------------------------------


# 4. kiritlgan sonni ketma ket 5 marta 2 ga 
# bo'lganda chiqadigan sonnit opish (integreda)


# son = int(input("son kiriting: "))
# for i in range(5):
#     son /= 2

# print(son)





n = int(input())
arr = map(int, input().split())

the_highest = 0
the_second = 0
for i in arr:
    for j in arr:
        if j > the_highest:
            the_highest = j
        elif j < the_highest:
            the_second = j

print(the_highest)
print(the_second)



