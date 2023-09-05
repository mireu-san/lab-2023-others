def removeDuplicate(items):
    list1 = []
    for i in items:
        if i not in list1:
            list1.append(i)
    return list1

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicate(nums))