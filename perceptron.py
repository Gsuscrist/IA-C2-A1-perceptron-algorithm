from tkinter import messagebox

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def generate_norm_evolution_graphic(norm_data):
    norm_data = np.array(norm_data)
    plt.plot(norm_data[:, 0], norm_data[:, 1], marker='o')
    plt.title('Error norm evolution')
    plt.xlabel('Generation')
    plt.ylabel('Error norm')
    plt.show()


def generate_weight_evolution_graphic(weight_data):
    weight_data = np.array(weight_data)
    for i in range(weight_data.shape[1]):
        plt.plot(weight_data[:, i], label=f'Weight {i}')
    plt.title('Weight evolution')
    plt.xlabel('Generation')
    plt.ylabel('Weight value')
    plt.legend()
    plt.show()


def show_sum_up(best_gen_initial, weight_data, eta, tolerance_error):
    message = (f'initial weight: {weight_data[0]} \n'
               f'final weight: {weight_data[-1]} \n'
               f'eta: {eta} \n'
               f'tolerance error: {tolerance_error} \n'
               f'iterations until reach acceptance value: {best_gen_initial[0]+1}\n')
    messagebox.showinfo("information", message)


def get_start_best_gen(norm_data):
    min = float('inf')  # Inicializamos con infinito para asegurarnos de que cualquier valor en la lista sea menor
    best_element = None
    for norm in norm_data:
        valor = norm[1]
        if 0 <= valor < min:
            min = valor
            best_element = norm
    return best_element


def optimization(matrix_x, matrix_y_d, matrix_w, eta, tolerance_error, iterations):
    norm_data = []
    weight_data = []
    for i in range(iterations):
        weight_data.append(np.copy(np.squeeze(matrix_w)))
        matrix_u = np.linalg.multi_dot([matrix_x, matrix_w.T])
        matrix_y_c = np.where(matrix_u < 0, 0, 1)
        error = matrix_y_d - matrix_y_c
        norm_error = np.linalg.norm(error)
        print("ne: ", norm_error)
        norm_data.append([i, norm_error])
        if tolerance_error >= norm_error >= 0 or norm_error == 0:
            matrix_w = matrix_w
        else:
            matrix_delta_w = eta * np.dot(error.T, matrix_x)
            matrix_w = matrix_w + matrix_delta_w
    best_gen_initial = get_start_best_gen(norm_data)
    show_sum_up(best_gen_initial, weight_data, eta, tolerance_error)
    generate_norm_evolution_graphic(norm_data)
    generate_weight_evolution_graphic(weight_data)


def initialize(file_path):
    csv_doc = pd.read_csv(file_path, header=None)
    matrix_x = np.hstack((np.ones((len(csv_doc), 1)), csv_doc.iloc[:, :-1].values))
    matrix_y_d = csv_doc.iloc[:, -1].values.reshape(-1, 1)
    matrix_w = np.random.uniform(low=-1, high=1, size=(1, matrix_x.shape[1]))
    return matrix_x, matrix_y_d, matrix_w
