def dac_binary_search(arr, item):
    mid = int(len(arr)/2)
    if item == arr[mid]:
        return mid
    elif item < arr[mid]:
        dac_binary_search(arr[:mid], item)
    else:
        dac_binary_search(arr[mid+1:], item)

print(dac_binary_search([1, 3, 5, 14, 28, 99], 14))
