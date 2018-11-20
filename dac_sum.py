def dac_sum(arr):
    return 0 if len(arr) == 0 else arr[0] + dac_sum(arr[1:])
'''    if len(arr) == 0:
        return 0
    else: 
        return arr[0] + dac_sum(arr[1:])
'''

print(dac_sum([10, 4, 2, 1, 3, 4]))
