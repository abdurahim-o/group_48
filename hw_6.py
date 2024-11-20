def bubble_sort(arr):
    n = len(arr)
    for i in range(n):

                for j in range(0, n-i-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1]


unsorted_list = [7, 9, 28, 8, 10, 13, 5]
print("Список:",)