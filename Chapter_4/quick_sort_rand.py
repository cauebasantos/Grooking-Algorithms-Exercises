from random import randint

def quick_sort_rand(arr):
    if len(arr) < 2:
        return arr
    else:
        rand_index = randint(0, len(arr) - 1)
        pivot = arr[rand_index]
        less = [item for item in arr[:rand_index] + arr[rand_index + 1:] if item <= pivot]
        greater = [item for item in arr[:rand_index] + arr[rand_index + 1:] if item > pivot]

        return quick_sort_rand(less) + [pivot] + quick_sort_rand(greater)

print(quick_sort_rand([12, 3, 5, -1, 8, 13, 2, 22, 2]))
