if __name__ == '__main__':
    
    def find_indx_with_min_value(simple_list: list):
        index_min_value = 0
        for i in range(len(simple_list)):
            if simple_list[i][1] < simple_list[index_min_value][1]:
                index_min_value = i

        return index_min_value
    

    def my_sorting_by_grade(list_to_sort: list):
        result = []
        for _ in range(len(list_to_sort)):

            min_index = find_indx_with_min_value(list_to_sort)
            result.append(list_to_sort.pop(min_index))
            
        return result

    grade_students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grade_students.append([name, score])


    grade_students = my_sorting_by_grade(grade_students)
    second_lowest = 0
    grades = []
    for element in grade_students:
        grades.append(element[1])

    list_of_num = sorted(list(set(grades)))
    second_lowest = list_of_num[1]


    names_of_similar_values = []
    for grade in grade_students:
        if grade[1] == second_lowest:
            names_of_similar_values.append(grade[0])
        

    names_of_similar_values.sort()
    for name in names_of_similar_values:
        print(name)
                
        
        
        