
def binary_search(array, key):
    print(array, len(array))
    if len(array) == 1:
        if array[0] == key:
            return 1
        else:
            return -1
    else:
        mid = len(array)//2
        if array[mid] > key:
            return binary_search(array[:mid], key)
        if array[mid] == key:
            return 1
        else:
            return binary_search(array[mid:], key)



result = binary_search([1, 10, 12, 13, 14], 12)
print(result)