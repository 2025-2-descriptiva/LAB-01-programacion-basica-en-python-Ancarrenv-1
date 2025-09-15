"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    conteo = {}  # Dictionary to hold key

    with open('C:/Repositorios/LAB-01-programacion-basica-en-python-Ancarrenv-1/files/input/data.csv') as file:
        for linea in file:
            linea = linea.strip()
            columnas = linea.split('\t')

            bd = columnas[4].split(',')

            for n in bd:
                clave, valor = n.split(':')
                valor = int(valor)

                if clave not in conteo:
                    conteo[clave] = []  # Initialize list for this key
                conteo[clave].append(valor)  # Append value to the key's list

    resultado = []
    for clave in sorted(conteo.keys()):
        valores = conteo[clave]
    resultado.append((clave, min(valores), max(valores)))

    return resultado


print(pregunta_06())
