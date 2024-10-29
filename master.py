import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os
import time

# Configurar el logger para informar el proceso paso a paso
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configuración de los parámetros
num_datos = 1000
dominio = "example.com"

# Generar datos ficticios
logging.info("Generando datos ficticios...")
np.random.seed(int(time.time()))  # Usar el tiempo actual como semilla para obtener diferentes resultados cada vez
peticiones = np.random.randint(1, 1000, size=num_datos)  # Número de peticiones
tiempos_respuesta = np.random.normal(loc=200, scale=50, size=num_datos)  # Tiempos de respuesta en ms

# Crear un DataFrame
logging.info("Creando DataFrame con los datos generados...")
datos = pd.DataFrame({
    'Dominio': [dominio] * num_datos,
    'Peticiones': peticiones,
    'Tiempo_Respuesta': tiempos_respuesta
})

# Guardar en un archivo CSV
csv_file = 'datos_peticiones.csv'
logging.info(f"Guardando datos en el archivo CSV: {csv_file}...")
datos.to_csv(csv_file, index=False)
logging.info("Archivo CSV generado con éxito.")

# Leer el archivo CSV generado previamente
file_path = csv_file

# Verificar si el archivo existe
if not os.path.exists(file_path):
    logging.error(f"Archivo no encontrado: {file_path}. Por favor, verifique la ruta e inténtelo de nuevo.")
else:
    # Leer el archivo CSV
    logging.info("Leyendo el archivo CSV...")
    df = pd.read_csv(file_path)
    logging.info(f"DataFrame cargado exitosamente. Dimensiones: {df.shape}")

    # Definir los datos
    x = df['Peticiones']
    y = df['Tiempo_Respuesta']
    n = len(x)

    # Calcular sumatorias necesarias
    logging.info("Calculando sumatorias necesarias...")
    sum_x = np.sum(x)
    logging.info(f"Suma de x (Peticiones): {sum_x}")
    sum_y = np.sum(y)
    logging.info(f"Suma de y (Tiempo_Respuesta): {sum_y}")
    sum_xy = np.sum(x * y)
    logging.info(f"Suma de xy: {sum_xy}")
    sum_x2 = np.sum(x**2)
    logging.info(f"Suma de x^2: {sum_x2}")
    sum_y2 = np.sum(y**2)
    logging.info(f"Suma de y^2: {sum_y2}")

    # Calcular promedios
    logging.info("Calculando promedios...")
    mean_x = sum_x / n
    logging.info(f"Promedio de x (Peticiones): {mean_x}")
    mean_y = sum_y / n
    logging.info(f"Promedio de y (Tiempo_Respuesta): {mean_y}")

    # Calcular b1 y b0
    logging.info("Calculando coeficientes de la regresión lineal...")
    b1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    logging.info(f"Coeficiente b1: {b1}")
    b0 = mean_y - b1 * mean_x
    logging.info(f"Coeficiente b0: {b0}")

    # Calcular la correlación
    logging.info("Calculando coeficiente de correlación...")
    r = (n * sum_xy - sum_x * sum_y) / np.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))
    r_squared = r**2
    logging.info(f"Coeficiente de correlación (r): {r}")
    logging.info(f"Coeficiente de determinación (r^2): {r_squared}")

    # Determinar el tipo de correlación
    def tipo_correlacion(corr):
        if corr == 1:
            return "Correlación positiva perfecta"
        elif corr == -1:
            return "Correlación negativa perfecta"
        elif corr >= 0.7:
            return "Correlación positiva fuerte"
        elif corr <= -0.7:
            return "Correlación negativa fuerte"
        elif corr >= 0.5:
            return "Correlación positiva moderada"
        elif corr <= -0.5:
            return "Correlación negativa moderada"
        elif corr >= 0.3:
            return "Correlación positiva débil"
        elif corr <= -0.3:
            return "Correlación negativa débil"
        else:
            return "Sin correlación"

    corr_texto = tipo_correlacion(r)
    logging.info(f"Tipo de correlación: {corr_texto}")

    # Calcular predicciones
    logging.info("Calculando predicciones...")
    y_pred = b0 + b1 * x

    # Preparar el gráfico de dispersión
    logging.info("Preparando el gráfico de dispersión...")
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x=x, y=y, color='blue', label='Datos reales')
    sns.lineplot(x=x, y=y_pred, color='red', label='Regresión lineal')
    #Poner el título y etiquetas de los ejes y cuantos datos se tienen
    plt.title('Gráfico de Dispersión')
    plt.xlabel('Peticiones')
    plt.ylabel('Tiempo de Respuesta')
    plt.text(x.min(), y.min(), f'Datos: {n}', fontsize=10)
    # Poner valores de b0 y b1 y r
    plt.text(x.min(), y.min() + 50, f'b0={b0:.2f}, b1={b1:.2f}, r={r:.2f}')
    plt.text(x.min(), y.max(), f'Correlación: {corr_texto}', fontsize=10)
    plt.legend()
    plt.show()
    logging.info("Gráfico de dispersión generado y mostrado.")

    # Guardar los resultados en un archivo CSV
    logging.info("Guardando los resultados en un archivo CSV...")
    df['y_pred'] = y_pred
    df.to_csv('resultados_regresion.csv', index=False)
    logging.info("Resultados finales impresos y exportados a CSV.")
    logging.info("Proceso completado exitosamente.")
