# if __name__ == '__main__':
    
#     def my_sum(list_to_sum: list):
#         total = 0
#         for element in list_to_sum:
#             total += element
        
#         return total
        
        
#     def my_len(list_to_count: list) -> int:
#         count = 0
#         for element in list_to_count:
#             count += 1
            
#         return count
        
        
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
    
#     summa = my_sum(student_marks[query_name])
#     uzunlik = my_len(student_marks[query_name])
    
#     print(summa/uzunlik)
    




# if __name__ == '__main__':
#     N = int(input())
#     my_list = []
#     for _ in range(N):
#         command, *parametrs = input().split()
#         if command == "print":
#             print(my_list)
#         elif command == "insert":
#             parametr_1 = int(parametrs[0])
#             parametr_2 = int(parametrs[1])
#             my_list = my_list[:parametr_1] + [parametr_2] + my_list[parametr_1:]
#         elif command == "append":
#             parametr_1 = int(parametrs[0])
#             my_list.append(parametr_1)
#         elif command == "sort":
#             my_list.sort()
#         elif command == "pop":
#             if parametrs:
#                 parametr_1 = int(parametrs[0])
#                 my_list.pop(parametr_1)
#             else:
#                 my_list.pop()
#         elif command == "remove":
#             parametr_1 = int(parametrs[0])
#             my_list.remove(parametr_1)
#         elif command == "reverse":
#             my_list.reverse()
            
            

n = input()
my_tuple = input().split()
my_tuple = tuple(map(int, my_tuple))
print(hash(my_tuple))

print(hash("1 2"))