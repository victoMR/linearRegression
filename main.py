"""
Linear Regression program
Fecha de creacion: 2021-09-17

Este programa realiza una regresion lineal simple a partir de dos conjuntos de datos

-------------------------------------------
Datos 1:
Trafico de datos : [3,5,7,9,11]
Consumo Energetico (kWh) : [45,50,55,60,65]
-------------------------------------------
Datos 2:
Numero de ataqes detectados ( por dia ) : [5,8,12,15,20,22,25,28,30,33,35,38,40,42,45,48,50,52,55]
Tiempo de respuesta (seg) : [1.2,1.8,2.3,2.8,3.1,3.5,3.9,4.2,4.6,4.8,5.2,5.6,5.9,6.2,6.4,6.9,7.3,7.6,8.0,8.3]
-------------------------------------------

Se puede obtener correlacion negativa perfecta, correlacion positiva perfecta,
correlacion negativa fuerte, correlacion positiva fuerte, correlacion negativa moderada,
correlacion positiva moderada, correlacion negativa debil, correlacion positiva debil,
correlacion nula .

Procedimiento:
0. Definir los datos y contar cuantos datos hay en cada uno de los conjuntos
1. Esturcturar los datos en forma de listas y o tablas de cada uno de los datos
2. Multiplicar los valores en forma x * y de cada uno de los datos
3. Sumar los valores de cada uno de los datos osea sumar los valores de x y de y y de x*y
4. Sacar los valores de x al cuadrado y de y al cuadrado
5. Sumar los valores de x al cuadrado y de y al cuadrado
6. Aplicar la formula para sacar la diferecia de y con esta formula dif de y = b0 + b1*x
7. Aplicar la formula para sacar b0 en esta formula b0 = promedio de y - b1 * promedio de x
8. Aplicar la formula para sacar promedio de y con esta formula promedio de y = sumatoria de y / n
9. Aplicar la formula para sacar promedio de x con esta formula promedio de x = sumatoria de x / n
10. Aplicar la formula para sacar b1 con esta formula b1 = n * sumatoria de x*y - sumatoria de x * sumatoria de y / n * sumatoria de x al cuadrado - (sumatoria de x) al cuadrado
11. Aplicar la formula para sacar la correlacion con esta formula r = n * sumatoria de x*y - sumatoria de x * sumatoria de y / raiz cuadrada de n * sumatoria de x al cuadrado - (sumatoria de x) al cuadrado * raiz cuadrada de n * sumatoria de y al cuadrado - (sumatoria de y) al cuadrado
12. Aplicar la formula para sacar la prediccion con esta formula prediccion = b0 + b1*x
14. Sacar r con las operaciones de la formula de r
15. Sacar la correlacion con las operaciones de la formula de r
16. Sacar la prediccion con las operaciones de la formula de prediccion
17. Mostrar los resultados de la correlacion y de la prediccion con los datos de x y de y , con graficas de los datos de x y de y y de la prediccion

"""
# Importar librerías
import matplotlib.pyplot as plt
import numpy as np
import logging

# Configurar el logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Definir los datos
# Datos 1: Tráfico de datos vs Consumo Energético
x1 = [3, 5, 7, 9, 11]
y1 = [45, 50, 55, 60, 65]

# Datos 2: Número de ataques detectados vs Tiempo de respuesta
x2 = [5, 8, 12, 15, 20, 22, 25, 28, 30, 33, 35, 38, 40, 42, 45, 48, 50, 52, 55]
y2 = [1.2, 1.8, 2.3, 2.8, 3.1, 3.5, 3.9, 4.2, 4.6, 4.8, 5.2, 5.6, 5.9, 6.2, 6.4, 6.9, 7.3, 7.6, 8.0, 8.3]

# Contar la cantidad de datos en cada conjunto
n1 = len(x1)
n2 = len(x2)

# Verificar que haya suficientes datos
if n1 < 2 or n2 < 2:
    logging.error("Se requieren al menos 2 datos en cada conjunto para poder hacer regresión lineal.")
    raise ValueError("Datos insuficientes.")

# Calcular los parámetros de regresión lineal para el primer conjunto de datos
logging.info("Calculando parámetros de regresión lineal para el primer conjunto de datos...")
x1_arr = np.array(x1)
y1_arr = np.array(y1)
sum_x1 = np.sum(x1_arr)
sum_y1 = np.sum(y1_arr)
sum_xy1 = np.sum(x1_arr * y1_arr)
sum_x1_sq = np.sum(x1_arr ** 2)
b1 = (n1 * sum_xy1 - sum_x1 * sum_y1) / (n1 * sum_x1_sq - sum_x1 ** 2)
b0_1 = np.mean(y1_arr) - b1 * np.mean(x1_arr)
y1_pred = b0_1 + b1 * x1_arr
r1 = (n1 * sum_xy1 - sum_x1 * sum_y1) / (np.sqrt(n1 * sum_x1_sq - sum_x1 ** 2) * np.sqrt(n1 * np.sum(y1_arr ** 2) - sum_y1 ** 2))
corr1 = r1 ** 2

# Determinar el tipo de correlación para el primer conjunto de datos
if corr1 >= 0.9:
    corr1_text = "correlación positiva muy fuerte"
elif corr1 >= 0.7:
    corr1_text = "correlación positiva fuerte"
elif corr1 >= 0.5:
    corr1_text = "correlación positiva moderada"
elif corr1 >= 0.3:
    corr1_text = "correlación positiva débil"
elif corr1 <= -0.9:
    corr1_text = "correlación negativa muy fuerte"
elif corr1 <= -0.7:
    corr1_text = "correlación negativa fuerte"
elif corr1 <= -0.5:
    corr1_text = "correlación negativa moderada"
elif corr1 <= -0.3:
    corr1_text = "correlación negativa débil"
else:
    corr1_text = "correlación nula"

logging.info(f"La correlación es {corr1_text}")
logging.info(f"Resultados del primer conjunto de datos: b0={b0_1:.2f}, b1={b1:.2f}, Correlación={corr1:.2f}")

# Calcular los parámetros de regresión lineal para el segundo conjunto de datos
logging.info("Calculando parámetros de regresión lineal para el segundo conjunto de datos...")
x2_arr = np.array(x2)
y2_arr = np.array(y2)

# Asegurar que x2_arr y y2_arr tengan la misma longitud
if len(x2_arr) > len(y2_arr):
    x2_arr = x2_arr[:len(y2_arr)]
elif len(y2_arr) > len(x2_arr):
    y2_arr = y2_arr[:len(x2_arr)]

sum_x2 = np.sum(x2_arr)
sum_y2 = np.sum(y2_arr)
sum_xy2 = np.sum(x2_arr * y2_arr)
sum_x2_sq = np.sum(x2_arr ** 2)
b1_2 = (len(x2_arr) * sum_xy2 - sum_x2 * sum_y2) / (len(x2_arr) * sum_x2_sq - sum_x2 ** 2)
b0_2 = np.mean(y2_arr) - b1_2 * np.mean(x2_arr)
y2_pred = b0_2 + b1_2 * x2_arr
r2 = (len(x2_arr) * sum_xy2 - sum_x2 * sum_y2) / (np.sqrt(len(x2_arr) * sum_x2_sq - sum_x2 ** 2) * np.sqrt(len(x2_arr) * np.sum(y2_arr ** 2) - sum_y2 ** 2))
corr2 = r2 ** 2

# Determinar el tipo de correlación para el segundo conjunto de datos
if corr2 >= 0.9:
    corr2_text = "correlación positiva muy fuerte"
elif corr2 >= 0.7:
    corr2_text = "correlación positiva fuerte"
elif corr2 >= 0.5:
    corr2_text = "correlación positiva moderada"
elif corr2 >= 0.3:
    corr2_text = "correlación positiva débil"
elif corr2 <= -0.9:
    corr2_text = "correlación negativa muy fuerte"
elif corr2 <= -0.7:
    corr2_text = "correlación negativa fuerte"
elif corr2 <= -0.5:
    corr2_text = "correlación negativa moderada"
elif corr2 <= -0.3:
    corr2_text = "correlación negativa débil"
else:
    corr2_text = "correlación nula"

logging.info(f"La correlación es {corr2_text}")
logging.info(f"Resultados del segundo conjunto de datos: b0={b0_2:.2f}, b1={b1_2:.2f}, Correlación={corr2:.2f}")

# Graficar los resultados
logging.info("Generando gráficas...")
plt.figure(figsize=(12, 6))

# Gráfica 1: Tráfico de datos vs Consumo Energético
plt.subplot(1, 2, 1)
plt.scatter(x1, y1, color='blue')
plt.plot(x1, y1_pred, color='red')
plt.title('Tráfico de datos vs Consumo Energético')
plt.xlabel('Tráfico de datos')
plt.ylabel('Consumo Energético')
plt.text(3, 55, f'Correlación: {corr1_text}', fontsize=10)

# Gráfica 2: Número de ataques detectados vs Tiempo de respuesta
plt.subplot(1, 2, 2)
plt.scatter(x2_arr, y2_arr, color='blue')
plt.plot(x2_arr, y2_pred, color='red')
plt.title('Número de ataques detectados vs Tiempo de respuesta')
plt.xlabel('Número de ataques detectados')
plt.ylabel('Tiempo de respuesta')
plt.text(5, 7.5, f'Correlación: {corr2_text}', fontsize=10)

plt.tight_layout()
plt.show()
logging.info("Gráficas generadas exitosamente.")

# Imprimir resultados
logging.info("Imprimiendo resultados finales...")
print('Resultados del primer conjunto de datos:')
print(f'b0: {b0_1:.2f}')
print(f'b1: {b1:.2f}')
print(f'Correlación: {corr1_text}')

print('\nResultados del segundo conjunto de datos:')
print(f'b0: {b0_2:.2f}')
print(f'b1: {b1_2:.2f}')
print(f'Correlación: {corr2_text}')
logging.info("Resultados finales impresos.")
