#Modifikasi program Fibonacci menggunakan konsep class dan method
class Fibonacci:
    def generate(self, n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        else:
            list_fib = [0, 1]
            while len(list_fib) < n:
                next_fib = list_fib[-1] + list_fib[-2]
                list_fib.append(next_fib)
            return list_fib

#Contoh penggunaan
fibonacci_generator = Fibonacci()
jumlah_bilangan = 15
deret_fibonacci = fibonacci_generator.generate(jumlah_bilangan)
print(f"Deret Fibonacci ({jumlah_bilangan} bilangan): {deret_fibonacci}")

import time
class Sorting:
    def bubble_sort(self, data):
        n = len(data)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

    def insertion_sort(self, data):
        n = len(data)
        for i in range(1, n):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        return data

    def selection_sort(self, data):
        n = len(data)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if data[j] < data[min_index]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
        return data

    def bubble_sort_descending(self, data):
        n = len(data)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if data[j] < data[j + 1]: 
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

    def insertion_sort_descending(self, data):
        n = len(data)
        for i in range(1, n):
            key = data[i]
            j = i - 1
            while j >= 0 and key > data[j]: 
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        return data

    def selection_sort_descending(self, data):
        n = len(data)
        for i in range(n):
            max_index = i 
            for j in range(i + 1, n):
                if data[j] > data[max_index]: 
                    max_index = j
            data[i], data[max_index] = data[max_index], data[i]
        return data

# Contoh penggunaan
sorting_algorithms = Sorting()
data_acak = [12, 14, 10, 24, 9]

print("Data Awal:", data_acak)

print("Bubble Sort (Ascending):", sorting_algorithms.bubble_sort(data_acak.copy()))
print("Insertion Sort (Ascending):", sorting_algorithms.insertion_sort(data_acak.copy()))
print("Selection Sort (Ascending):", sorting_algorithms.selection_sort(data_acak.copy()))

print("Bubble Sort (Descending):", sorting_algorithms.bubble_sort_descending(data_acak.copy()))
print("Insertion Sort (Descending):", sorting_algorithms.insertion_sort_descending(data_acak.copy()))
print("Selection Sort (Descending):", sorting_algorithms.selection_sort_descending(data_acak.copy()))

# Bandingkan waktu eksekusi antara algoritma sorting menggunakan OOP dan tanpa OOP
def bubble_sort_non_oop(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

data_uji = list(range(1000, 0, -1))

# Pengukuran waktu dengan OOP
sorting_oop = Sorting()
start_time_oop = time.time()
sorting_oop.bubble_sort(data_uji.copy())
end_time_oop = time.time()
waktu_oop = end_time_oop - start_time_oop

# Pengukuran waktu tanpa OOP
start_time_non_oop = time.time()
bubble_sort_non_oop(data_uji.copy())
end_time_non_oop = time.time()
waktu_non_oop = end_time_non_oop - start_time_non_oop

print(f"Waktu Eksekusi (OOP): {waktu_oop:.6f} detik")
print(f"Waktu Eksekusi (Tanpa OOP): {waktu_non_oop:.6f} detik")