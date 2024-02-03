# Execute this file in order to try te perceptron algorithm.
# Here you will find the interface and the execution call.


import customtkinter
from tkinter import messagebox, filedialog

import perceptron

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


def load_file():
    global file_path
    file = filedialog.askopenfilename(title="Choose file", filetypes=[("Archivos de texto", "*.csv")])
    file_path = file


def start():
    matrix_x, matrix_y_d, matrix_w = perceptron.initialize(file_path)
    perceptron.optimization(matrix_x, matrix_y_d, matrix_w, float(input_eta.get()), float(input_tolerance.get()),
                            int(input_iteration.get()))


app = customtkinter.CTk()
app.geometry("430x250")
app.title("IA C2 A1 Perceptron 01")
app.resizable(False, False)

master_frame01 = customtkinter.CTkFrame(master=app, width=430, height=150, fg_color="transparent")

frame0 = customtkinter.CTkFrame(master=master_frame01, width=430, height=75, fg_color="transparent")
customtkinter.CTkLabel(master=frame0, text="Initialization", width=430, ).pack(fill="x", expand=True)
frame0.pack(side="top", fill="x", expand=True)

frame01 = customtkinter.CTkFrame(master=master_frame01, width=210, height=75, fg_color="transparent")
customtkinter.CTkLabel(master=frame01, text="Eta: ", width=100).pack(side="left")
input_eta = customtkinter.CTkEntry(master=frame01, width=100)
input_eta.pack()
frame01.pack(padx=5, pady=5, side="left")

frame02 = customtkinter.CTkFrame(master=master_frame01, width=210, height=75, fg_color="transparent")
customtkinter.CTkLabel(master=frame02, text="Tolerancia: ", width=100).pack(side="left")
input_tolerance = customtkinter.CTkEntry(master=frame02, width=100)
input_tolerance.pack()
frame02.pack(padx=5, pady=5, side="left")
master_frame01.pack(pady=5, padx=10, side="top")

master_frame02 = customtkinter.CTkFrame(master=app, width=430, height=150, fg_color="transparent")
frame04 = customtkinter.CTkFrame(master=master_frame02, width=210, height=75, fg_color="transparent")
customtkinter.CTkLabel(master=frame04, text="Iterations: ", width=100).pack(side="left")
input_iteration = customtkinter.CTkEntry(master=frame04, width=100)
input_iteration.pack()
frame04.pack(side="left", padx=10)
frame05  = customtkinter.CTkFrame(master=master_frame02, width=210, height=75, fg_color="transparent")
bttn_load_file = customtkinter.CTkButton(master=frame05, text="Load CSV file", command=load_file, width=140)
bttn_load_file.pack(pady=10)
frame05.pack(side="left", padx=10)
master_frame02.pack(padx=10, pady=5)

master_frame03 = customtkinter.CTkFrame(master=app, width=430, height=150, fg_color="transparent")
bttn_start = customtkinter.CTkButton(master=master_frame03, text="Start Perceptron Algorithm", command=start, width=300)
bttn_start.pack(pady=30)
master_frame03.pack()

app.mainloop()

# By Jesus Antonio Gordillo Orantes 213359