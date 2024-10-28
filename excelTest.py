# Importar librerías necesarias
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
import os
import logging

# Configurar el logger para informar el proceso paso a paso
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Definir los datos de entrada
x1 = [3, 5, 7, 9, 11]
y1 = [45, 50, 55, 60, 65]
x2 = [5, 8, 12, 15, 20, 22, 25, 28, 30, 33, 35, 38, 40, 42, 45, 48, 50, 52, 55]
y2 = [1.2, 1.8, 2.3, 2.8, 3.1, 3.5, 3.9, 4.2, 4.6, 4.8, 5.2, 5.6, 5.9, 6.2, 6.4, 6.9, 7.3, 7.6, 8.0]

# Función para calcular regresión lineal y correlación
def calcular_regresion(x, y):
    n = len(x)
    x_arr = np.array(x)
    y_arr = np.array(y)
    sum_x = np.sum(x_arr)
    sum_y = np.sum(y_arr)
    sum_xy = np.sum(x_arr * y_arr)
    sum_x_sq = np.sum(x_arr ** 2)
    sum_y_sq = np.sum(y_arr ** 2)
    b1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_sq - sum_x ** 2)
    b0 = np.mean(y_arr) - b1 * np.mean(x_arr)
    r = (n * sum_xy - sum_x * sum_y) / (np.sqrt(n * sum_x_sq - sum_x ** 2) * np.sqrt(n * sum_y_sq - sum_y ** 2))
    return b0, b1, r ** 2

# Calcular los parámetros y correlación para cada conjunto de datos
b0_1, b1_1, corr1 = calcular_regresion(x1, y1)
b0_2, b1_2, corr2 = calcular_regresion(x2, y2)

# Función para determinar el tipo de correlación
def tipo_correlacion(corr):
    if corr >= 0.9:
        return "correlación positiva muy fuerte"
    elif corr >= 0.7:
        return "correlación positiva fuerte"
    elif corr >= 0.5:
        return "correlación positiva moderada"
    elif corr >= 0.3:
        return "correlación positiva débil"
    elif corr <= -0.9:
        return "correlación negativa muy fuerte"
    elif corr <= -0.7:
        return "correlación negativa fuerte"
    elif corr <= -0.5:
        return "correlación negativa moderada"
    elif corr <= -0.3:
        return "correlación negativa débil"
    else:
        return "correlación nula"

# Preparar la gráfica
def graficar(x, y, y_pred, titulo, xlabel, ylabel, corr_texto):
    plt.scatter(x, y, color='blue')
    plt.plot(x, y_pred, color='red')
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.text(min(x), max(y), f'Correlación: {corr_texto}', fontsize=10)

# Calcular predicciones
y1_pred = [b0_1 + b1_1 * xi for xi in x1]
y2_pred = [b0_2 + b1_2 * xi for xi in x2]

# Graficar ambos conjuntos de datos
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
graficar(x1, y1, y1_pred, 'Tráfico de datos vs Consumo Energético', 'Tráfico de datos', 'Consumo Energético', tipo_correlacion(corr1))
plt.subplot(1, 2, 2)
graficar(x2, y2, y2_pred, 'Número de ataques detectados vs Tiempo de respuesta', 'Número de ataques detectados', 'Tiempo de respuesta', tipo_correlacion(corr2))
plt.tight_layout()
plt.show()

# Crear archivo de Excel y guardar los resultados
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Resultados de Regresión"

# Agregar resultados al archivo de Excel
ws.append(["Conjunto de Datos", "b0 (Intercepto)", "b1 (Pendiente)", "Correlación", "Tipo de Correlación"])
ws.append(["Tráfico de datos vs Consumo Energético", b0_1, b1_1, corr1, tipo_correlacion(corr1)])
ws.append(["Número de ataques detectados vs Tiempo de respuesta", b0_2, b1_2, corr2, tipo_correlacion(corr2)])

# Definir la ruta específica donde se guardará el archivo de Excel
ruta_excel = r"C:\Users\raton\Downloads\resultados_regresion.xlsx"

# Guardar el archivo de Excel en la ruta especificada
wb.save(ruta_excel)
print(f"Resultados exportados a {ruta_excel}")

# Intentar abrir el archivo automáticamente después de guardarlo
try:
    os.startfile(ruta_excel)  # En Windows
    # os.system(f"open {ruta_excel}")  # En Mac
    # os.system(f"xdg-open {ruta_excel}")  # En Linux
except Exception as e:
    print("No se pudo abrir el archivo automáticamente:", e)

# Imprimir resultados en consola
print('Resultados del primer conjunto de datos:')
print(f'b0: {b0_1:.2f}')
print(f'b1: {b1_1:.2f}')
print(f'Correlación: {tipo_correlacion(corr1)}')

print('\nResultados del segundo conjunto de datos:')
print(f'b0: {b0_2:.2f}')
print(f'b1: {b1_2:.2f}')
print(f'Correlación: {tipo_correlacion(corr2)}')

logging.info("Resultados finales impresos y exportados a Excel.")
