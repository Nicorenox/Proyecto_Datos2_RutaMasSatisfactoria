import csv
import networkx as nx
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

# Crear el gráfico
G = nx.Graph()

# Leer el archivo CSV y agregar nodos y aristas al gráfico
with open(r'C:\Users\123\Downloads\DatosMunicipios.csv', 'r', encoding='UTF-8') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)  # Omitir la primera fila si contiene encabezados

    for row in reader:
        municipio = row[0]
        temp = int(row[1])
        alt = int(row[2])
        act = row[3]

        G.add_node(municipio, temp=temp, alt=alt, act=act)

        G.add_edge('Medellín', municipio, weight=1)  # Usar un peso de 1 para todas las aristas

def recomendar():
    lugargustado = combo_lugar.get()
    caractgustada = combo_caracteristica.get()

    # Encontrar el valor de la característica del lugar que le gustó
    valor_caracteristica_gustada = None
    for node, data in G.nodes(data=True):
        if node == lugargustado:
            if caractgustada == 'Temperatura':
                valor_caracteristica_gustada = data['temp']
            elif caractgustada == 'Altura':
                valor_caracteristica_gustada = data['alt']
            break

    # Encontrar el lugar más cercano al lugar que le ha gustado con una característica similar
    lugar_recomendado = None
    min_diferencia = float('inf')  # Valor inicial alto para la diferencia

    for node, data in G.nodes(data=True):
        if node != lugargustado:
            caracteristica_actual = data['temp' if caractgustada == 'Temperatura' else 'alt']
            diferencia = abs(caracteristica_actual - valor_caracteristica_gustada)
            if diferencia < min_diferencia:
                min_diferencia = diferencia
                lugar_recomendado = node

    if lugar_recomendado:
        # Encontrar el camino más corto hacia la recomendación utilizando el algoritmo de Dijkstra
        ruta_mas_corta = nx.dijkstra_path(G, lugargustado, lugar_recomendado)

        # Obtener datos del lugar recomendado
        actividades_recomendadas = G.nodes[lugar_recomendado]['act']
        temperatura_recomendada = G.nodes[lugar_recomendado]['temp']
        altura_recomendada = G.nodes[lugar_recomendado]['alt']

        # Actualizar etiquetas con la recomendación y el camino más corto
        label_recomendacion.configure(text="Te recomendamos visitar: " + lugar_recomendado, font=font_style)
        label_actividades.configure(text="Actividades: " + actividades_recomendadas, font=font_style)
        label_temperatura.configure(text="Temperatura: " + str(temperatura_recomendada) + " grados", font=font_style)
        label_altura.configure(text="Altura: " + str(altura_recomendada) + " metros sobre el nivel del mar", font=font_style)
        label_ruta.configure(text="Camino más corto: " + " -> ".join(ruta_mas_corta), font=font_style)

    else:
        # No se encontró un lugar recomendado
        label_recomendacion.configure(text="No se encontró un lugar recomendado con la característica seleccionada.", font=font_style)
        label_actividades.configure(text="", font=font_style)
        label_temperatura.configure(text="", font=font_style)
        label_altura.configure(text="", font=font_style)
        label_ruta.configure(text="", font=font_style)


# Crear ventana principal
window = tk.Tk()
window.title("Recomendador de Lugares")

# Obtener dimensiones de la pantalla
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calcular posición para centrar la ventana
window_width = 800
window_height = 600
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Establecer posición y tamaño de la ventana
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Cambiar el estilo de fuente
font_style = Font(family="Arial", size=14)

# Establecer un color de fondo
window.configure(bg="#E6E6FA")

# Etiqueta y menú desplegable para seleccionar el lugar
label_lugar = tk.Label(window, text="Seleccione el lugar que le ha gustado:", font=font_style, bg="#E6E6FA")
label_lugar.pack()

lugares = list(G.nodes())
combo_lugar = ttk.Combobox(window, values=lugares, font=font_style)
combo_lugar.pack()

# Etiqueta y menú desplegable para seleccionar la característica
label_caracteristica = tk.Label(window, text="Seleccione la característica que le gustó:", font=font_style, bg="#E6E6FA")
label_caracteristica.pack()

caracteristicas = ['Temperatura', 'Altura']
combo_caracteristica = ttk.Combobox(window, values=caracteristicas, font=font_style)
combo_caracteristica.pack()

# Botón de recomendar
button_recomendar = tk.Button(window, text="Recomendar", command=recomendar, font=font_style)
button_recomendar.pack()

# Etiquetas para mostrar la recomendación y el camino más corto
label_recomendacion = tk.Label(window, text="", font=font_style, bg="#E6E6FA")
label_recomendacion.pack()
label_actividades = tk.Label(window, text="", font=font_style, bg="#E6E6FA")
label_actividades.pack()
label_temperatura = tk.Label(window, text="", font=font_style, bg="#E6E6FA")
label_temperatura.pack()
label_altura = tk.Label(window, text="", font=font_style, bg="#E6E6FA")
label_altura.pack()
label_ruta = tk.Label(window, text="", font=font_style, bg="#E6E6FA")
label_ruta.pack()

window.mainloop()
