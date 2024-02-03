import pandas
import numpy as np
import matplotlib.pyplot as plt

doc = pandas.read_csv("dataset/dataset02.csv")

print("doc: \n", doc)

# Obtener las columnas 'x' de las filas y guardarlas en una lista
columnas_x = [[1] + list(row.drop('y')) for index, row in doc.iterrows()]

# Obtener la columna 'y' y guardarla en una lista
columna_y = list(doc['y'])



# Generar un arreglo de números aleatorios entre -1 y 1 para los pesos iniciales
pesos = np.random.uniform(low=-1, high=1, size=(1, len(columnas_x[0])))

print("Columnas X:", columnas_x)
print("Columna Y:", columna_y)
print("pesos (W):", pesos)

coords_norma = []
coords_pesos = []

for i in range(100):
    # aca obtener coords de peso
    coords_pesos.append(np.squeeze(pesos))

    suma_ponderada = np.linalg.multi_dot([columnas_x, pesos.T])
    activada = np.where(suma_ponderada < 0, 0, 1)

    error = activada.flatten() - columna_y
    #error = columna_y - activada.flatten()
    norma_error = np.linalg.norm(error)
    print("norma error:", norma_error)
    # guardar norma del error como coords [gen, norma]
    coords_norma.append([i, norma_error])

    eta = 0.1

    # revisar este pedo
    incremento_pesos = -eta * np.dot(error.T, columnas_x)

    pesos = pesos + incremento_pesos
'''
print("c-e: ", coords_norma)
print("c-p: ", coords_pesos)

# Graficar la evolución de la norma del error
coords_norma = np.array(coords_norma)
plt.plot(coords_norma[:, 0], coords_norma[:, 1], marker='o')
plt.title('Evolución de la Norma del Error')
plt.xlabel('Iteración')
plt.ylabel('Norma del Error')
plt.show()

coords_pesos = np.array(coords_pesos)
for i in range(coords_pesos.shape[1]):
    plt.plot(coords_pesos[:, i], label=f'Peso {i + 1}')

plt.title('Evolución de los Pesos por Iteración')
plt.xlabel('Iteración')
plt.ylabel('Valor del Peso')
plt.legend()
plt.show()
'''