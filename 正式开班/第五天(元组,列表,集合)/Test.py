from typing import List


# 冒泡排序
def bubbleSort(list_name) -> List:
    for i in range(len(list_name) - 1):
        flag = False
        for j in range(len(list_name) - 1 - i):
            if list_name[j] > list_name[j + 1]:
                flag = True
                list_name[j], list_name[j + 1] = list_name[j + 1], list_name[j]
        if not flag:
            break
    return list_name


print(bubbleSort([1, 2, 3, 4222, 1, 2, 3]))
