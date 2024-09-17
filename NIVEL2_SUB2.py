import tkinter as tk
from PIL import Image, ImageTk


# Lista de verbos y sus conjugaciones 
verbos = {
    "comer": {
        "presente": ["como", "comes", "come", "comemos", "coméis", "comen"],
        "pasado": ["comí", "comiste", "comió", "comimos", "comisteis", "comieron"],
        "futuro": ["comeré", "comerás", "comerá", "comeremos", "comeréis", "comerán"]
    },
    "vivir": {
        "presente": ["vivo", "vives", "vive", "vivimos", "vivís", "viven"],
        "pasado": ["viví", "viviste", "vivió", "vivimos", "vivisteis", "vivieron"],
        "futuro": ["viviré", "vivirás", "vivirá", "viviremos", "viviréis", "vivirán"]
    },
    "amar": {
        "presente": ["amo", "amas", "ama", "amamos", "amáis", "aman"],
        "pasado": ["amé", "amaste", "amó", "amamos", "amasteis", "amaron"],
        "futuro": ["amaré", "amarás", "amará", "amaremos", "amaréis", "amarán"]
    },
    
    "abrir": {
        "presente": ["abro", "abres", "abre", "abrimos", "abrís", "abren"],
        "pasado": ["abrí", "abriste", "abrió", "abrimos", "abristeis", "abrieron"],
        "futuro": ["abriré", "abrirás", "abrirá", "abriremos", "abriréis", "abrirán"]
    },
    "escribir": {
        "presente": ["escribo", "escribes", "escribe", "escribimos", "escribís", "escriben"],
        "pasado": ["escribí", "escribiste", "escribió", "escribimos", "escribisteis", "escribieron"],
        "futuro": ["escribiré", "escribirás", "escribirá", "escribiremos", "escribiréis", "escribirán"]
    },
    "caminar": {
        "presente": ["camino", "caminas", "camina", "caminamos", "camináis", "caminan"],
        "pasado": ["caminar", "caminaste", "caminó", "caminamos", "caminasteis", "caminaron"],
        "futuro": ["caminaré", "caminarás", "caminará", "caminaremos", "caminaréis", "caminarán"]
    },
    "correr": {
        "presente": ["corro", "corres", "corre", "corremos", "corréis", "corren"],
        "pasado": ["corrí", "corriste", "corrió", "corrimos", "corristeis", "corrieron"],
        "futuro": ["correré", "correrás", "correrá", "correremos", "correréis", "correrán"]
    },
    "subir": {
        "presente": ["subo", "subes", "sube", "subimos", "subís", "suben"],
        "pasado": ["subí", "subiste", "subió", "subimos", "subisteis", "subieron"],
        "futuro": ["subiré", "subirás", "subirá", "subiremos", "subiréis", "subirán"]
    }
}

oraciones = [
    {"texto": "La niña ___ una manzana. (comer)", "respuestas": ["come", "comió", "comerá"]},
    {"texto": "El perro ___ en el jardín. (vivir)", "respuestas": ["vive", "vivió", "vivirá"]},
    {"texto": "Juan ___ matemáticas. (estudiar)", "respuestas": ["estudia", "estudió", "estudiará"]},
    {"texto": "Los pájaros ___ en el cielo. (volar)", "respuestas": ["vuelan", "volaron", "volarán"]},
    {"texto": "María ___ en el coro. (cantar)", "respuestas": ["canta", "cantó", "cantará"]},
    {"texto": "Carlos ___ la ventana. (abrir)", "respuestas": ["abre", "abrió", "abrirá"]},
    {"texto": "Nosotros ___ una carta. (escribir)", "respuestas": ["escribimos", "escribimos", "escribiremos"]},
    {"texto": "Ella ___ por el parque. (caminar)", "respuestas": ["camina", "caminó", "caminará"]},
    {"texto": "Ellos ___ rápidamente. (correr)", "respuestas": ["corren", "corrieron", "correrán"]},
    {"texto": "Usted ___ la montaña. (subir)", "respuestas": ["sube", "subió", "subirá"]},
    {"texto": "Mi hermano ___ un libro. (leer)", "respuestas": ["lee", "leyó", "leerá"]},
    {"texto": "Mis amigos ___ a la fiesta. (ir)", "respuestas": ["van", "fueron", "irán"]},
    {"texto": "La profesora ___ la lección. (explicar)", "respuestas": ["explica", "explicó", "explicará"]},
    {"texto": "Nosotros ___ el coche. (manejar)", "respuestas": ["manejamos", "manejamos", "manejaremos"]},
    {"texto": "El chef ___ una receta. (preparar)", "respuestas": ["prepara", "preparó", "preparará"]}
]

# Lista de pronombres
pronombres = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos/ellas"]

def verificar_conjugacion(verbo, tiempo, respuestas_usuario):
    conjugaciones_correctas = verbos[verbo][tiempo]
    resultado = []
    for i in range(len(conjugaciones_correctas)):
        if i < len(respuestas_usuario) and respuestas_usuario[i].strip().lower() == conjugaciones_correctas[i]:
            resultado.append((conjugaciones_correctas[i], "green"))
        else:
            resultado.append((conjugaciones_correctas[i], "red"))
    return resultado

def verificar_oraciones(oracion, respuestas_usuario):
    resultados = []
    for i in range(len(oracion["respuestas"])):
        if i < len(respuestas_usuario) and respuestas_usuario[i].strip().lower() == oracion["respuestas"][i]:
            resultados.append((oracion["respuestas"][i], "green"))
        else:
            resultados.append((oracion["respuestas"][i], "red"))
    return resultados

def deshabilitar_entradas(entradas):
    for entrada in entradas:
        entrada.config(state="disabled")


def calcular_nivel(puntos, total):
    porcentaje = (puntos / total) * 100
    if porcentaje <= 20:
        nivel = "Mal nivel de aprendizaje"
    elif porcentaje <= 40:
        nivel = "Medio nivel de aprendizaje"
    elif porcentaje <= 60:
        nivel = "Buen nivel de aprendizaje"
    elif porcentaje <= 80:
        nivel = "Excelente nivel de aprendizaje"
    else:
        nivel = "Nivel de aprendizaje perfecto"
    return nivel, porcentaje

import random

def ventana_explicacion():
    def cerrar_ventana():
        ventana_explicacion.destroy()

    ventana_explicacion = tk.Toplevel(root)
    ventana_explicacion.title("Explicación de Conjugación de Verbos")
    ventana_explicacion.geometry("600x500")
    ventana_explicacion.resizable(True, True)
    
    # Calcular la posición central
    ventana_explicacion.update_idletasks()  # Asegurarse de que las dimensiones sean actualizadas
    ventana_subniveles_width = ventana_explicacion.winfo_width()
    ventana_subniveles_height = ventana_explicacion.winfo_height()
    screen_width = ventana_explicacion.winfo_screenwidth()
    screen_height = ventana_explicacion.winfo_screenheight()
    x = (screen_width // 2) - (ventana_subniveles_width // 2)
    y = (screen_height // 4) - (ventana_subniveles_height // 4)
    ventana_explicacion.geometry(f"600x500+{x}+{y}")

    contenedor = tk.Frame(ventana_explicacion)
    contenedor.pack(fill="both", expand=True)

    canvas = tk.Canvas(contenedor)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    frame_contenido = tk.Frame(canvas)
    frame_contenido.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=frame_contenido, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    def _on_mouse_wheel(event):
        canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

    canvas.bind("<MouseWheel>", _on_mouse_wheel)

    tk.Label(frame_contenido, text="Cómo Conjugar los Verbos", font=("Arial", 12, "bold")).pack(pady=10)

    # Explicación de cada tiempo verbal
    explicacion_presente = (
        '1. Verbo “Comer” en Presente:\n'
        '- Presente: Es como si estuvieras hablando de algo que está pasando ahora. Por ejemplo, si dices “Yo como pizza”, estás hablando de algo que haces en este momento.\n'
        '  - Yo como pizza.\n'
        '  - Tú comes pizza.\n'
        '  - Él/Ella come pizza.\n\n'
        '2. Verbo “Jugar” en Presente:\n'
        '- Presente: Hablas de algo que estás haciendo ahora. Por ejemplo, si dices “Yo juego fútbol”, estás hablando de algo que haces en este momento.\n'
        '  - Yo juego fútbol.\n'
        '  - Tú juegas fútbol.\n'
        '  - Él/Ella juega fútbol.'
    )

    explicacion_pasado = (
        '1. Verbo “Comer” en Pasado:\n'
        '- Pasado: Es como si estuvieras hablando de algo que ya ocurrió. Por ejemplo, si dices “Yo comí pizza”, estás hablando de algo que hiciste en el pasado.\n'
        '  - Yo comí pizza.\n'
        '  - Tú comiste pizza.\n'
        '  - Él/Ella comió pizza.\n\n'
        '2. Verbo “Jugar” en Pasado:\n'
        '- Pasado: Hablas de algo que ya hiciste. Por ejemplo, si dices “Yo jugué fútbol”, estás hablando de algo que hiciste antes.\n'
        '  - Yo jugué fútbol.\n'
        '  - Tú jugaste fútbol.\n'
        '  - Él/Ella jugó fútbol.'
    )

    explicacion_futuro = (
        '1. Verbo “Comer” en Futuro:\n'
        '- Futuro: Es como si estuvieras hablando de algo que pasará en el futuro. Por ejemplo, si dices “Yo comeré pizza”, estás hablando de algo que harás más adelante.\n'
        '  - Yo comeré pizza.\n'
        '  - Tú comerás pizza.\n'
        '  - Él/Ella comerá pizza.\n\n'
        '2. Verbo “Jugar” en Futuro:\n'
        '- Futuro: Hablas de algo que harás más adelante. Por ejemplo, si dices “Yo jugaré fútbol”, estás hablando de algo que harás en el futuro.\n'
        '  - Yo jugaré fútbol.\n'
        '  - Tú jugarás fútbol.\n'
        '  - Él/Ella jugará fútbol.'
    )

    tk.Label(frame_contenido, text="Presente", font=("Arial", 11, "bold")).pack(pady=(10, 5))
    tk.Label(frame_contenido, text=explicacion_presente, wraplength=580, justify="left", font=("Arial", 11)).pack(pady=5, padx=10)

    tk.Label(frame_contenido, text="Pasado", font=("Arial", 11, "bold")).pack(pady=(10, 5))
    tk.Label(frame_contenido, text=explicacion_pasado, wraplength=580, justify="left", font=("Arial", 11)).pack(pady=5, padx=10)

    tk.Label(frame_contenido, text="Futuro", font=("Arial", 11, "bold")).pack(pady=(10, 5))
    tk.Label(frame_contenido, text=explicacion_futuro, wraplength=580, justify="left", font=("Arial", 11)).pack(pady=5, padx=10)

    tk.Button(frame_contenido, text="Cerrar", command=cerrar_ventana).pack(pady=10)


ventana_conjugacion_abierta = False
ventana_oraciones_abierta = False

def ventana_conjugacion():
    global ventana_conjugacion_abierta
    if ventana_conjugacion_abierta:
        return
    ventana_conjugacion_abierta = True

    def cerrar_ventana():
        global ventana_conjugacion_abierta
        ventana_conjugacion_abierta = False
        ventana.destroy()

    ventana = tk.Toplevel(root)
    ventana.title("Conjugación de Verbos")
    ventana.geometry("600x550")
    ventana.resizable(True, True)
    
        # Calcular la posición central
    ventana.update_idletasks()  # Asegurarse de que las dimensiones sean actualizadas
    ventana_width = ventana.winfo_width()
    ventana_height = ventana.winfo_height()
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    x = (screen_width // 2) - (ventana_width // 2)
    y = (screen_height // 4) - (ventana_height // 4)
    ventana.geometry(f"600x550+{x}+{y}")
    

    ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)
    
    contenedor = tk.Frame(ventana)
    contenedor.pack(fill="both", expand=True)

    canvas = tk.Canvas(contenedor)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    frame_contenido = tk.Frame(canvas)
    frame_contenido.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=frame_contenido, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    def _on_mouse_wheel(event):
        canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

    canvas.bind("<MouseWheel>", _on_mouse_wheel)

    verbos_usados = set()

    def cargar_verbos_aleatorios():
        disponibles = list(set(verbos.keys()) - verbos_usados)
        if not disponibles:
            disponibles = list(verbos.keys())
            verbos_usados.clear()
        seleccionados = random.sample(disponibles, k=min(3, len(disponibles)))
        verbos_usados.update(seleccionados)
        return seleccionados

    resultado_mostrado_label = tk.Label(ventana)
    resultado_mostrado_label.pack(pady=10)

    boton_mostrar_resultado = tk.Button(ventana, text="Mostrar Resultado")
    boton_reintentar = tk.Button(ventana, text="Reintentar")

    def mostrar_verbos(verbos_seleccionados):
        for widget in frame_contenido.winfo_children():
            widget.destroy()

        tk.Label(frame_contenido, text="Conjuga los verbos en presente, pasado y futuro", font=("Times", 12, "bold"), bg="salmon").pack()
        tk.Label(frame_contenido, text="Ten en cuenta signos de puntuacion para que tu acierto sea correcto.", font=("Times", 12, "bold"), bg="salmon").pack()

        puntos = 0
        total = 54

        for verbo in verbos_seleccionados:
            frame_verbo = tk.Frame(frame_contenido)
            frame_verbo.pack(pady=5, fill="x")

            tk.Label(frame_verbo, text=f"Verbo: {verbo}").grid(row=0, column=0, padx=10, pady=5)

            for tiempo in ["presente", "pasado", "futuro"]:
                frame_tiempo = tk.Frame(frame_verbo)
                frame_tiempo.grid(row=1, column=["presente", "pasado", "futuro"].index(tiempo), padx=10, pady=5)

                tk.Label(frame_tiempo, text=f"{tiempo.capitalize()}: ").grid(row=0, column=0)

                entradas = []
                respuestas_correctas_labels = []

                for i, pronombre in enumerate(pronombres):
                    tk.Label(frame_tiempo, text=pronombre).grid(row=i+1, column=0, padx=5)
                    entrada = tk.Entry(frame_tiempo, width=10)
                    entrada.grid(row=i+1, column=1, padx=5)
                    entradas.append(entrada)

                    respuesta_correcta = tk.Label(frame_tiempo, text="", font=("Arial", 10), bg="white")
                    respuesta_correcta.grid(row=i+1, column=2, padx=5)
                    respuestas_correctas_labels.append(respuesta_correcta)

                def verificar_respuesta(verbo=verbo, tiempo=tiempo, entradas=entradas, respuestas_correctas_labels=respuestas_correctas_labels):
                    nonlocal puntos
                    respuestas_usuario = [entrada.get() for entrada in entradas]
                    resultado = verificar_conjugacion(verbo, tiempo, respuestas_usuario)
                    for i, (respuesta, color) in enumerate(resultado):
                        if i < len(respuestas_correctas_labels):
                            respuestas_correctas_labels[i].config(text=respuesta, fg=color)
                        if color == "green":
                            puntos += 1
                    deshabilitar_entradas(entradas)

                tk.Button(frame_tiempo, text="Verificar", command=verificar_respuesta).grid(row=len(pronombres)+1, column=1, pady=5)

        def mostrar_resultado():
            nivel, porcentaje = calcular_nivel(puntos, total)
            resultado_mostrado_label.config(text=f"Puntuación: {puntos}/{total} puntos\nPorcentaje: {porcentaje:.2f}%\nNivel de aprendizaje: {nivel}")

        def reiniciar_ventana():
            for widget in frame_contenido.winfo_children():
                widget.destroy()
            verbos_seleccionados = cargar_verbos_aleatorios()
            mostrar_verbos(verbos_seleccionados)

        boton_mostrar_resultado.config(command=mostrar_resultado)
        boton_reintentar.config(command=reiniciar_ventana)

        if not resultado_mostrado_label.winfo_ismapped():
            resultado_mostrado_label.pack(pady=10)

        if not boton_mostrar_resultado.winfo_ismapped():
            boton_mostrar_resultado.pack(pady=10)
        if not boton_reintentar.winfo_ismapped():
            boton_reintentar.pack(pady=5)

    verbos_seleccionados = cargar_verbos_aleatorios()
    mostrar_verbos(verbos_seleccionados)



def ventana_oraciones():
    global ventana_oraciones_abierta
    if ventana_oraciones_abierta:
        return
    ventana_oraciones_abierta = True

    def cerrar_ventana():
        global ventana_oraciones_abierta
        ventana_oraciones_abierta = False
        ventana.destroy()

    ventana = tk.Toplevel(root)
    ventana.title("Completar Oraciones")
    ventana.geometry("500x600")
    ventana.resizable(True, True)
    
    # Calcular la posición central
    ventana.update_idletasks()  # Asegurarse de que las dimensiones sean actualizadas
    ventana_width = ventana.winfo_width()
    ventana_height = ventana.winfo_height()
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    x = (screen_width // 2) - (ventana_width // 2)
    y = (screen_height // 4) - (ventana_height // 4)
    ventana.geometry(f"500x600+{x}+{y}")

    ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

    oraciones_usadas = set()

    def cargar_oraciones_aleatorias():
        disponibles = list(set(o["texto"] for o in oraciones) - oraciones_usadas)
        if not disponibles:
            disponibles = list(o["texto"] for o in oraciones)
            oraciones_usadas.clear()
        seleccionadas = random.sample(disponibles, k=min(4, len(disponibles)))
        oraciones_usadas.update(o["texto"] for o in oraciones if o["texto"] in seleccionadas)
        return [o for o in oraciones if o["texto"] in seleccionadas]

    frame_contenido = tk.Frame(ventana)
    frame_contenido.pack(fill="both", expand=True)

    frame_resultado = tk.Frame(ventana)
    frame_resultado.pack(side="bottom", fill="x", pady=5)

    resultado_mostrado_label = tk.Label(frame_resultado, text="", anchor="w")
    resultado_mostrado_label.pack()

    boton_mostrar_resultado = tk.Button(frame_resultado, text="Mostrar Resultado")
    boton_reintentar = tk.Button(frame_resultado, text="Reintentar")

    def mostrar_oraciones(oraciones_seleccionadas):
        for widget in frame_contenido.winfo_children():
            widget.destroy()

        tk.Label(frame_contenido, text="Completa las oraciones con sus verbos en presente, pasado y futuro", font=("Times", 12, "bold"), bg="salmon").pack()
        tk.Label(frame_contenido, text="Ten en cuenta signos de puntuacion para que tu acierto sea correcto.", font=("Times", 12, "bold"), bg="salmon").pack()

        puntos = 0
        total = 15

        for oracion in oraciones_seleccionadas:
            frame_oracion = tk.Frame(frame_contenido)
            frame_oracion.pack(pady=5, fill="x")

            tk.Label(frame_oracion, text=oracion["texto"]).grid(row=0, column=0, padx=10, pady=5)

            entradas = []
            respuestas_correctas_labels = []
            for tiempo in ["Presente", "Pasado", "Futuro"]:
                entrada = tk.Entry(frame_oracion, width=10)
                entrada.grid(row=0, column=["Presente", "Pasado", "Futuro"].index(tiempo) + 1)
                entradas.append(entrada)

                respuesta_correcta = tk.Label(frame_oracion, text="", font=("Arial", 10), bg="white")
                respuesta_correcta.grid(row=1, column=["Presente", "Pasado", "Futuro"].index(tiempo) + 1)
                respuestas_correctas_labels.append(respuesta_correcta)

            def verificar_respuesta(oracion=oracion, entradas=entradas, respuestas_correctas_labels=respuestas_correctas_labels):
                nonlocal puntos
                respuestas_usuario = [entrada.get() for entrada in entradas]
                resultados = verificar_oraciones(oracion, respuestas_usuario)
                for i, (respuesta, color) in enumerate(resultados):
                    if i < len(respuestas_correctas_labels):
                        respuestas_correctas_labels[i].config(text=respuesta, fg=color)
                    if color == "green":
                        puntos += 1
                deshabilitar_entradas(entradas)

            tk.Button(frame_oracion, text="Verificar", command=verificar_respuesta).grid(row=2, column=0, columnspan=3, pady=5)

        def mostrar_resultado():
            nivel, porcentaje = calcular_nivel(puntos, total)
            resultado_mostrado_label.config(text=f"Puntuación: {puntos}/{total} puntos\nPorcentaje: {porcentaje:.2f}%\nNivel de aprendizaje: {nivel}")

        def reiniciar_ventana():
            for widget in frame_contenido.winfo_children():
                widget.destroy()
            oraciones_seleccionadas = cargar_oraciones_aleatorias()
            mostrar_oraciones(oraciones_seleccionadas)

        boton_mostrar_resultado.config(command=mostrar_resultado)
        boton_reintentar.config(command=reiniciar_ventana)

        if not resultado_mostrado_label.winfo_ismapped():
            resultado_mostrado_label.pack(pady=10)

        if not boton_mostrar_resultado.winfo_ismapped():
            boton_mostrar_resultado.pack(pady=10)
        if not boton_reintentar.winfo_ismapped():
            boton_reintentar.pack(pady=5)

    oraciones_seleccionadas = cargar_oraciones_aleatorias()
    mostrar_oraciones(oraciones_seleccionadas)


def ventana_principal():
    global root
    root = tk.Toplevel()
    root.title("Juego de Conjugación de Verbos en Español")
    root.geometry("501x300")  
    root.resizable(False, False)  
    
    # Cargar imagen
    img = Image.open("IMG/IMG04.jpeg")  # Reemplaza con la ruta a tu imagen
    img = img.resize((501, 300), Image.Resampling.LANCZOS)  # Ajusta el tamaño si es necesario
    img_tk = ImageTk.PhotoImage(img)
    
    # Calcular la posición central
    root.update_idletasks()  # Asegurarse de que las dimensiones sean actualizadas
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (root_width // 2)
    y = (screen_height // 4) - (root_height // 4)
    root.geometry(f"501x300+{x}+{y}")

    img_label = tk.Label(root, image=img_tk)
    img_label.image = img_tk  
    img_label.place(relwidth=1, relheight=1)  

    # Agregar el texto sobre la imagen
    tk.Label(root, text="¡Bienvenido al juego de conjugación de verbos en español!", font=("Times", 14, "bold"), bg="steel blue").pack(pady=10)
    tk.Label(root, text="\nSelecciona una opción para comenzar:\n", font=("arial", 10, "bold"), bg=root.cget("bg")).pack()

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="¿Cómo conjugar los verbos?", command=ventana_explicacion, bg="lightgreen").pack(pady=(5, 10))
    tk.Button(button_frame, text="Actividad Conjugación de Verbos", command=ventana_conjugacion, bg="lightgreen").pack(pady=5)
    tk.Button(button_frame, text="Actividad Completar Oraciones", command=ventana_oraciones, bg="lightgreen").pack(pady=5)