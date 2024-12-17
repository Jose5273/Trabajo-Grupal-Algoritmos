def busqueda_binaria(arr, x):
    inicio = 0
    fin = len(arr) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        
        if arr[medio] == x:
            return True  
        elif arr[medio] < x:
            inicio = medio + 1  
        else:
            fin = medio - 1  
    
    return False 
