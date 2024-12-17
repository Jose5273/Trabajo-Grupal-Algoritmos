def insertion_sort(lista):
    for i in range(1, len(lista)):  # Recorremos desde el segundo elemento hasta el final
        key = lista[i]  # Valor actual que queremos insertar
        j = i - 1  # Posición anterior al índice actual
        
        # Mover elementos mayores al valor de 'key' hacia la derecha
        while j >= 0 and lista[j] > key:
            lista[j + 1] = lista[j]
            j -= 1
        
        # Insertar el valor 'key' en la posición correcta
        lista[j + 1] = key
    
    return lista
