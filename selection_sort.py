def findBigger(arr):
    bigger = arr[0]
    bigger_index = 0

    for i in range(1, len(arr)):
        if arr[i] > bigger:
            bigger = arr[i]
            bigger_index = i

    return bigger_index

def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        bigger = findBigger(arr)
        newArr.append(arr.pop(bigger))

    return newArr


print(selection_sort([5, 3, 6, 2, 10]))
