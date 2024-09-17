import tkinter as tk

def crear_ventana_intro():
    # Crear la ventana Toplevel
    ventana_gram = tk.Toplevel()
    ventana_gram.title("Gramática")
    ventana_gram.geometry("700x450")
    
     # Calcular la posición central
    ventana_gram.update_idletasks()  # Asegurarse de que las dimensiones sean actualizadas
    ventana_gram_width = ventana_gram.winfo_width()
    ventana_gram_height = ventana_gram.winfo_height()
    screen_width = ventana_gram.winfo_screenwidth()
    screen_height = ventana_gram.winfo_screenheight()
    x = (screen_width // 2) - (ventana_gram_width // 2)
    y = (screen_height // 4) - (ventana_gram_height // 4)
    ventana_gram.geometry(f"700x450+{x}+{y}")

    # Crear un marco para el contenido
    marco = tk.Frame(ventana_gram, bg='white')
    marco.pack(fill=tk.BOTH, expand=True)

    # Agregar el título "Gramática"
    titulo = tk.Label(marco, text="Gramática", font=("Times", 24, "bold"), bg='white')
    titulo.pack(pady=10)

    # Crear el texto de introducción
    texto_intro = (
        "La gramática es el conjunto de reglas que rigen el uso de un idioma. Estas reglas abarcan "
        "la estructura de las oraciones, el uso adecuado de palabras y frases, y la correcta concordancia "
        "entre los elementos de la oración.\n\n"
        "En esta sección, exploraremos conceptos clave de la gramática, tales como:\n\n"
        " - Tipos de palabras: Las diferentes categorías de palabras como sustantivos, verbos, adjetivos, etc.\n"
        " - Oraciones: La estructura y componentes de las oraciones, cómo se forman y cómo se utilizan.\n"
        " - Conjugación de verbos: Cómo se conjugan los verbos en diferentes tiempos y modos.\n"
        " - Voz pasiva: Cómo se estructura la voz pasiva en las oraciones y cómo se utiliza para enfatizar el objeto de la acción.\n\n"
        "Comprender estos elementos es fundamental para desarrollar habilidades de comunicación efectivas y precisas."
    )

    # Crear un Label para el texto de introducción
    label_texto = tk.Label(marco, text=texto_intro, font=("Arial", 12), bg='white', justify='left', wraplength=600)
    label_texto.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Botón para cerrar la ventana de introducción
    boton_cerrar = tk.Button(marco, text="Cerrar", command=ventana_gram.destroy)
    boton_cerrar.pack(pady=10)