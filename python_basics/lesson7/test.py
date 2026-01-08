# n = int(input("n: "))
# arr = map(int, input().split())
          
# print(list(arr))


# a = [1, 2, 3]
# b = [4, 5, 6]

# result = map(lambda x, y: x + y, a, b)
# print(list(result))

n = int(input())
arr = map(int, input().split())
max1 = None
max2 = None
for i in arr:
    if i != max1:
        if max1 == None:
            max1 = i
        elif i > max1:
            max2 = max1
            max1 = i
        elif max2 == None or i > max2:
            max2 = i

            
print(max2)

    

