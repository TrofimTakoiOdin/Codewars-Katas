def digitalRoot(num):
    num = str(num)
    digit_sum = 0
    while len(num) != 1:
        num = sum(list(map(int, num)))
        num = str(num)
    return num

k = digitalRoot(942)
print(k)