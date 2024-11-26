print("sistem manajemen stok barang")
stokbarang = 100
def kurangistok(jumlah):
    global stokbarang
    if jumlah > stokbarang:
        print("stok tidak mencukupi")
        return
    else:
        stokbarang -= jumlah
        return stokbarang
    
while True:
    z =int(input("masukkan jumlah barang yang ingin dikurangi: "))
    print(f"{z} barang telah terjual", "stok total:",kurangistok(z))
    r =input("apakah anda ingin melanjutkan transaksi? (ya/tidak)")
    if r ==("ya"):
        True
    else:
        print("Transaksi selesai. Terima Kasih!")
        break