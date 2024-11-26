nilai = int(input("masukan nilai ujian anda (0-100): "))
if 100 >= nilai >= 90:
    print("feedback: sangat baik")
elif 89 >= nilai >= 80:
    print("feedback: baik")
elif 79 >= nilai >= 70:
    print("feedback: cukup")
elif 69 >= nilai >= 60:
    print("feedback: kurang")
else:
    print("feedback: sangat kurang")