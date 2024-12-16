from tkinter import *
from Bubble_sort import bubble_sort, generar_numeros  # Importar funciones del otro archivo
import time

# Bubble Sort
def ejecutar_bubble_sort():
    cerrar_botones()  # Limpiar botones
    
    label_instrucciones.place(x=160, y=55)
    entry_cantidad.place(x=450, y=55)
    boton_procesar.place(x=160, y=115)
    numeros_generados_label.place(x=160, y=180)
    numeros_ordenados_label.place(x=160, y=300)

    # Función de ordenamiento
    def procesar():
        # Limpiar texto
        advertencia_label.place_forget()
        tiempo_label.place_forget()
        numeros_generados_label.delete(1.0, END)
        numeros_ordenados_label.delete(1.0, END)

        try:
            cantidad = int(entry_cantidad.get())
            if cantidad > 50_000:
                advertencia_label.config(text="ADVERTENCIA: Máximo recomendado es 5,000 números.")
                advertencia_label.place(x=160, y=85)
                return

            # Generar números
            numeros = generar_numeros(cantidad)
            numeros_para_ordenar = numeros.copy()

            # Mostrar números generados
            numeros_generados_label.insert(END, str(numeros))

            # Ordenar los números
            inicio = time.time()
            numeros_ordenados = bubble_sort(numeros_para_ordenar)
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

    # Cerrar los numeros generados
    def cerrar_seccion_numeros():
        label_instrucciones.place_forget()
        entry_cantidad.place_forget()
        boton_procesar.place_forget()
        numeros_generados_label.place_forget()
        numeros_ordenados_label.place_forget()
        advertencia_label.place_forget()
        tiempo_label.place_forget()

    # Botón Buble Sort cierra lo que se abre
    boton_bubble_sort.config(command=cerrar_seccion_numeros)

# Cerrar todo lo referente al Bubble Sort
def cerrar_botones():
    global botones
    for boton in botones:
        boton.place_forget()

# Mostrar el Bubble Sort al pasar el cursor
def mostrar_boton_bubble(event):
    global boton_bubble_sort
    boton_bubble_sort = Button(principal, text="Algoritmo Bubble Sort", width=30, fg="blue", font=("Times New Roman", 12), command=ejecutar_bubble_sort)
    boton_bubble_sort.place(x=160, y=55)
    principal.after(7000, lambda: boton_bubble_sort.place_forget())

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

# Almacenar botones
botones = []

# Ingresar num
label_instrucciones = Label(principal, text="Ingresa la cantidad de números a generar:", font=("Times New Roman", 12))
entry_cantidad = Entry(principal, font=("Times New Roman", 12), width=10)

advertencia_label = Label(principal, text="", font=("Times New Roman", 12), fg="red")
tiempo_label = Label(principal, text="", font=("Times New Roman", 12))

boton_procesar = Button(principal, text="Ejecutar", command=None, width=15, fg="blue", font=("Times New Roman", 12))

numeros_generados_label = Text(principal, wrap=WORD, width=80, height=10, font=("Times New Roman", 10), bg="light grey")
numeros_ordenados_label = Text(principal, wrap=WORD, width=80, height=10, font=("Times New Roman", 10), bg="light grey")

label_opciones = Label(principal, text="Opciones", width=15, fg="blue", relief="flat", font=("Times New Roman", 12))
label_opciones.place(x=5, y=25)

# Botón iterativos
boton_iterativos = Button(principal, text="Iterativos", width=15, fg="green", relief="sunken", font=("Times New Roman", 12))
boton_iterativos.place(x=5, y=55)
boton_iterativos.bind("<Enter>", mostrar_boton_bubble)

raiz.mainloop()

