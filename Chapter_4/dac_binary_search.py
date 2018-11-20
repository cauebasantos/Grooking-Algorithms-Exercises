def dac_binary_search(arr, item):
    mid = int(len(arr)/2)
    if item == arr[mid]:
        return mid
    elif item < arr[mid]:
        return dac_binary_search(arr[:mid], item)
    else:
        return mid + 1 + dac_binary_search(arr[mid+1:], item)

print(dac_binary_search([1, 3, 5, 14, 28, 99],  1))
print(dac_binary_search([1, 3, 5, 14, 28, 99],  3))
print(dac_binary_search([1, 3, 5, 14, 28, 99],  5)) 
print(dac_binary_search([1, 3, 5, 14, 28, 99],  14))
print(dac_binary_search([1, 3, 5, 14, 28, 99],  28))
print(dac_binary_search([1, 3, 5, 14, 28, 99],  99)) 
