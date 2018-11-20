def countdown(i):
    print(i)
    return None if i <= 0 else countdown(i-1)

num = int(input())

countdown(num)
