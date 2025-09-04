x = int(input())
while x > 1:
    if x % 2:
        x *= 3
        x += 1
    else:
        x //= 2
    print(x)