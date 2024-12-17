from tkinter import *
from Bubble_sort import bubble_sort, generar_numeros 
from Quick_sort import quicksort, generar_numeros
from Insertion_sort import insertion_sort
from Busqueda_binaria import busqueda_binaria
from Busqueda_secuencial import busqueda_secuencial
from Selection_sort import selection_sort
from Heap_sort import heap_sort
import time

botones_algoritmos = []

def ocultar_todos():
    # Lista de widgets que NO deben ocultarse
    widgets_permanentes = [label_opciones, boton_iterativos, boton_recursivos]

    # Ocultar todos los widgets, excepto los permanentes
    for widget in principal.winfo_children():
        if widget not in widgets_permanentes:
            widget.place_forget()

    # Ocultar botones de algoritmos (y limpiar la lista)
    for boton in botones_algoritmos:
        boton.place_forget()
    botones_algoritmos.clear()


# Bubble Sort
def ejecutar_bubble_sort():
    ocultar_todos()  # Oculta cualquier sección previamente abierta

    label_instrucciones.place(x=160, y=55)
    entry_cantidad.place(x=450, y=55)
    boton_procesar.place(x=160, y=115)
    numeros_generados_label.place(x=160, y=180)
    numeros_ordenados_label.place(x=160, y=300)

    # Define la funcionalidad específica de Bubble Sort
    def procesar():
        advertencia_label.place_forget()
        tiempo_label.place_forget()
        numeros_generados_label.delete(1.0, END)
        numeros_ordenados_label.delete(1.0, END)

        try:
            cantidad = int(entry_cantidad.get())
            if cantidad > 50_000:
                advertencia_label.config(text="Máximo recomendado es 50,000 números.")
                advertencia_label.place(x=160, y=85)
                return

            numeros = generar_numeros(cantidad)
            numeros_generados_label.insert(END, str(numeros))

            inicio = time.time()
            numeros_ordenados = bubble_sort(numeros)
            fin = time.time()

            numeros_ordenados_label.insert(END, str(numeros_ordenados))
            tiempo_label.config(text=f"Tiempo de ordenamiento: {fin - inicio:.2f} segundos")
            tiempo_label.place(x=160, y=450)

        except ValueError:
            advertencia_label.config(text="ERROR: Ingresa un número válido.")
            advertencia_label.place(x=160, y=85)


    boton_procesar.config(command=procesar)

        
# Quick Sort

def ejecutar_quicksort():
    ocultar_todos()
    
    label_instrucciones.place(x=160, y=55)
    entry_cantidad.place(x=450, y=55)
    boton_procesar.place(x=160, y=115)
    numeros_generados_label.place(x=160, y=180)
    numeros_ordenados_label.place(x=160, y=300)

    def procesar():
        advertencia_label.place_forget()
        tiempo_label.place_forget()
        numeros_generados_label.delete(1.0, END)
        numeros_ordenados_label.delete(1.0, END)

        try:
            cantidad = int(entry_cantidad.get())
            if cantidad > 50_000:
                advertencia_label.config(text="Máximo recomendado es 50,000 números.")
                advertencia_label.place(x=160, y=85)
                return

            numeros = generar_numeros(cantidad)
            numeros_generados_label.insert(END, str(numeros))

            inicio = time.time()
            numeros_ordenados = bubble_sort(numeros)
            fin = time.time()

            numeros_ordenados_label.insert(END, str(numeros_ordenados))
            tiempo_label.config(text=f"Tiempo de ordenamiento: {fin - inicio:.2f} segundos")
            tiempo_label.place(x=160, y=450)

        except ValueError:
            advertencia_label.config(text="ERROR: Ingresa un número válido.")
            advertencia_label.place(x=160, y=85)
    boton_procesar.config(command=procesar)
       
# Insertion Sort
def ejecutar_insertion_sort():
    ocultar_todos()

    label_instrucciones.place(x=160, y=55)
    entry_cantidad.place(x=450, y=55)
    boton_procesar.place(x=160, y=115)
    numeros_generados_label.place(x=160, y=180)
    numeros_ordenados_label.place(x=160, y=300)

    def procesar():
        advertencia_label.place_forget()
        tiempo_label.place_forget()
        numeros_generados_label.delete(1.0, END)
        numeros_ordenados_label.delete(1.0, END)

        try:
            cantidad = int(entry_cantidad.get())
            if cantidad > 100_000:
                advertencia_label.config(text="Máximo recomendado es 50,000 números.")
                advertencia_label.place(x=160, y=85)
                return

            # Generar números
            numeros = generar_numeros(cantidad)
            numeros_para_ordenar = numeros.copy()

            # Mostrar números generados
            numeros_generados_label.insert(END, str(numeros))

            # Ordenar los números con Insertion Sort
            inicio = time.time()
            numeros_ordenados = insertion_sort(numeros_para_ordenar)
            fin = time.time()

            # Mostrar números ordenados
            numeros_ordenados_label.insert(END, str(numeros_ordenados))

            # Mostrar tiempo de ejecución
            tiempo_label.config(text=f"Tiempo de ordenamiento: {fin - inicio:.2f} segundos")
            tiempo_label.place(x=160, y=450)

        except ValueError:
            advertencia_label.config(text="ERROR: Ingresa un número válido.")
            advertencia_label.place(x=160, y=85)

    boton_procesar.config(command=procesar)

#Busqueda Secuencial    
def ejecutar_busqueda_secuencial():
    ocultar_todos()
    
    label_instrucciones.place(x=160, y=55)
    entry_cantidad.place(x=450, y=55)
    boton_procesar.place(x=160, y=115)
    numeros_generados_label.place(x=160, y=180)
    numeros_ordenados_label.place(x=160, y=300)

    def procesar():
        advertencia_label.place_forget()
        tiempo_label.place_forget()
        numeros_generados_label.delete(1.0, END)
        numeros_ordenados_label.delete(1.0, END)

        try:
            cantidad = int(entry_cantidad.get())
            if cantidad > 50_000:
                advertencia_label.config(text="Máximo recomendado es 50,000 números.")
                advertencia_label.place(x=160, y=85)
                return

            numeros = generar_numeros(cantidad)
            numeros_generados_label.insert(END, str(numeros))

            inicio = time.time()
            numeros_ordenados = busqueda_secuencial(numeros) 
            fin = time.time()

            numeros_ordenados_label.insert(END, str(numeros_ordenados))
            tiempo_label.config(text=f"Tiempo de ordenamiento: {fin - inicio:.2f} segundos")
            tiempo_label.place(x=160, y=450)

        except ValueError:
            advertencia_label.config(text="ERROR: Ingresa un número válido.")
            advertencia_label.place(x=160, y=85)

    boton_procesar.config(command=procesar)

def ejecutar_selection_sort():
    ocultar_todos()

    label_instrucciones.place(x=160, y=55)
    entry_cantidad.place(x=450, y=55)
    boton_procesar.place(x=160, y=115)
    numeros_generados_label.place(x=160, y=180)
    numeros_ordenados_label.place(x=160, y=300)

    def procesar():
        advertencia_label.place_forget()
        tiempo_label.place_forget()
        numeros_generados_label.delete(1.0, END)
        numeros_ordenados_label.delete(1.0, END)

        try:
            cantidad = int(entry_cantidad.get())
            if cantidad > 50_000:
                advertencia_label.config(text="Máximo recomendado es 50,000 números.")
                advertencia_label.place(x=160, y=85)
                return

            numeros = generar_numeros(cantidad)
            numeros_generados_label.insert(END, str(numeros))

            inicio = time.time()
            numeros_ordenados = selection_sort(numeros)  # Asegúrate de definir el algoritmo Selection Sort
            fin = time.time()

            numeros_ordenados_label.insert(END, str(numeros_ordenados))
            tiempo_label.config(text=f"Tiempo de ordenamiento: {fin - inicio:.2f} segundos")
            tiempo_label.place(x=160, y=450)

        except ValueError:
            advertencia_label.config(text="ERROR: Ingresa un número válido.")
            advertencia_label.place(x=160, y=85)

    boton_procesar.config(command=procesar)

def ejecutar_heap_sort():
    ocultar_todos()

    label_instrucciones.place(x=160, y=55)
    entry_cantidad.place(x=450, y=55)
    boton_procesar.place(x=160, y=115)
    numeros_generados_label.place(x=160, y=180)
    numeros_ordenados_label.place(x=160, y=300)

    def procesar():
        advertencia_label.place_forget()
        tiempo_label.place_forget()
        numeros_generados_label.delete(1.0, END)
        numeros_ordenados_label.delete(1.0, END)

        try:
            cantidad = int(entry_cantidad.get())
            if cantidad > 50_000:
                advertencia_label.config(text="Máximo recomendado es 50,000 números.")
                advertencia_label.place(x=160, y=85)
                return

            numeros = generar_numeros(cantidad)
            numeros_generados_label.insert(END, str(numeros))

            inicio = time.time()
            numeros_ordenados = heap_sort(numeros)  # Asegúrate de definir el algoritmo Heap Sort
            fin = time.time()

            numeros_ordenados_label.insert(END, str(numeros_ordenados))
            tiempo_label.config(text=f"Tiempo de ordenamiento: {fin - inicio:.2f} segundos")
            tiempo_label.place(x=160, y=450)

        except ValueError:
            advertencia_label.config(text="ERROR: Ingresa un número válido.")
            advertencia_label.place(x=160, y=85)

    boton_procesar.config(command=procesar)
    
# Búsqueda Binaria
def ejecutar_busqueda_binaria():
    ocultar_todos()

    label_instrucciones.place(x=160, y=55)
    entry_cantidad.place(x=450, y=55)
    boton_procesar.place(x=160, y=115)
    numeros_generados_label.place(x=160, y=180)

    def procesar():
        advertencia_label.place_forget()
        tiempo_label.place_forget()
        numeros_generados_label.delete(1.0, END)

        try:
            cantidad = int(entry_cantidad.get())
            if cantidad > 1_000_000:
                advertencia_label.config(text="Máximo recomendado es 1,000,000 números.")
                advertencia_label.place(x=160, y=85)
                return

            # Generar y ordenar números para la búsqueda
            numeros = sorted(generar_numeros(cantidad))
            numeros_generados_label.insert(END, str(numeros))

            # Preguntar número a buscar
            numero_a_buscar = int(entry_busqueda.get())

            # Realizar búsqueda binaria
            inicio = time.time()
            encontrado = busqueda_binaria(numeros, numero_a_buscar)
            fin = time.time()

            # Mostrar resultado
            resultado = f"Número {'encontrado' if encontrado else 'no encontrado'} en el arreglo."
            tiempo_label.config(text=f"{resultado}\nTiempo de búsqueda: {fin - inicio:.6f} segundos")
            tiempo_label.place(x=160, y=450)

        except ValueError:
            advertencia_label.config(text="ERROR: Ingresa un número válido.")
            advertencia_label.place(x=160, y=85)

    boton_procesar.config(command=procesar)

    # Elemento adicional para ingresar el número a buscar
    label_busqueda.place(x=160, y=85)
    entry_busqueda.place(x=450, y=85)

# Mostrar botones de algoritmos iterativos (Bubble Sort e Insertion Sort)
def mostrar_botones_iterativos(event):
    ocultar_todos()
    global boton_bubble_sort, boton_insertion_sort
    boton_bubble_sort = Button(principal, text="Algoritmo Bubble Sort", width=30, fg="blue", font=("Times New Roman", 12), command=ejecutar_bubble_sort)
    boton_insertion_sort = Button(principal, text="Algoritmo Insertion Sort", width=30, fg="blue", font=("Times New Roman", 12), command=ejecutar_insertion_sort)
    boton_busqueda_secuencial = Button(principal, text="Algoritmo Merge Sort", width=30, fg="blue", font=("Times New Roman", 12), command=ejecutar_busqueda_secuencial)  # Nueva función
    boton_selection_sort = Button(principal, text="Algoritmo Selection Sort", width=30, fg="blue", font=("Times New Roman", 12), command=ejecutar_selection_sort)  # Nueva función
    boton_heap_sort = Button(principal, text="Algoritmo Heap Sort", width=30, fg="blue", font=("Times New Roman", 12), command=ejecutar_heap_sort)  # Nueva función
    
    # Colocar botones
    boton_bubble_sort.place(x=160, y=55)
    boton_insertion_sort.place(x=160, y=85)
    boton_busqueda_secuencial.place(x=160, y=115)  # Botón Merge Sort
    boton_selection_sort.place(x=160, y=145)  # Botón Selection Sort
    boton_heap_sort.place(x=160, y=175)  # Botón Heap Sort

    # Agregar botones a la lista global
    botones_algoritmos.extend([boton_bubble_sort, boton_insertion_sort, boton_busqueda_secuencial, boton_selection_sort, boton_heap_sort])

def mostrar_botones_recursivos(event):
    ocultar_todos()
    global boton_quicksort, boton_busqueda_binaria
    boton_quicksort = Button(principal, text="Algoritmo QuickSort", width=30, fg="blue", font=("Times New Roman", 12), command=ejecutar_quicksort)
    boton_busqueda_binaria = Button(principal, text="Búsqueda Binaria", width=30, fg="blue", font=("Times New Roman", 12), command=ejecutar_busqueda_binaria)

    # Colocar botones
    boton_quicksort.place(x=160, y=55)
    boton_busqueda_binaria.place(x=160, y=85)

    # Agregar botones a la lista global
    botones_algoritmos.extend([boton_quicksort, boton_busqueda_binaria])

# Ventana principal
raiz = Tk()
raiz.title("Algoritmos de Ordenamiento")
raiz.iconbitmap("TrabajoGrupal/signetofdeliverance.ico")
raiz.config(bg="white")
raiz.geometry("800x600")
raiz.resizable(False, False)

# Configuración del menú
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Como usar el programa")
ayudaMenu.add_command(label="Algoritmos disponibles")
ayudaMenu.add_command(label="Integrantes de Grupo")
ayudaMenu.add_command(label="Salir", command=raiz.quit)

barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

principal = Frame(raiz, width=800, height=550, bg="light blue", bd=0, cursor="hand2")
principal.pack(fill="x", expand=True)

# Detectar clics en cualquier lugar del principal
principal.bind("<Button-1>", lambda event: ocultar_todos())

# Almacenar botones
botones = []

# Ingresar num
label_instrucciones = Label(principal, text="Ingresa la cantidad de números a generar:", font=("Times New Roman", 12))
entry_cantidad = Entry(principal, font=("Times New Roman", 12), width=10)

advertencia_label = Label(principal, text="", font=("Times New Roman", 12), fg="red")
tiempo_label = Label(principal, text="", font=("Times New Roman", 12))

boton_procesar = Button(principal, text="Ejecutar", width=15, fg="blue", font=("Times New Roman", 12))

numeros_generados_label = Text(principal, wrap=WORD, width=80, height=10, font=("Times New Roman", 10), bg="light grey")
numeros_ordenados_label = Text(principal, wrap=WORD, width=80, height=10, font=("Times New Roman", 10), bg="light grey")

label_opciones = Label(principal, text="Opciones", width=15, fg="blue", relief="flat", font=("Times New Roman", 12))
label_opciones.place(x=5, y=25)

boton_iterativos = Button(principal, text="Iterativos", width=15, fg="green", relief="sunken", font=("Times New Roman", 12))
boton_iterativos.place(x=5, y=55)

boton_recursivos = Button(principal, text="Recursivos", width=15, fg="green", relief="sunken", font=("Times New Roman", 12))
boton_recursivos.place(x=5, y=85)

# Modificación en los botones iniciales
boton_iterativos.bind("<Enter>", mostrar_botones_iterativos)

# Modificación en los botones iniciales
boton_recursivos.bind("<Enter>", mostrar_botones_recursivos)

# Elementos para la búsqueda binaria
label_busqueda = Label(principal, text="Número a buscar:", font=("Times New Roman", 12))
entry_busqueda = Entry(principal, font=("Times New Roman", 12), width=10)

raiz.mainloop()
