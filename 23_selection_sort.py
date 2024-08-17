def selection_sort(list1):
    for i in range(len(list1)):
        min_index = i
        for j in range(i+1, len(list1)):
            if list1[j]<list1[min_index]:
                min_index = j
        list1[i], list1[min_index] = list1[min_index], list1[i]


l = [34,67,12, 89,25,50]
selection_sort(l)
print(l)