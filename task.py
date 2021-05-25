
def quick_sort(username_password):
    length = len(username_password)
    if length <= 1:
        return username_password
    else:
        pivot = username_password.pop()

    items_greater = []
    items_lower = []

    for item in username_password:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

arr = [42, 12, 13, 89, 63, 11]
print("The array is:")
print(quick_sort(arr))
