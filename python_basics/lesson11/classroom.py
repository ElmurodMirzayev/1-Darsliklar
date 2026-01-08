
def my_max(list1):
    maximum = list1[0]
    index = None
    for i in range(len(list1)):
        if maximum <= list1[i]:
            maximum = list1[i]
            index = i
    return index

def my_sort(list1):
    new_list1 = []
    for i in range(len(list1)):
        bigger_inx = my_max(list1)
        new_list1.append(list1.pop(bigger_inx))

    return new_list1

sorted_list = my_sort([45, 23, 67, 1, 78, 100, 23, 45, ])
print(sorted_list[1])