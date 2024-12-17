import random

def bubble_sort(lista):
    
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def generar_numeros(cantidad, minimo=0, maximo=1_000_000):
    
    return [random.randint(minimo, maximo) for _ in range(cantidad)]
