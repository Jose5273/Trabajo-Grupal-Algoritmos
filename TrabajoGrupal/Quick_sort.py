import random
def quicksort(lista):
    
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[len(lista) // 2]
        menores = [x for x in lista if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista if x > pivote]
        return quicksort(menores) + iguales + quicksort(mayores)
    
def generar_numeros(cantidad, minimo=0, maximo=1_000_000):
    return [random.randint(minimo, maximo) for _ in range(cantidad)]
