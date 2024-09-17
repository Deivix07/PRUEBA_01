import random
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

def ventana_oraciones():
    global oraciones
    oraciones = tk.Toplevel()
    oraciones.title("Estructura de oraciones")
    oraciones.geometry("501x300")  
    oraciones.resizable(False, False)  

    # Cargar imagen
    img = Image.open("IMG/IMG03.jpg")
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
    tk.Label(oraciones, text="Aprende a estructurar oraciones", font=("Times", 14, "bold"), bg="steel blue").pack(pady=10)
    tk.Label(oraciones, text="\nSelecciona una opción para comenzar:\n", font=("arial", 10, "bold"), bg=oraciones.cget("bg")).pack()

    button_frame = tk.Frame(oraciones)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Oraciones Simples", command=mostrar_concepto, bg="lightgreen").pack(pady=5)
    tk.Button(button_frame, text="Actividad Identificar", command=iniciar_juego, bg="lightgreen").pack(pady=5)
    tk.Button(button_frame, text="Actividad Crucigrama", bg="lightgreen").pack(pady=5)

def mostrar_concepto():
    concepto_window = tk.Toplevel()
    concepto_window.title("Concepto de Oraciones Simples")
    concepto_window.geometry("500x400")

    instrucciones_texto = """¡Ahora estudiaremos las oraciones simples!
    
    Una oración simple es como una pequeña idea que tiene todo lo que necesita para que quien la escuche la entienda, por ejemplo:
    
    "Mamá quiero pollo frito."
    
    Aunque mamá te va a decir que no porque en la casa hay sopa, usaste una oración simple y ella te entendió.
    
    Una oración simple tiene tres partes: UN SUJETO, que es de quien se habla, UN VERBO, que es la acción que está realizando y UN COMPLEMENTO, que como su nombre lo dice, nos ayuda a darle más sentido a nuestra oración.
    Por ejemplo cuando tu dices 'Mi gato come atún', el sujeto es tu GATO, el verbo es COME, y el complemento es el ATUN.
    Otra oración simple podría ser:
    'La niña canta en inglés.'
    Aquí LA NIÑA es el sujeto, CANTA es lo que hace y EN INGLES, el complemento, que como ves no es indispensable pero sí nos aporta en la oración."""

    instrucciones_label = tk.Label(concepto_window, text=instrucciones_texto, wraplength=450)
    instrucciones_label.pack(pady=10)

    jugar_button = tk.Button(concepto_window, text="Comenzar Juego", command=iniciar_juego)
    jugar_button.pack(pady=10)

def iniciar_juego():
    juego_window = tk.Toplevel()
    juego_window.title("Juego de Oraciones Simples")
    juego_window.geometry("500x400")

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

    # Variables del juego
    contador_preguntas = 0
    max_preguntas = 4

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

    def mostrar_pregunta():
        nonlocal contador_preguntas

        if contador_preguntas >= max_preguntas:
            messagebox.showinfo("Fin del Juego", "¡Has completado todas las preguntas!")
            juego_window.destroy()
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
            sujeto = sujeto_entry.get()
            verbo = verbo_entry.get()
            complemento = complemento_entry.get()

            correcta = True
            if sujeto != oracion_actual["sujeto"]:
                correcta = False
                messagebox.showerror("Respuesta Incorrecta", f"El sujeto correcto es: {oracion_actual['sujeto']}")

            if verbo != oracion_actual["verbo"]:
                correcta = False
                messagebox.showerror("Respuesta Incorrecta", f"El verbo correcto es: {oracion_actual['verbo']}")

            if complemento != oracion_actual["complemento"]:
                correcta = False
                messagebox.showerror("Respuesta Incorrecta", f"El complemento correcto es: {oracion_actual['complemento']}")

            if correcta:
                messagebox.showinfo("Resultado", "¡Respuesta correcta!")

            contador_preguntas += 1
            mostrar_pregunta()

        check_button = tk.Button(preguntas_frame, text="Verificar Respuestas", command=verificar_respuestas)
        check_button.pack(pady=10)

    mostrar_pregunta()