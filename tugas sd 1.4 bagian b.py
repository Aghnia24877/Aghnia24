def big_o_n_n2(n):
    # Bagian O(n) - Loop berjalan sebanyak n kali
    for i in range(n):
        print(f"O(n) - Iterasi ke-{i+1}")
    
    # Bagian O(n^2) - Loop bersarang berjalan sebanyak n^2 kali
    for i in range(n):
        for j in range(n):
            print(f"O(n^2) - Iterasi ke-{i+1},{j+1}")

# Contoh pemanggilan fungsi
n = 3  # Bisa diganti dengan nilai lain
big_o_n_n2(n)