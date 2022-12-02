#  Codewars Kata 6 kyu
# https://www.codewars.com/kata/59fa8e2646d8433ee200003f/train/python

def bitCount(num):
    return bin(num)[2:].count("1")


def sort_by_bit(lst):
    lst.sort(key=lambda x: bitCount(x))
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            x, y = bin(lst[i])[2:].count("1"), bin(lst[j])[2:].count("1")
            if lst[i] > lst[j] and x == y:
                lst[i], lst[j] = lst[j], lst[i]
            if lst[i] == lst[j] and x > y:
                lst[i], lst[j] = lst[j], lst[i]
            if lst[i] < lst[j] and x > y:
                lst[i], lst[j] = lst[j], lst[i]

    return lst

arr = [9, 4, 5, 3, 5, 7, 2, 56, 8, 2, 6, 8, 0]
print(sort_by_bit(arr))

# Нашел более разумное решение на форуме:

# def sort_by_bit(arr):
#     arr.sort(key=lambda x:(bin(x).count('1'), x))   # they wanted to modify the input

    # return arr