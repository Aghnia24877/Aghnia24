def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Pindahkan cakram 1 dari {source} ke {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Pindahkan cakram {n} dari {source} ke {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

# Contoh Penggunaan
n = 3 # Jumlah cakram
tower_of_hanoi(n, 'A', 'B', 'C')