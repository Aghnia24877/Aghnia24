import time
import random
import matplotlib.pyplot as plt

# Bubble Sort
class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    swapped = True
            if not swapped:
                break
        return self.arr

# Insertion Sort
class InsertionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
        return self.arr

# Selection Sort
class SelectionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
        return self.arr

# Merge Sort
class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self, arr=None):
        if arr is None:
            arr = self.arr

        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.sort(left_half)
            self.sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        return arr

# Quick Sort
class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self, arr=None):
        if arr is None:
            arr = self.arr

        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return self.sort(left) + middle + self.sort(right)

# Fungsi untuk mengukur waktu eksekusi
def measure_time(sort_func):
    start = time.time()
    sort_func()
    end = time.time()
    return (end - start) * 1000

# Dataset random
data = random.sample(range(1000), 500)

# Instansiasi dan pengukuran
times = {
    "BubbleSort": measure_time(lambda: BubbleSort(data.copy()).sort()),
    "InsertionSort": measure_time(lambda: InsertionSort(data.copy()).sort()),
    "SelectionSort": measure_time(lambda: SelectionSort(data.copy()).sort()),
    "MergeSort": measure_time(lambda: MergeSort(data.copy()).sort()),
    "QuickSort": measure_time(lambda: QuickSort(data.copy()).sort())
}

# Visualisasi hasil
plt.figure(figsize=(10, 6))
plt.bar(times.keys(), times.values(), color='skyblue')
plt.ylabel("Waktu Eksekusi (ms)")
plt.title("Perbandingan Efisiensi Algoritma Sorting")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
