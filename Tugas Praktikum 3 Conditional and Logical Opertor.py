usia = int(input("masukan usia anda: "))
darah = int(input("masukan tekanan darah anda: "))

if usia >= 60 and darah > 140:
    print("status kesehatan tinggi")
elif usia >=60 and darah <= 140:
    print("status kesehtan normal")
elif usia < 60 and darah > 130:
    print("status kesehatan tinggi")
elif usia <60 and darah <= 130:
    print("status kesehatan normal")