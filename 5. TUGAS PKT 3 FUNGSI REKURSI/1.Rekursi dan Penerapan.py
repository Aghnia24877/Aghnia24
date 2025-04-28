#poin ke-1
def faktorial(n) :
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
# Uji coba
print(faktorial(15))

#poin ke-2
def faktorial_i(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil   
print(faktorial_i(15)) 

#poin ke-3
def fibonacci(n) :
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    #Uji coba
print(fibonacci(25))