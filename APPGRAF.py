import tkinter as tk
from PIL import Image, ImageTk
import NIVEL1_SUB1
import NIVEL1_SUB2
import NIVEL2_SUB1
import NIVEL2_SUB2
import NIVEL3_SUB1
import NIVEL3_SUB2

def mostrar_subniveles(nivel, subnivel1_nombre, subnivel2_nombre):
    # Crear una nueva ventana para los subniveles
    ventana_subniveles = tk.Toplevel(ventana)
    ventana_subniveles.title(f"Subniveles de {nivel.capitalize()}")
    ventana_subniveles.geometry("600x350")
    
        # Calcular la posición central
    ventana_subniveles.update_idletasks()  # Asegurarse de que las dimensiones sean actualizadas
    ventana_subniveles_width = ventana_subniveles.winfo_width()
    ventana_subniveles_height = ventana_subniveles.winfo_height()
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    x = (screen_width // 2) - (ventana_subniveles_width // 2)
    y = (screen_height // 4) - (ventana_subniveles_height // 4)
    ventana_subniveles.geometry(f"600x350+{x}+{y}")

    # Título de los subniveles
    titulo_subniveles = tk.Label(ventana_subniveles, text=f"Subniveles de {nivel.capitalize()}", font=("Times", 30, "bold"))
    titulo_subniveles.pack(pady=20)
    
    # Cargar y redimensionar la imagen subniveles
    imagen_subniveles = Image.open("IMG/IMG01.jpg")  # ruta imagen
    imagen_subniveles = imagen_subniveles.resize((600, 350))  # Redimensionar la imagen al tamaño de la ventana
    imagen_subniveles_fondo = ImageTk.PhotoImage(imagen_subniveles)
    
    # Crear un label para contener la imagen de fondo
    label_fondo = tk.Label(ventana_subniveles, image=imagen_subniveles_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
        
    # Mantener una referencia a la imagen
    ventana_subniveles.imagen_fondosub = imagen_subniveles_fondo

    # Función para manejar la selección del subnivel
    def seleccionar_subnivel(subnivel):
        if nivel == "nivel_1":
            if subnivel == "subnivel_1":
                NIVEL1_SUB1.crear_ventana_intro()
            elif subnivel == "subnivel_2":
                NIVEL1_SUB2.ventana_tip_palabras()
        elif nivel == "nivel_2":
            if subnivel == "subnivel_1":
                NIVEL2_SUB1.ventana_oraciones()
            elif subnivel == "subnivel_2":
                NIVEL2_SUB2.ventana_principal()
        elif nivel == "nivel_3":
            if subnivel == "subnivel_1":
                NIVEL3_SUB1.ventana_modif()
            elif subnivel == "subnivel_2":
                NIVEL3_SUB2.ventana_voz()
                
    # Crear botones para los subniveles con nombres personalizados
    boton_subnivel_1 = tk.Button(ventana_subniveles, text=subnivel1_nombre, font=("Times", 20), command=lambda: seleccionar_subnivel("subnivel_1"))
    boton_subnivel_1.pack(pady=10)

    boton_subnivel_2 = tk.Button(ventana_subniveles, text=subnivel2_nombre, font=("Times", 20), command=lambda: seleccionar_subnivel("subnivel_2"))
    boton_subnivel_2.pack(pady=10)

def seleccionar_nivel():
    nivel = nivel_seleccionado.get()

    # Nombres personalizados para los subniveles
    if nivel == "nivel_1":
        subnivel1_nombre = "¿Qué es la Gramática?"
        subnivel2_nombre = "Tipos de Palabras"
    elif nivel == "nivel_2":
        subnivel1_nombre = "Estructura de Oraciones"
        subnivel2_nombre = "Tiempos Verbales Básicos"
    elif nivel == "nivel_3":
        subnivel1_nombre = "Oraciones Compuestas"
        subnivel2_nombre = "Voz Pasiva"

    # Mostrar ventana de subniveles
    mostrar_subniveles(nivel, subnivel1_nombre, subnivel2_nombre)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Menú Principal de Niveles")
ventana.geometry("800x600")

    # Calcular la posición central
ventana.update_idletasks()  # Asegurarse de que las dimensiones sean actualizadas
ventana_width = ventana.winfo_width()
ventana_height = ventana.winfo_height()
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()
x = (screen_width // 2) - (ventana_width // 2)
y = (screen_height // 4) - (ventana_height // 4)
ventana.geometry(f"800x600+{x}+{y}")

# Cargar la imagen para la ventana principal
imagen_principal = Image.open("IMG/IMG02.jpg")
imagen_principal = imagen_principal.resize((800, 600))  # Redimensionar la imagen al tamaño de la ventana
imagen_principal_fondo = ImageTk.PhotoImage(imagen_principal)
    
# Crear un label para contener la imagen de fondo en la ventana principal
label_fondo_principal = tk.Label(ventana, image=imagen_principal_fondo)
label_fondo_principal.place(x=0, y=0, relwidth=1, relheight=1)
    
# Mantener una referencia a la imagen
ventana.imagen_fondo = imagen_principal_fondo

# Crear un frame para organizar los widgets
frame = tk.Frame(ventana, bg="light cyan", padx=9, pady=9)
frame.pack(pady=20)

# Añadir un título al menú de niveles
titulo = tk.Label(frame, text=" FunGrammar ", font=("Times", 40, "bold"), bg="azure", relief="groove")
titulo.pack(pady=10)

# Crear las opciones de niveles en burbujas (radio buttons)
nivel_seleccionado = tk.StringVar(value="nivel_1")

tk.Radiobutton(frame, text="Nivel 1 - Primeros Pasos", font=("Times", 30), bg="aquamarine", relief="raised", variable=nivel_seleccionado, value="nivel_1").pack(pady=10, anchor=tk.W)
tk.Radiobutton(frame, text="Nivel 2 - Construye y Aprende", font=("Times", 30), bg="khaki", relief="raised", variable=nivel_seleccionado, value="nivel_2").pack(pady=10, anchor=tk.W)
tk.Radiobutton(frame, text="Nivel 3 - Domina la Gramática", font=("Times", 30), bg="lightblue2", relief="raised", variable=nivel_seleccionado, value="nivel_3").pack(pady=10, anchor=tk.W)

# Crear un botón de "Siguiente"
boton_siguiente = tk.Button(ventana, text="Siguiente", command=seleccionar_nivel, font=("Times", 17, "bold"), bg="bisque", width=8, height=1)
boton_siguiente.pack(pady=20)

# Ejecutar el loop principal de la aplicación
ventana.mainloop()