

# BANK ===========================================================================================================

import h5py
import pandas as pd
import math
from tkinter import filedialog
import matplotlib.pyplot as plt
import seaborn as sns
import os

TAB = """
    """
preset_str = ""
type_preset_str = ""
label_preset_str = ""
surface_cell_output_str = "Experiment_cellmax_surface"
Growth_str = "Growth"
Yield_str = "Yield"
Substrate_str = "Substrate"
Matrix_folder_str = "Matrix_Data"
CellMax_Str = "CellMax"
Growth_dictionary = {"0.00008": "S1", "0.00028": "S2", "0.00048": "S3", "0.00068": "S4", "0.00088": "S5", "0.00108": "S6", "0.00128": "S7",
                     "0.00148": "S8"}
Yield_dictionary = {"0.41": "S1", "0.46": "S2", "0.51": "S3", "0.56": "S4", "0.61": "S5", "0.66": "S6", "0.71": "S7", "0.76": "S8"}
Substrate_dictionary = {"0.000005": "S1", "0.000015": "S2", "0.000025": "S3", "0.000035": "S4", "0.000045": "S5", "0.000055": "S6",
                        "0.000065": "S7", "0.000075": "S8"}
palette = "viridis"


# PLOTTER ========================================================================================================

# filename = filedialog.askopenfilename()
home_exp_directory = filedialog.askdirectory()

matrix_folder = os.listdir(home_exp_directory)

if Growth_str in home_exp_directory:
    type_preset_str = "Growth_"
    label_preset_str = "Growth"
    label_dictionary = Growth_dictionary
if Yield_str in home_exp_directory:
    type_preset_str = "Yield_"
    label_preset_str = "Yield"
    label_dictionary = Yield_dictionary
if Substrate_str in home_exp_directory:
    type_preset_str = "Substrate_"
    label_preset_str = "Substrate"
    label_dictionary = Substrate_dictionary

cell_max_running = 0
min_h = 0
max_h = 0.000099
height_delta_str = ""
for file in matrix_folder:
    print(file)
    if CellMax_Str in file:
        palette = "rocket"
        cell_max_running = 1
    if file.endswith(".xlsx"):
        for key, value in label_dictionary.items():
            if value in file:
                sample_name = key
        print("file found")
        data_path = f"{home_exp_directory}/{file}"
        data = pd.read_excel(data_path)
        if cell_max_running == 1:
            min_h = data.min().min()
            max_h = data.max().max()
            height_delta = max_h - min_h
            height_delta = round(height_delta, 6)
            height_delta_str = f"; Height delta = {height_delta:.1e}"
        print(data)
        sns.heatmap(data=data, annot=False, cmap=palette, vmin=min_h, vmax=max_h)
        plt.xlabel("X-Dimension")
        plt.ylabel("Y-Dimension")
        plt.title(f"Biofilm height heatmap \n [{label_preset_str} Factor: {sample_name}{height_delta_str}]")
        file_str = file.replace(".xlsx", "")
        plt.savefig(f"{home_exp_directory}/{file_str}_Heatmap")
        plt.clf()




