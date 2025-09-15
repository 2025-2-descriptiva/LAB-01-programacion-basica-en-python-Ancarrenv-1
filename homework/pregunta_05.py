"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor máximo y mínimo de la columna 2
    por cada letra de la columna 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    """
    conteo = {}
    
    with open('C:/Repositorios/LAB-01-programacion-basica-en-python-Ancarrenv-1/files/input/data.csv') as file:
        for linea in file:
            linea = linea.strip()
            columnas = linea.split('\t')
            
            letra = columnas[0]
            valor = int(columnas[1])
            
            if letra not in conteo:
                conteo[letra] = []
                conteo[letra].append(valor)

    resultado = []
    for letra in sorted(conteo.keys()):
        valores = conteo[letra]
        resultado.append((letra, max(valores), min(valores)))
    
    return resultado

# Ejecutar y mostrar resultado
resultado = pregunta_05()
print(resultado)
