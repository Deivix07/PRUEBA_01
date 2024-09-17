import tkinter as tk
from PIL import Image, ImageTk

def ventana_voz():
    global oraciones
    oraciones = tk.Toplevel()
    oraciones.title("Estructura de oraciones")
    oraciones.geometry("501x300")  
    oraciones.resizable(False, False)  

    # Cargar imagen
    img = Image.open("IMG/IMG07.jpg")
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
    tk.Label(oraciones, text="Entendiendo la Voz Pasiva: Transformando Oraciones", font=("Times", 14, "bold"), bg="light blue").pack(pady=10)
    tk.Label(oraciones, text="\nSelecciona una opción para comenzar:\n", font=("arial", 10, "bold"), bg="orange").pack()

    button_frame = tk.Frame(oraciones, bg="papaya whip")
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Voz Pasiva", command=mostrar_concepto, bg="lightgreen").pack(pady=5)
    tk.Button(button_frame, text="Actividad Transformar", command=iniciar_juego_voz_pasiva, bg="lightgreen").pack(pady=5)
    tk.Button(button_frame, text="Actividad Crucigrama", command=identificar_voz, bg="lightgreen").pack(pady=5)

def mostrar_concepto():
    concepto_window = tk.Toplevel()
    concepto_window.title("Concepto de Oraciones Simples")
    concepto_window.geometry("500x450")
    
    concepto_window.update_idletasks()
    concepto_window_width = concepto_window.winfo_width()
    concepto_window_height = concepto_window.winfo_height()
    screen_width = concepto_window.winfo_screenwidth()
    screen_height = concepto_window.winfo_screenheight()
    x = (screen_width // 2) - (concepto_window_width // 2)
    y = (screen_height // 4) - (concepto_window_height // 4)
    concepto_window.geometry(f"500x450+{x}+{y}")

    tk.Label(concepto_window,text="Voz Pasiva", font=("Arial", 12, "bold")).pack(pady=10)

    instrucciones_texto = (
        "La voz pasiva es una forma gramatical que se utiliza para enfatizar la acción o el resultado de la acción "
        "más que al sujeto que realiza la acción. En una oración en voz pasiva, el objeto directo de la oración activa "
        "se convierte en el sujeto de la oración pasiva. Por ejemplo:\n\n"
        
        "Oración Activa: 'El chef prepara la cena.'\n"
        "Oración Pasiva: 'La cena es preparada por el chef.'\n\n"
        
        "En la voz pasiva, la estructura de la oración cambia de la siguiente manera:\n"
        "- Se usa el verbo 'ser' en el tiempo correspondiente.\n"
        "- Se agrega el participio pasado del verbo principal.\n"
        "- Se usa el complemento agente (quien realiza la acción) al final, introducido por la preposición 'por'.\n\n"
        
        "Sujeto + verbo ser + participio pasado + complemento agente)\n\n"
        
        "Más ejemplos:\n\n"
        "1.  Activa: 'El equipo completó el proyecto.'\n"
        "    Pasiva: 'El proyecto fue completado por el equipo.'\n\n"
        "2.  Activa: 'El artista pintó el mural.'\n"
        "    Pasiva: 'El mural fue pintado por el artista.'\n\n"
    )
    
    instrucciones_label = tk.Label(concepto_window, text=instrucciones_texto, wraplength=450)
    instrucciones_label.pack(pady=10)

def iniciar_juego_voz_pasiva():
    juego_window = tk.Toplevel()
    juego_window.title("Transformar a Voz Pasiva")
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

    oraciones_frame = tk.Frame(juego_window)
    oraciones_frame.pack(pady=10)

    resultado_frame = tk.Frame(juego_window)
    resultado_frame.pack(pady=10)

    # Instrucciones
    instrucciones_label = tk.Label(instrucciones_frame, text="Convierte la oración de voz activa a pasiva.")
    instrucciones_label.pack()

    resultado_label = tk.Label(resultado_frame, text="", wraplength=450)
    resultado_label.pack(pady=10)

    # Oraciones activas y sus transformaciones pasivas
    oraciones_activas = [
        "El chef prepara la cena",
        "El niño rompe el juguete",
        "La profesora enseña la lección",
        "El perro persigue al gato",
        "La secretaria organiza los archivos"
    ]

    oraciones_pasivas = [
        "La cena es preparada por el chef",
        "El juguete es roto por el niño",
        "La lección es enseñada por la profesora",
        "El gato es perseguido por el perro",
        "Los archivos son organizados por la secretaria"
    ]

    # Variable para la oración actual
    global indice_oracion
    indice_oracion = 0

    def mostrar_oracion(activa):
        for widget in oraciones_frame.winfo_children():
            widget.destroy()

        tk.Label(oraciones_frame, text=activa, bg="lightgray", padx=10, pady=5).pack(pady=5)

    def verificar_transformacion():
        global indice_oracion
        entrada_usuario = entrada_entry.get().strip()

        if entrada_usuario == oraciones_pasivas[indice_oracion]:
            resultado_label.config(text="¡Correcto!", fg="green")
            entrada_entry.delete(0, tk.END)  # Limpiar entrada
            # Avanzar a la siguiente oración después de un pequeño retraso
            juego_window.after(1000, avanzar_a_siguiente_oracion)  # Esperar 1 segundo antes de avanzar
        else:
            resultado_label.config(text=f"Incorrecto. La respuesta correcta es: {oraciones_pasivas[indice_oracion]}", fg="red")

    def avanzar_a_siguiente_oracion():
        global indice_oracion
        indice_oracion += 1
        if indice_oracion < len(oraciones_activas):
            # Limpiar el mensaje de resultado antes de mostrar la siguiente oración
            resultado_label.config(text="")
            mostrar_oracion(oraciones_activas[indice_oracion])
        else:
            resultado_label.config(text="¡Has completado todas las oraciones!", fg="black")
            check_button.pack_forget()  # Ocultar el botón al finalizar

    # Mostrar oración activa de la primera oración
    mostrar_oracion(oraciones_activas[indice_oracion])

    # Campo de entrada para escribir la oración transformada
    entrada_frame = tk.Frame(juego_window)
    entrada_frame.pack(pady=10)
    entrada_entry = tk.Entry(entrada_frame, width=50)
    entrada_entry.pack()

    # Botón para verificar la transformación
    check_button = tk.Button(juego_window, text="Verificar Transformación", command=verificar_transformacion)
    check_button.pack(pady=10)
    
def identificar_voz():
    # Lista de oraciones con su tipo (Activa o Pasiva)
    oraciones = [
        {"texto": "El chef prepara una cena deliciosa.", "tipo": "Activa"},
        {"texto": "La carta fue escrita por María.", "tipo": "Pasiva"},
        {"texto": "El estudiante completó el examen.", "tipo": "Activa"},
        {"texto": "La pizza fue entregada por el repartidor.", "tipo": "Pasiva"},
        {"texto": "Los niños jugaron en el parque.", "tipo": "Activa"},
        {"texto": "El libro fue leído por Juan.", "tipo": "Pasiva"},
        {"texto": "La película fue dirigida por el famoso director.", "tipo": "Pasiva"},
        {"texto": "El ingeniero construyó un puente.", "tipo": "Activa"}
    ]

    # Variables globales
    current_index = 0
    errores = 0

    # Función para verificar la respuesta y avanzar a la siguiente oración
    def verificar_respuesta(index, seleccion):
        nonlocal errores
        if oraciones[index]["tipo"] == seleccion:
            resultado_label.config(text="¡Respuesta correcta!", fg="green")
            ventana.after(1000, siguiente_oracion)  # Avanzar después de 1 segundo
        else:
            errores += 1
            resultado_label.config(text="Respuesta incorrecta. Intenta nuevamente.", fg="red")

    def siguiente_oracion():
        nonlocal current_index
        current_index += 1
        if current_index < len(oraciones):
            oracion_label.config(text=oraciones[current_index]["texto"])
            resultado_label.config(text="")
        else:
            mostrar_resultado_final()

    def mostrar_resultado_final():
        oracion_label.config(text=f"¡Has terminado todas las oraciones! Fallos: {errores}")
        activa_button.pack_forget()
        pasiva_button.pack_forget()

    # Crear ventana Toplevel
    ventana = tk.Toplevel()
    ventana.title("Identifica la Voz: Activa o Pasiva")
    ventana.geometry("400x200")
    
    ventana.update_idletasks()
    ventana_width = ventana.winfo_width()
    ventana_height = ventana.winfo_height()
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    x = (screen_width // 2) - (ventana_width // 2)
    y = (screen_height // 4) - (ventana_height // 4)
    ventana.geometry(f"400x200+{x}+{y}")

    # Mostrar la primera oración
    oracion_label = tk.Label(ventana, text=oraciones[current_index]["texto"], wraplength=400)
    oracion_label.pack(pady=20)

    # Frame para botones
    button_frame = tk.Frame(ventana)
    button_frame.pack(pady=20)

    # Botones para seleccionar si la oración es Activa o Pasiva
    activa_button = tk.Button(button_frame, text="Voz Activa", command=lambda: verificar_respuesta(current_index, "Activa"))
    activa_button.pack(side=tk.LEFT, padx=20)

    pasiva_button = tk.Button(button_frame, text="Voz Pasiva", command=lambda: verificar_respuesta(current_index, "Pasiva"))
    pasiva_button.pack(side=tk.RIGHT, padx=20)

    # Label para mostrar el resultado de la respuesta
    resultado_label = tk.Label(ventana, text="", font=("Arial", 12))
    resultado_label.pack(pady=20)