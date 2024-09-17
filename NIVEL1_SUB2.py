import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def ventana_tip_palabras():
    global tip_palabras
    tip_palabras = tk.Toplevel()
    tip_palabras.title("Juego de Conjugación de Verbos en Español")
    tip_palabras.geometry("501x300")  
    tip_palabras.resizable(False, False)  

    # Cargar imagen
    img = Image.open("IMG/IMG03.jpg")
    img = img.resize((501, 300))
    img_tk = ImageTk.PhotoImage(img)

    # Calcular la posición central
    tip_palabras.update_idletasks()
    tip_palabras_width = tip_palabras.winfo_width()
    tip_palabras_height = tip_palabras.winfo_height()
    screen_width = tip_palabras.winfo_screenwidth()
    screen_height = tip_palabras.winfo_screenheight()
    x = (screen_width // 2) - (tip_palabras_width // 2)
    y = (screen_height // 4) - (tip_palabras_height // 4)
    tip_palabras.geometry(f"501x300+{x}+{y}")

    img_label = tk.Label(tip_palabras, image=img_tk)
    img_label.image = img_tk  
    img_label.place(relwidth=1, relheight=1)  

    # Agregar el texto sobre la imagen
    tk.Label(tip_palabras, text="Tipos de palabras: sustantivos, verbos y más", font=("Times", 14, "bold"), bg="light blue").pack(pady=10)
    tk.Label(tip_palabras, text="\nSelecciona una opción para comenzar:\n", font=("arial", 10, "bold"), bg="gold").pack(pady=10)

    button_frame = tk.Frame(tip_palabras, bg='IndianRed1')
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Tipos de Palabras", command=ventana_explicacion_palabras, bg="lightgreen").pack(pady=5)
    tk.Button(button_frame, text="Actividad Completar Oraciones", command=ventana_completar_oraciones, bg="lightgreen").pack(pady=5)
    tk.Button(button_frame, text="Actividad Crucigrama", command=abrir_crucigrama, bg="lightgreen").pack(pady=5)

def ventana_explicacion_palabras():
    explicacion_palabras = tk.Toplevel(tip_palabras)
    explicacion_palabras.title("Tipos de Palabras - Explicación")
    explicacion_palabras.geometry("700x500")
    
    # Calcular la posición central
    explicacion_palabras.update_idletasks()  # Asegurarse de que las dimensiones sean actualizadas
    explicacion_palabras_width = explicacion_palabras.winfo_width()
    explicacion_palabras_height = explicacion_palabras.winfo_height()
    screen_width = explicacion_palabras.winfo_screenwidth()
    screen_height = explicacion_palabras.winfo_screenheight()
    x = (screen_width // 2) - (explicacion_palabras_width // 2)
    y = (screen_height // 4) - (explicacion_palabras_height // 4)
    explicacion_palabras.geometry(f"700x500+{x}+{y}")

    # Crear un Frame con Canvas para permitir el desplazamiento
    frame = tk.Frame(explicacion_palabras)
    frame.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    scrollable_frame = tk.Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    tk.Label(scrollable_frame, text="Tipos de Palabras", font=("Arial", 12, "bold")).pack(pady=0)

    # Texto de la explicación en un Label
    texto_explicacion = """
    Existen varios tipos de palabras en español:
    
    1. Sustantivos: Nombres de cosas, personas, animales o lugares.
       Ej: casa, perro, Juan.
       
    2. Adjetivos: Palabras que describen a los sustantivos.
       Ej: grande, hermoso, rápido.
       
    3. Verbos: Expresan acciones o estados.
       Ej: correr, ser, hablar.
    
    4. Adverbios: Modifican verbos, adjetivos o adverbios.
       Ej: rápidamente, muy, ayer.
    
    5. Preposiciones: Relacionan elementos en la oración.
       Ej: en, de, con.
       
    6. Conjunciones: Enlazan oraciones o palabras.
       Ej: y, o, pero.
    
    7. Pronombres: Reemplazan al sustantivo.
       Ej: él, ella, nosotros.
       
    ¡Es importante conocer estos tipos de palabras para mejorar nuestra gramática y conjugación!
    """

    # Colocar el texto dentro de un Label con desplazamiento
    label_texto = tk.Label(scrollable_frame, text=texto_explicacion, font=("Arial", 12), justify=tk.LEFT)
    label_texto.pack(pady=10, padx=10)

def ventana_completar_oraciones():
    # Diccionario de oraciones con espacios para completar
    oraciones = {
        "El gato _____ en el tejado.": ("salta", "azul", "acostar"),
        "El cielo está muy _____.": ("azul", "saltar", "verde"),  
        "El niño juega con su _____.": ("pelota", "rojo", "canta"), 
        "Ellos _____ a la escuela.": ("van", "carro", "rápido"),    
        "El libro es muy _____.": ("interesante", "caminar", "nube"),
        "La comida _____ deliciosa.": ("es", "comer", "jugar"),   
        "El carro es _____.": ("rojo", "correr", "volar"), 
        "Ella tiene un _____ en el brazo.": ("reloj", "correr", "herida"), 
        "Los perros _____ mucho.": ("ladran", "verde", "grande"),
        "La casa está _____.": ("limpia", "bailar", "grande")         
    }


    # Seleccionar 5 oraciones aleatorias
    oraciones_seleccionadas = random.sample(list(oraciones.keys()), 5)

    def mostrar_oracion(oracion_actual):
        # Crear una nueva ventana para cada oración
        ventana_oracion = tk.Toplevel()
        ventana_oracion.title("Completar Oración")
        ventana_oracion.geometry("400x300")
        ventana_oracion.transient()
        ventana_oracion.grab_set()
        
        # Calcular la posición central
        ventana_oracion.update_idletasks()
        ventana_oracion_width = ventana_oracion.winfo_width()
        ventana_oracion_height = ventana_oracion.winfo_height()
        screen_width = ventana_oracion.winfo_screenwidth()
        screen_height = ventana_oracion.winfo_screenheight()
        x = (screen_width // 2) - (ventana_oracion_width // 2)
        y = (screen_height // 4) - (ventana_oracion_height // 4)
        ventana_oracion.geometry(f"400x300+{x}+{y}")

        # Obtener las opciones para la oración actual
        opciones = list(oraciones[oracion_actual])
        respuesta_correcta = opciones[0]
        random.shuffle(opciones)

        # Mostrar la oración
        tk.Label(ventana_oracion, text=oracion_actual, font=("Arial", 12)).pack(pady=10)

        # Mostrar las opciones como texto en una fila
        opciones_label = tk.Label(ventana_oracion, text=f"Opciones: {', '.join(opciones)}", font=("Arial", 12))
        opciones_label.pack(pady=5)

        # Cuadro de entrada para la respuesta
        respuesta_entry = tk.Entry(ventana_oracion, font=("Arial", 12))
        respuesta_entry.pack(pady=10)

        # Etiqueta para mostrar retroalimentación
        feedback_label = tk.Label(ventana_oracion, text="", font=("Arial", 12))
        feedback_label.pack(pady=10)

        # Función para verificar la respuesta
        def verificar_respuesta():
            if respuesta_entry.get().lower() == respuesta_correcta.lower():
                feedback_label.config(text="¡La respuesta es correcta!", fg="green")
                ventana_oracion.after(1000, lambda: [ventana_oracion.destroy(), mostrar_siguiente_oracion()])  # Mostrar siguiente oración después de 1 segundo
            else:
                feedback_label.config(text=f"La respuesta correcta es: {respuesta_correcta}", fg="red")

        # Función para mostrar la siguiente oración
        def mostrar_siguiente_oracion():
            if oraciones_seleccionadas:
                siguiente_oracion = oraciones_seleccionadas.pop(0)
                mostrar_oracion(siguiente_oracion)  # Mostrar la siguiente oración
            else:
                feedback_label.config(text="¡Has completado todas las oraciones correctamente!", fg="blue")
        
        # Botón para verificar la respuesta
        tk.Button(ventana_oracion, text="Verificar respuesta", command=verificar_respuesta, bg="lightblue").pack(pady=10)

    # Mostrar la primera oración
    if oraciones_seleccionadas:
        mostrar_oracion(oraciones_seleccionadas.pop(0))  # Mostrar la primera oración
        

# Datos del crucigrama
titulo = "****Crucigrama Tipo de Palabras****"
# Pistas Horizontales y Verticales
horizontal = """----Pistas Horizontales----
1) Que siente o muestra alegría
2) Levantar o fabricar una estructura.
3) Gran extensión de agua salada.
4) Que tiene facilidad para aprender y comprender.
5) Elevación natural del terreno."""

vertical = """-----Pistas Verticales----
A) Interpretar letras y palabras escritas.
B) Estar en estado de reposo durante el cual se suspende la actividad consciente.
C) Conjunto de edificios y calles donde habita una gran cantidad de personas.
D) Preparar alimentos para comer.
E) Que se mueve o actúa con gran velocidad.
F) De gran estatura o altura.
G) Cuerpo celeste que brilla en el cielo nocturno."""

palabras_diccionario = {
    "Feliz": {"posicion": (10, 1), "direccion": "H", "pista": 1},
    "Leer": {"posicion": (9, 2), "direccion": "V", "pista": 'A'},
    "Dormir": {"posicion": (6, 4), "direccion": "V", "pista": 'B'},
    "Construir": {"posicion": (7, 3), "direccion": "H", "pista": 2},
    "Oceano": {"posicion": (9, 6), "direccion": "H", "pista": 3},
    "Ciudad": {"posicion": (5, 9), "direccion": "V", "pista": 'C'},
    "Cocinar": {"posicion": (1, 11), "direccion": "V", "pista": 'D'},
    "Inteligente": {"posicion": (4, 11), "direccion": "H", "pista": 4},
    "Montaña": {"posicion": (11, 12), "direccion": "H", "pista": 5},
    "Rapido": {"posicion": (1, 16), "direccion": "V", "pista": 'E'},
    "Alto": {"posicion": (2, 20), "direccion": "V", "pista": 'F'},
    "Estrella": {"posicion": (4, 18), "direccion": "V", "pista": 'G'},
}

def calcular_dimensiones():
    max_fila = max_columna = 0
    for palabra, info in palabras_diccionario.items():
        fila, columna = info["posicion"]
        if info["direccion"] == "H":
            max_fila = max(max_fila, fila)
            max_columna = max(max_columna, columna + len(palabra) - 1)
        elif info["direccion"] == "V":
            max_fila = max(max_fila, fila + len(palabra) - 1)
            max_columna = max(max_columna, columna)
    return max_fila + 1, max_columna + 1

def crear_crucigrama():
    filas, columnas = calcular_dimensiones()
    crucigrama = [[' ']*columnas for _ in range(filas)]
    for palabra, info in palabras_diccionario.items():
        fila, columna = info["posicion"]
        if info["direccion"] == "H":
            for i, letra in enumerate(palabra.upper()):
                crucigrama[fila][columna + i] = letra
        elif info["direccion"] == "V":
            for i, letra in enumerate(palabra.upper()):
                crucigrama[fila + i][columna] = letra
    return crucigrama, filas, columnas

def abrir_crucigrama():
    class CrucigramaApp(tk.Toplevel):
        def __init__(self, master=None):
            super().__init__(master)
            self.title("Crucigrama Tipo de Palabras")
            self.geometry("900x600")
            self.crucigrama, self.filas, self.columnas = crear_crucigrama()
            self.crear_widgets()
            
            # Calcular la posición central
            self.update_idletasks()  # Asegurarse de que las dimensiones sean actualizadas
            self_width = self.winfo_width()
            self_height = self.winfo_height()
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()
            x = (screen_width // 2) - (self_width // 2)
            y = (screen_height // 4) - (self_height // 4)
            self.geometry(f"900x600+{x}+{y}")

        def crear_widgets(self):
            # Título
            tk.Label(self, text=titulo, font=('Helvetica', 14)).pack(pady=10)

            # Pistas
            pistas_frame = tk.Frame(self)
            pistas_frame.pack(pady=5)
            tk.Label(pistas_frame, text=horizontal, font=('Helvetica', 10), justify=tk.LEFT).pack(side=tk.LEFT, padx=10)
            tk.Label(pistas_frame, text=vertical, font=('Helvetica', 10), justify=tk.LEFT).pack(side=tk.LEFT, padx=10)

            # Cuadrícula
            self.frame_crucigrama = tk.Frame(self)
            self.frame_crucigrama.pack(pady=10)
            self.celdas = [[None]*self.columnas for _ in range(self.filas)]
            self.crear_celdas()

            # Botón para validar respuestas
            tk.Button(self, text="Validar", command=self.validar_respuestas).pack(pady=10)
            self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)  # Configurar el cierre de ventana

        def crear_celdas(self):
            # Crear encabezado de números y letras solo en los inicios de las palabras
            for palabra, info in palabras_diccionario.items():
                fila, columna = info["posicion"]
                if info["direccion"] == "H":
                    tk.Label(self.frame_crucigrama, text=info["pista"], font=('Helvetica', 10, 'bold')).grid(row=fila + 1, column=columna, padx=1, pady=1)
                elif info["direccion"] == "V":
                    tk.Label(self.frame_crucigrama, text=info["pista"], font=('Helvetica', 10, 'bold')).grid(row=fila, column=columna + 1, padx=1, pady=1)

            # Crear celdas de la cuadrícula
            for fila in range(self.filas):
                for columna in range(self.columnas):
                    if self.crucigrama[fila][columna] != ' ':
                        entry = tk.Entry(self.frame_crucigrama, width=2, font=('Helvetica', 12), justify='center')
                        entry.grid(row=fila + 1, column=columna + 1, padx=1, pady=1)
                        self.celdas[fila][columna] = entry

        def validar_respuestas(self):
            for palabra, info in palabras_diccionario.items():
                fila, columna = info["posicion"]
                if info["direccion"] == "H":
                    if columna + len(palabra) <= self.columnas:
                        if all(self.celdas[fila][columna + i].get().upper() == letra for i, letra in enumerate(palabra.upper())):
                            for i in range(len(palabra)):
                                self.celdas[fila][columna + i].config(bg='#90EE90')  # Color verde más claro
                        else:
                            for i in range(len(palabra)):
                                self.celdas[fila][columna + i].config(bg='#FFCCCB')  # Color rojo más claro
                elif info["direccion"] == "V":
                    if fila + len(palabra) <= self.filas:
                        if all(self.celdas[fila + i][columna].get().upper() == letra for i, letra in enumerate(palabra.upper())):
                            for i in range(len(palabra)):
                                self.celdas[fila + i][columna].config(bg='#90EE90')  # Color verde más claro
                        else:
                            for i in range(len(palabra)):
                                self.celdas[fila + i][columna].config(bg='#FFCCCB')  # Color rojo más claro

        def cerrar_ventana(self):
            self.destroy()
            
    # Crear la ventana principal oculta
    root = tk.Toplevel()
    root.withdraw()
    
    # Abrir la ventana del crucigrama
    app = CrucigramaApp(master=root)
    app.mainloop()