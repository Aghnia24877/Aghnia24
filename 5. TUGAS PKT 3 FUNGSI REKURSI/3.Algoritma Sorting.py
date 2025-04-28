#poin ke-1 Implementasikan Bubble Sort 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False 
        for j in range(0, n - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped  = True
        if not swapped:
            break 
#Uji coba
data = [115, 18, 45, 29, 56, 1, 37]
bubble_sort(data)
print(data)

#poin ke-2 Implementasikan Selection sort dan Bubble Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Uji Coba
data = [115, 18, 45, 29, 56, 1, 37]
selection_sort(data)
print("Hasil pengurutan:", data)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False 
        for j in range(0, n - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped  = True
        if not swapped:
            break 
#Uji coba
data = [115, 18, 45, 29, 56, 1, 37]
bubble_sort(data)
print(data)

#poin 3 Implementasikan Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Uji coba
data = [115, 18, 45, 29, 56, 1, 37]
sorted_data = quick_sort(data)
print(sorted_data)