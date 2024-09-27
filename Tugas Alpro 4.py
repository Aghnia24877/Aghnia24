print("""menu pizza
      size          topping 
      kecil         paperoni
      sedang        jamur
      besar         sosis

      crust
      pan crust
      cheesy bite crust
      chili cheesy stuffed crust
""")

print("pilih ukuran pizza")
size =input()
print("masukkan toping")
toping =input()
print("pilih crust")
rasa =input()
print("tambahkan keju")
cheese =input()

bil=0
if size =="kecil":
    bil +=50000
elif size =="sedang":
    bil +=60000
elif size =="besar":
    bil +=75000
else:
    print()

if toping =="paperoni":
    bil +=10000
elif toping =="jamur":
    bil +=20000
elif toping =="sosis":
    bil +=30000
else:
    print()

if rasa =="pan crust":
    bil +=40000
elif rasa =="cheesy bite crust":
    bil +=45000
elif rasa =="chili cheesy stuffed crust":
    bil +=50000
else:
    print()

if cheese=="y":
    bil +=10000

print("total pesanan anda = Rp", bil)