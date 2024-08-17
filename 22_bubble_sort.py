def bubble_sort(list1):
    for i in range(1, len(list1)):
        for j in range(len(list1)-i):
            if list1[j]<list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]




def modified_bubble_sort(list1):
    flag = False
    for i in range(1, len(list1)):
        flag = False
        for j in range(len(list1)-i):
            if list1[j]>list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
                flag = True
        if not flag:
            break

# l = [34,67,12, 89,25,50]
# bubble_sort(l)
# print(l)
l = [34,67,12, 89,25,50]
modified_bubble_sort(l)
print(l)