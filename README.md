# Proyecto_Datos2_RutaMasSatisfactoria

Este proyecto es un recomendador de lugares basado en características como temperatura y altura. Utiliza la biblioteca NetworkX para construir un grafo que representa las conexiones entre diferentes lugares y sus atributos.

El objetivo principal de este programa es permitir a los usuarios seleccionar un lugar que les guste y una característica específica que les interese, como la temperatura o la altura. Luego, el programa encuentra el camino más corto desde el lugar seleccionado hasta el lugar más cercano con una característica similar, proporcionando así una ruta eficiente para llegar allí, junto con una recomendación detallada del lugar.

Esta funcionalidad permite a los usuarios descubrir nuevos destinos que se ajusten a sus preferencias, considerando tanto la característica deseada como la proximidad geográfica.

## Bibliotecas requeridas

Para ejecutar este programa, asegúrate de tener instaladas las siguientes bibliotecas de Python:

- `csv`: para leer los datos del archivo CSV.
- `networkx`: para construir y analizar el grafo.
- `tkinter`: para crear la interfaz gráfica.
- `tkinter.ttk`: para estilizar algunos elementos de la interfaz.
- `tkinter.font`: para cambiar el estilo de fuente de las etiquetas.

Puedes instalar las bibliotecas necesarias mediante el administrador de paquetes `pip`. Ejecuta el siguiente comando:

    ```bash
    pip install networkx
    pip install tkinter  
    ```

## Uso

1. Clona este repositorio en tu máquina local o descarga los archivos.

2. Asegúrate de tener el archivo CSV con los datos de los municipios y actualiza la ruta en el código según tu ubicación:

    ```python
    with open(r'Tu/Ruta/Al/Archivo/DatosMunicipios.csv', 'r', encoding='UTF-8') as file:  
    ```  
3. Ejecuta el programa utilizando Python.

4. Se abrirá una ventana con una interfaz gráfica donde podrás seleccionar el lugar y la característica que te gustaron.

5. Haz clic en el botón "Recomendar" y se mostrará una recomendación junto con el camino más corto para llegar al lugar recomendado.  

¡Disfruta explorando nuevos lugares con este recomendador!

## Equipo Abyss Watchers  

- NICOLAS MORENO LÓPEZ
- JOSÉ MIGUEL MUÑOZ RÍOS
- JULIO CÉSAR POSADA TORRES

#### Versiones 

Python 3.11.3  
Networkx 3.1  
Tkinter 8.6  

Recuerda reemplazar `"Tu/Ruta/Al/Archivo/DatosMunicipios.csv"` con la ruta adecuada donde instales tu archivo CSV el cual descargaras desde:  
Enlace al archivo: [DatosMunicipios.csv](/Archivos/DatosMunicipios.csv)



