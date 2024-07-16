

# BANK ===============================================================================================================

import sys
from tkinter import filedialog
import os
import pandas as pd
import Result_Timepoint_Analyser
import Result_Surface_Analyser_I
import Result_Surface_Analyser_II
import Result_Surface_Analyser_III
import matplotlib.pyplot as plt
import seaborn as sns
TAB = """
"""
Timepoint_str = "timepoint"
surface_output_str = "Experiment_surface"
surface_cell_output_str = "Experiment_cellmax_surface"
Heatmap_str = "Matrix_Data"
Growth_str = "Growth"
Yield_str = "Yield"
All_factors_str = "All_Factors"
Substrate_str = "Substrate"
File_Name = "Unknown_"

# RUNNER =============================================================================================================

home_exp_directory = filedialog.askdirectory()
home_exp_directory_str = str(home_exp_directory)
results_folder = os.listdir(home_exp_directory_str)


if Growth_str in home_exp_directory_str:
    File_Name = "Growth_"
if Yield_str in home_exp_directory_str:
    File_Name = "Yield_"
if Substrate_str in home_exp_directory_str:
    File_Name = "Substrate_"
if All_factors_str in home_exp_directory_str:
    File_Name = "All_Factors_"


for file in results_folder:
        ### TIME-POINT ###
    if Timepoint_str in file:
        Result_Timepoint_Analyser.all_timepoint_plotter(f"{home_exp_directory}/{File_Name}Experiment_timepoint_data_xlsx.xlsx",
                                                   home_exp_directory)
        plt.clf()
        plt.close()

         ### SURFACE I ###
    if surface_cell_output_str in file:
        Result_Surface_Analyser_I.all_cells_plotter(f"{home_exp_directory}/{File_Name}Experiment_cellmax_surface_data_xlsx.xlsx",
                                                  home_exp_directory)
        plt.clf()
        plt.close()
    if surface_output_str in file:
        Result_Surface_Analyser_I.all_cells_plotter(f"{home_exp_directory}/{File_Name}Experiment_surface_data_xlsx.xlsx",
                                                  home_exp_directory)
        plt.clf()
        plt.close()

        ### SURFACE II ###
    if surface_cell_output_str in file:
        Result_Surface_Analyser_II.surface_plotter_II(f"{home_exp_directory}/{File_Name}Experiment_cellmax_surface_data_xlsx.xlsx",
                                                  home_exp_directory)
        plt.clf()
        plt.close()
    if surface_output_str in file:
        Result_Surface_Analyser_II.surface_plotter_II(f"{home_exp_directory}/{File_Name}Experiment_surface_data_xlsx.xlsx",
                                                  home_exp_directory)
        plt.clf()
        plt.close()

        ### SURFACE III ###
    if surface_cell_output_str in file:
        Result_Surface_Analyser_III.surface_plotter_III(f"{home_exp_directory}/{File_Name}Experiment_cellmax_surface_data_xlsx.xlsx",
                                                  home_exp_directory)
    if surface_output_str in file:
        Result_Surface_Analyser_III.surface_plotter_III(f"{home_exp_directory}/{File_Name}Experiment_surface_data_xlsx.xlsx",
                                                  home_exp_directory)


