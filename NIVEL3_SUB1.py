import tkinter as tk
from PIL import Image, ImageTk

def mostrar_concepto():
    concepto_window = tk.Toplevel()
    concepto_window.title("Concepto de Modificadores y Conjunciones")
    concepto_window.geometry("500x450")
    
    concepto_window.update_idletasks()
    concepto_window_width = concepto_window.winfo_width()
    concepto_window_height = concepto_window.winfo_height()
    screen_width = concepto_window.winfo_screenwidth()
    screen_height = concepto_window.winfo_screenheight()
    x = (screen_width // 2) - (concepto_window_width // 2)
    y = (screen_height // 4) - (concepto_window_height // 4)
    concepto_window.geometry(f"500x450+{x}+{y}")
    
    tk.Label(concepto_window,text="Modificadores y Conjunciones", font=("Arial", 12, "bold")).pack(pady=0)

    instrucciones_texto = ("**Modificadores**\n\n""Los modificadores son palabras o grupos de palabras que aportan información adicional sobre "
                      "otros elementos en una oración, como sustantivos o pronombres. Ayudan a enriquecer el significado "
                      "y proporcionar más detalles.\n\n"
                      "Ejemplos:\n"
                      "- 'El gato **negro** duerme.' Aquí, '**negro**' es un modificador que describe al gato.\n"
                      "- 'Ella lleva un vestido **hermoso**.' En este caso, '**hermoso**' modifica al vestido.\n\n"
                      "**Conjunciones**\n\n"
                      "Las conjunciones son palabras que sirven para unir oraciones, frases o palabras dentro de una oración. "
                      "Permiten conectar ideas y establecer relaciones entre diferentes partes del texto.\n\n"
                      "Ejemplos:\n"
                      "- 'Me gusta el café **y** el té.' La conjunción '**y**' une dos elementos de la oración.\n"
                      "- 'Puedes venir **pero** solo si terminas tu tarea.' La conjunción '**pero**' introduce una condición que contrasta con la primera parte.\n\n"
                      "Las conjunciones y los modificadores son esenciales para construir oraciones complejas y claras, facilitando la comunicación efectiva.")

    instrucciones_label = tk.Label(concepto_window, text=instrucciones_texto, wraplength=450)
    instrucciones_label.pack(pady=10)

# ----------- Actividad 1: Completar oraciones con conjunciones -----------
def verificar_respuesta_completar():
    respuestas = {
        "1": "pero",
        "2": "y",
        "3": "porque",
        "4": "o",
        "5": "aunque"
    }
    # Verificar cada oración
    for i in range(1, 6):
        seleccion = opciones[i].get()
        if seleccion == respuestas[str(i)]:
            resultados[i].config(text="¡Correcto!", fg="green")
        else:
            resultados[i].config(text=f"Incorrecto, la respuesta correcta es '{respuestas[str(i)]}'", fg="red")

def iniciar_actividad_completar():
    ventana_actividad_completar = tk.Toplevel()
    ventana_actividad_completar.title("Actividad: Completar Oraciones")
    ventana_actividad_completar.geometry("500x400")
    
    ventana_actividad_completar.update_idletasks()
    ventana_actividad_completar_width = ventana_actividad_completar.winfo_width()
    ventana_actividad_completar_height = ventana_actividad_completar.winfo_height()
    screen_width = ventana_actividad_completar.winfo_screenwidth()
    screen_height = ventana_actividad_completar.winfo_screenheight()
    x = (screen_width // 2) - (ventana_actividad_completar_width // 2)
    y = (screen_height // 4) - (ventana_actividad_completar_height // 4)
    ventana_actividad_completar.geometry(f"500x400+{x}+{y}")

    # Etiqueta de instrucción
    instruccion = tk.Label(ventana_actividad_completar, text="Completa las oraciones eligiendo la conjunción correcta:")
    instruccion.pack()

    oraciones = [
        "1. Me gusta el helado, _____ no me gusta el chocolate.",
        "2. Fui al cine _____ luego cenamos.",
        "3. Estoy cansado _____ trabajé todo el día.",
        "4. Puedes tomar café _____ té.",
        "5. Juan fue a la fiesta _____ estaba cansado."
    ]

    # Crear las oraciones con opciones para completar
    global opciones, resultados
    opciones = {}
    resultados = {}

    respuestas_posibles = [("y", "pero", "porque", "o", "aunque")]

    for i, oracion in enumerate(oraciones, 1):
        oracion_label = tk.Label(ventana_actividad_completar, text=oracion)
        oracion_label.pack()

        opciones[i] = tk.StringVar()
        opciones[i].set(None)

        # Colocar las opciones en horizontal
        frame_opciones = tk.Frame(ventana_actividad_completar)
        frame_opciones.pack()

        for conjuncion in respuestas_posibles[0]:
            conjuncion_button = tk.Radiobutton(frame_opciones, text=conjuncion, variable=opciones[i], value=conjuncion)
            conjuncion_button.pack(side="left")

        resultados[i] = tk.Label(ventana_actividad_completar, text="")
        resultados[i].pack()

    # Botón para verificar la respuesta
    boton_verificar = tk.Button(ventana_actividad_completar, text="Verificar", command=verificar_respuesta_completar)
    boton_verificar.pack()

# ----------- Actividad 2: Identificar conjunciones y modificadores -----------
def verificar_respuesta_identificar():
    respuestas = {
        "1": "pero",
        "2": "y",
        "3": "sin embargo",
        "4": "aunque",
        "5": "además"
    }
    # Verificar las respuestas escritas por el usuario
    for i in range(1, 6):
        seleccion = entradas[i].get().strip().lower()  # Convertir a minúsculas para evitar problemas con mayúsculas
        if seleccion == respuestas[str(i)]:
            resultados[i].config(text="¡Correcto!", fg="green")
        else:
            resultados[i].config(text=f"Incorrecto, la respuesta correcta es '{respuestas[str(i)]}'", fg="red")

def iniciar_actividad_identificar():
    ventana_actividad_identificar = tk.Toplevel()
    ventana_actividad_identificar.title("Actividad: Identificar Conjunciones y Modificadores")
    ventana_actividad_identificar.geometry("500x400")
    
    ventana_actividad_identificar.update_idletasks()
    ventana_actividad_identificar_width = ventana_actividad_identificar.winfo_width()
    ventana_actividad_identificar_height = ventana_actividad_identificar.winfo_height()
    screen_width = ventana_actividad_identificar.winfo_screenwidth()
    screen_height = ventana_actividad_identificar.winfo_screenheight()
    x = (screen_width // 2) - (ventana_actividad_identificar_width // 2)
    y = (screen_height // 4) - (ventana_actividad_identificar_height // 4)
    ventana_actividad_identificar.geometry(f"500x400+{x}+{y}")

    # Etiqueta de instrucción
    instruccion = tk.Label(ventana_actividad_identificar, text="Identifica la conjunción o modificador en cada oración:")
    instruccion.pack()

    oraciones = [
        "1. Me gusta correr, pero me canso rápido.",
        "2. El perro corrió rápidamente y el gato se escondió.",
        "3. No me gusta el chocolate, sin embargo, el helado es mi favorito.",
        "4. Aunque estaba cansado, siguió trabajando.",
        "5. Me gusta el helado, además, el pastel también es delicioso."
    ]

    # Crear las oraciones con una entrada de texto debajo
    global entradas, resultados
    entradas = {}
    resultados = {}

    for i, oracion in enumerate(oraciones, 1):
        oracion_label = tk.Label(ventana_actividad_identificar, text=oracion)
        oracion_label.pack()

        entradas[i] = tk.Entry(ventana_actividad_identificar)
        entradas[i].pack()

        resultados[i] = tk.Label(ventana_actividad_identificar, text="")
        resultados[i].pack()

    # Botón para verificar las respuestas
    boton_verificar = tk.Button(ventana_actividad_identificar, text="Verificar", command=verificar_respuesta_identificar)
    boton_verificar.pack()


# ----------- Ventana principal del programa -----------
def ventana_modif():
    oraciones = tk.Toplevel()
    oraciones.title("Modificadores y COnjunciones")
    oraciones.geometry("501x300")  
    oraciones.resizable(False, False)  

    # Cargar imagen
    img = Image.open("IMG/IMG06.jpg")
    img = img.resize((501, 300))
    img_tk = ImageTk.PhotoImage(img)

    # Calcular la posición central
    oraciones.update_idletasks()
    oraciones_width = oraciones.winfo_width()
    oraciones_height = oraciones.winfo_height()
    screen_width = oraciones.winfo_screenwidth()
    screen_height = oraciones.winfo_screenheight()
    x = (screen_width // 2) - (oraciones_width // 2)
    y = (screen_height // 4) - (oraciones_height // 4)
    oraciones.geometry(f"501x300+{x}+{y}")

    img_label = tk.Label(oraciones, image=img_tk)
    img_label.image = img_tk  
    img_label.place(relwidth=1, relheight=1)  

    # Agregar el texto sobre la imagen
    tk.Label(oraciones, text="Modificadores y conjunciones: Conecta y describe.", font=("Times", 14, "bold"), bg="pink3").pack(pady=10)
    tk.Label(oraciones, text="\nSelecciona una opción para comenzar:\n", font=("arial", 10, "bold"), bg="DarkSlateGray2").pack()

    button_frame = tk.Frame(oraciones)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Modificadores y Conjunciones", command=mostrar_concepto, bg="lightgreen").pack(pady=5)
    tk.Button(button_frame, text="Actividad Identificar", command=iniciar_actividad_identificar, bg="lightgreen").pack(pady=5)
    tk.Button(button_frame, text="Actividad Completar", command=iniciar_actividad_completar, bg="lightgreen").pack(pady=5)