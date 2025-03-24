def sort_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        if lst[left] == '_':
            while lst[right] == '_' and left < right:
                right -= 1
            lst[left], lst[right] = lst[right], lst[left]
        left += 1
    return lst

lst = [0, 1, 4, '_', 3, 0, '_', '_']
print(sort_list(lst))