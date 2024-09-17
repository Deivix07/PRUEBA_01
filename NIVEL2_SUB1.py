import random
import tkinter as tk
from PIL import Image, ImageTk

def ventana_oraciones():
    global oraciones
    oraciones = tk.Toplevel()
    oraciones.title("Estructura de oraciones")
    oraciones.geometry("501x300")  
    oraciones.resizable(False, False)  

    # Cargar imagen
    img = Image.open("IMG/IMG05.jpg")
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
    tk.Label(oraciones, text="Aprende a estructurar oraciones", font=("Times", 14, "bold"), bg="light blue").pack(pady=10)
    tk.Label(oraciones, text="\nSelecciona una opción para comenzar:\n", font=("arial", 10, "bold"), bg="DarkSlateGray2").pack()

    button_frame = tk.Frame(oraciones, bg="cyan2")
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Oraciones Simples", command=mostrar_concepto, bg="lightgreen").pack(pady=5)
    tk.Button(button_frame, text="Actividad Identificar", command=iniciar_juego, bg="lightgreen").pack(pady=5)
    tk.Button(button_frame, text="Actividad Crucigrama", command=iniciar_juego_ordenar_palabras, bg="lightgreen").pack(pady=5)

def mostrar_concepto():
    concepto_window = tk.Toplevel()
    concepto_window.title("Concepto de Oraciones Simples")
    concepto_window.geometry("500x400")
    
    concepto_window.update_idletasks()
    concepto_window_width = concepto_window.winfo_width()
    concepto_window_height = concepto_window.winfo_height()
    screen_width = concepto_window.winfo_screenwidth()
    screen_height = concepto_window.winfo_screenheight()
    x = (screen_width // 2) - (concepto_window_width // 2)
    y = (screen_height // 4) - (concepto_window_height // 4)
    concepto_window.geometry(f"500x400+{x}+{y}")

    tk.Label(concepto_window,text="Oraciones Simples", font=("Arial", 12, "bold")).pack(pady=0)

    instrucciones_texto = """¡Ahora estudiaremos las oraciones simples!
    
    Una oración simple es como una pequeña idea que tiene todo lo que necesita para que quien la escuche la entienda, por ejemplo:
    
    "Mamá quiero pollo frito."
    
    Aunque mamá te va a decir que no porque en la casa hay sopa, usaste una oración simple y ella te entendió.
    
    Una oración simple tiene tres partes: UN SUJETO, que es de quien se habla, UN VERBO, que es la acción que está realizando y UN COMPLEMENTO, que como su nombre lo dice, nos ayuda a darle más sentido a nuestra oración.
    
    Ejemplo:
    
    'Mi gato come atún'
    El sujeto es tu GATO, el verbo es COME, y el complemento es el ATUN.
    
    'La niña canta en inglés.'
    Aquí LA NIÑA es el sujeto, CANTA es lo que hace y EN INGLES, el complemento, que como ves no es indispensable pero sí nos aporta en la oración."""

    instrucciones_label = tk.Label(concepto_window, text=instrucciones_texto, wraplength=450)
    instrucciones_label.pack(pady=10)

def iniciar_juego():
    juego_window = tk.Toplevel()
    juego_window.title("Juego de Oraciones Simples")
    juego_window.geometry("500x300")
    juego_window.attributes('-topmost', True)  # Mantener la ventana siempre al frente

    juego_window.update_idletasks()
    juego_window_width = juego_window.winfo_width()
    juego_window_height = juego_window.winfo_height()
    screen_width = juego_window.winfo_screenwidth()
    screen_height = juego_window.winfo_screenheight()
    x = (screen_width // 2) - (juego_window_width // 2)
    y = (screen_height // 4) - (juego_window_height // 4)
    juego_window.geometry(f"500x300+{x}+{y}")

    # Crear frames para la actividad
    preguntas_frame = tk.Frame(juego_window)
    preguntas_frame.pack(pady=10)

    resultado_frame = tk.Frame(juego_window)
    resultado_frame.pack(pady=10)

    # Labels y cuadros de entrada
    pregunta_label = tk.Label(preguntas_frame, text="", wraplength=450)
    pregunta_label.pack()

    sujeto_label = tk.Label(preguntas_frame, text="¿Cuál es el sujeto?")
    sujeto_label.pack()
    sujeto_entry = tk.Entry(preguntas_frame)
    sujeto_entry.pack()

    verbo_label = tk.Label(preguntas_frame, text="¿Cuál es el verbo?")
    verbo_label.pack()
    verbo_entry = tk.Entry(preguntas_frame)
    verbo_entry.pack()

    complemento_label = tk.Label(preguntas_frame, text="¿Cuál es el complemento?")
    complemento_label.pack()
    complemento_entry = tk.Entry(preguntas_frame)
    complemento_entry.pack()

    resultado_label = tk.Label(resultado_frame, text="", wraplength=450)
    resultado_label.pack(pady=10)

    # Variables del juego
    contador_preguntas = 0
    max_preguntas = 5  # Mostrar 5 oraciones

    faciles = {
        "sujeto": ["El perro", "El gato", "El tigre", "El tiburón", "La ballena", "El dragón"],
        "verbo": ["come", "muerde", "lame", "mira", "encontró"],
        "complemento": ["un hueso", "la carne", "un trapo", "un conejo"],
    }

    medias = {
        "sujeto": ["Andrea", "Alejandro", "Dayana", "Joel", "Ana", "Mateo"],
        "verbo": ["mira", "dibuja", "arregla", "rompió", "encontró", "compró"],
        "complemento": ["la televisión", "un libro", "un dibujo", "la cocina"],
    }

    # Crear el botón de verificar solo una vez
    check_button = tk.Button(preguntas_frame, text="Verificar Respuestas")
    check_button.pack(pady=10)

    def mostrar_pregunta():
        nonlocal contador_preguntas

        if contador_preguntas >= max_preguntas:
            resultado_label.config(text="¡Has completado todas las preguntas!", fg="black")
            check_button.pack_forget()  # Ocultar el botón cuando se termine
            return

        oraciones = []

        suj = random.choice(faciles["sujeto"])
        verb = random.choice(faciles["verbo"])
        comp = random.choice(faciles["complemento"])
        oraciones.append({"oracion": f"{suj} {verb} {comp}.", "sujeto": suj, "verbo": verb, "complemento": comp})

        sujb = random.choice(medias["sujeto"])
        verbb = random.choice(medias["verbo"])
        compb = random.choice(medias["complemento"])
        oraciones.append({"oracion": f"{sujb} {verbb} {compb}.", "sujeto": sujb, "verbo": verbb, "complemento": compb})

        oracion_actual = random.choice(oraciones)
        pregunta_label.config(text=oracion_actual["oracion"])

        sujeto_entry.delete(0, tk.END)
        verbo_entry.delete(0, tk.END)
        complemento_entry.delete(0, tk.END)

        def verificar_respuestas():
            nonlocal contador_preguntas

            sujeto = sujeto_entry.get()
            verbo = verbo_entry.get()
            complemento = complemento_entry.get()

            correcta = True
            resultado_text = ""

            if sujeto != oracion_actual["sujeto"]:
                correcta = False
                resultado_text += f"El sujeto correcto es: {oracion_actual['sujeto']}\n"

            if verbo != oracion_actual["verbo"]:
                correcta = False
                resultado_text += f"El verbo correcto es: {oracion_actual['verbo']}\n"

            if complemento != oracion_actual["complemento"]:
                correcta = False
                resultado_text += f"El complemento correcto es: {oracion_actual['complemento']}\n"

            if correcta:
                resultado_label.config(text="¡Respuesta correcta!", fg="green")
                contador_preguntas += 1
                juego_window.after(2000, mostrar_pregunta)  # Espera 2 segundos antes de mostrar la siguiente oración
            else:
                resultado_label.config(text=resultado_text, fg="red")

        check_button.config(command=verificar_respuestas)  # Actualizar el comando del botón para verificar respuestas

    mostrar_pregunta()
    
def iniciar_juego_ordenar_palabras():
    juego_window = tk.Toplevel()
    juego_window.title("Ordenar Palabras")
    juego_window.geometry("500x300")
    juego_window.attributes('-topmost', True)  # Mantener la ventana siempre al frente

    juego_window.update_idletasks()
    juego_window_width = juego_window.winfo_width()
    juego_window_height = juego_window.winfo_height()
    screen_width = juego_window.winfo_screenwidth()
    screen_height = juego_window.winfo_screenheight()
    x = (screen_width // 2) - (juego_window_width // 2)
    y = (screen_height // 4) - (juego_window_height // 4)
    juego_window.geometry(f"500x300+{x}+{y}")

    # Crear frames para la actividad
    instrucciones_frame = tk.Frame(juego_window)
    instrucciones_frame.pack(pady=10)

    palabras_frame = tk.Frame(juego_window)
    palabras_frame.pack(pady=10)

    resultado_frame = tk.Frame(juego_window)
    resultado_frame.pack(pady=10)

    # Instrucciones
    instrucciones_label = tk.Label(instrucciones_frame, text="Escribe las palabras en el orden correcto para formar una oración.")
    instrucciones_label.pack()

    resultado_label = tk.Label(resultado_frame, text="", wraplength=450)
    resultado_label.pack(pady=10)

    # Oraciones desordenadas
    oraciones = [
        ("perro", "El", "corre", "rápidamente"),
        ("niño", "El", "lee", "un libro"),
        ("El gato", "en", "duerme", "la silla"),
        ("comida", "Ella", "prepara", "deliciosa")
    ]

    respuestas = [
        "El perro corre rápidamente",
        "El niño lee un libro",
        "El gato duerme en la silla",
        "Ella prepara comida deliciosa"
    ]

    # Variable para la oración actual
    global indice_oracion
    indice_oracion = 0

    def mostrar_palabras(palabras):
        for widget in palabras_frame.winfo_children():
            widget.destroy()

        for palabra in palabras:
            tk.Label(palabras_frame, text=palabra, bg="lightgray", relief="raised", padx=10, pady=5).pack(side=tk.LEFT, padx=5)

    def verificar_orden():
        global indice_oracion
        entrada_usuario = entrada_entry.get().strip()
        orden_correcto = " ".join(palabra.cget("text") for palabra in palabras_frame.winfo_children())

        if entrada_usuario == respuestas[indice_oracion]:
            resultado_label.config(text="¡Correcto!", fg="green")
            entrada_entry.delete(0, tk.END)  # Limpiar entrada
            # Avanzar a la siguiente oración después de un pequeño retraso
            juego_window.after(1000, avanzar_a_siguiente_oracion)  # Esperar 1 segundo antes de avanzar
        else:
            resultado_label.config(text=f"Incorrecto. La respuesta correcta es: {respuestas[indice_oracion]}", fg="red")

    def avanzar_a_siguiente_oracion():
        global indice_oracion
        indice_oracion += 1
        if indice_oracion < len(oraciones):
            # Limpiar el mensaje de resultado antes de mostrar la siguiente oración
            resultado_label.config(text="")
            mostrar_palabras(oraciones[indice_oracion])
        else:
            resultado_label.config(text="¡Has completado todas las oraciones!", fg="black")
            check_button.pack_forget()  # Ocultar el botón al finalizar

    # Mostrar palabras de la primera oración
    mostrar_palabras(oraciones[indice_oracion])

    # Campo de entrada para escribir la oración
    entrada_frame = tk.Frame(juego_window)
    entrada_frame.pack(pady=10)
    entrada_entry = tk.Entry(entrada_frame, width=50)
    entrada_entry.pack()

    # Botón para verificar el orden
    check_button = tk.Button(juego_window, text="Verificar Orden", command=verificar_orden)
    check_button.pack(pady=10)