def dac_max_number(arr):
    try:
        return arr[0] if len(arr) == 1 else max(arr[0], dac_max_number(arr[1:]))
    except:
        return None

print(dac_max_number([1, 4, 3, 5, 10, 9]))
print(dac_max_number([]))
