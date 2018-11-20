def dac_count(arr):
    return 0 if len(arr) == 0 else 1 + dac_count(arr[1:])

print(dac_count([1, 3, 5, 2, 9]))
print(dac_count([1]))
