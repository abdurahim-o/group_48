def bubble_sort(cristiano):
    n = len(cristiano)
    for i in range(n):
        for i in range(0, n-i-1):
            if cristiano[i] > cristiano[i+1]:
                cristiano[i], cristiano[i+1] = cristiano[i+1], cristiano[i]

    return cristiano

sorted_list = [7, 9, 10, 11, 8]
sorted_list = bubble_sort(sorted_list)
print("Cписок:", sorted_list)


def binary_search(cristiano, x):
    left, right = 0, len(cristiano) - 1

    while left <= right:
        mid = left + (right - left)//2

        if cristiano[mid] == x:
            print(f"Нашел {x} на строчке {mid}")
            return

        elif cristiano[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    print(f"{x} не найден")
    return


element_to_find = 7
binary_search(sorted_list, element_to_find)
