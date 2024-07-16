
# BANK ===============================================================================================================

import sys
from tkinter import filedialog
import os
import pandas as pd
import Result_Surface_Analyser_I
import matplotlib.pyplot as plt
import seaborn as sns
import shutil
TAB = """
"""
all_cell_files = "TimepointNumbers"
surface_output_files = "SurfaceOutput"
surface_cell_output_files = "CellMax"
matrix_files = "SurfaceMatrix"
first_replicate = "R1"
Growth_str = "Growth"
Yield_str = "Yield"
replicate_num = 0
series_num = 0
series_list_num = 0
surface_columns = ["Surface_Area","Perfect_Smooth_Area","SD_Height","Av_Height","Est_ADAM","Overgrowth","SFA", "SFA_alt", "NUFEB_rough","N.P","N.C","N.E","Sample_Num", "Replicate_Num"]
timepoint_columns = ["Timepoint", "Cells", "EPS", "Sample_Num", "Replicate_Num"]
Samples_dictionary = {1: "S1", 2: "S2", 3: "S3", 4: "S4", 5: "S5", 6: "S6", 7: "S7",
                     8: "S8"}
Replicates_dictionary = {1: "R1_", 2: "R2", 3: "R3", 4: "R4", 5: "R5", 6: "R6", 7: "R7",
                     8: "R8", 9: "R9", 10: "R10"}
timepoints_num = 90
timepoints_list = []
matrix_dictionary = {}
surface_df = pd.DataFrame(columns=surface_columns)
cell_timepoint_df = pd.DataFrame()
eps_timepoint_df = pd.DataFrame()
timepoint_df = pd.DataFrame(columns=timepoint_columns)

# EXPLORER ===========================================================================================================

home_exp_directory = filedialog.askdirectory()
# home_exp_directory = sys.argv[1]
home_exp_directory_str = str(home_exp_directory)
experiment_replicates = os.listdir(home_exp_directory_str)

timepoint_lister_step = 0
timepoint_value = 0
timepoints_list.append(timepoint_value)
while True:
    if timepoint_lister_step < timepoints_num:
        timepoint_value = timepoint_value + 10
        timepoints_list.append(timepoint_value)
        timepoint_lister_step = timepoint_lister_step + 1
    else:
        break

cell_timepoint_df["Timepoint"] = timepoints_list
eps_timepoint_df["Timepoint"] = timepoints_list

for replicate in experiment_replicates:
    if not replicate.endswith(".xlsx"):
        if not replicate.endswith(".png"):
            if not replicate.endswith(".nufeb"):
                if not replicate.endswith(".in"):
                    if not replicate.endswith(".sh"):
                        if not replicate.endswith(".txt"):
                            replicate_directory = home_exp_directory_str + "/" + replicate
                            series_sample_list = os.listdir(replicate_directory)
                            replicate_num = experiment_replicates.index(replicate)+1
                            for series in series_sample_list:
                                series_directory = replicate_directory + "/" + series
                                file_list = os.listdir(series_directory)
                                series_num = series_sample_list.index(series)+1
                                for file in file_list:
                                    if first_replicate in replicate:
                                        if matrix_files in file:
                                            matix_file_path = series_directory + "/" + file
                                            matix_file_path_str = str(matix_file_path)
                                            matrix_dictionary[file] = matix_file_path_str
                                    if all_cell_files in file:
                                        all_cell_files_directory = series_directory + "/" + file
                                        print(
                                            "-------------------------------------------------------------------------------------")
                                        print("The file at following directory is being used:")
                                        print(all_cell_files_directory)
                                        timepoint_file = pd.read_csv(all_cell_files_directory)
                                        cell_timepoint_df[f"C_{replicate}_{series}"] = timepoint_file["Num_Cells"]
                                        eps_timepoint_df[f"E_{replicate}_{series}"] = timepoint_file["Num_EPS"]
                                        timepoint_values = timepoint_file["Timepoint"].tolist()
                                        cell_values = timepoint_file["Num_Cells"].tolist()
                                        eps_values = timepoint_file["Num_EPS"].tolist()
                                        for key, value in Samples_dictionary.items():
                                            if value in file:
                                                temp_sample_name = key
                                        for key, value in Replicates_dictionary.items():
                                            if value in file:
                                                temp_replicate_name = key
                                        temp_dictionary = {
                                            "Timepoint": timepoint_values,
                                            "Cells": cell_values,
                                            "EPS": eps_values,
                                            "Sample_Num": temp_sample_name,
                                            "Replicate_Num": temp_replicate_name,
                                        }
                                        temp_df = pd.DataFrame(temp_dictionary)
                                        timepoint_df = pd.concat([timepoint_df, temp_df], ignore_index=True)
                                    elif surface_output_files in file:
                                        if surface_cell_output_files not in file:
                                            surface_output_files_directory = series_directory + "/" + file
                                            print("-------------------------------------------------------------------------------------")
                                            print("The file at following directory is being used:")
                                            print(surface_output_files_directory)
                                            surface_file = pd.read_excel(surface_output_files_directory)
                                            print(surface_file)
                                            val_s_area = surface_file.iloc[1, 1]
                                            val_ps_area = surface_file.iloc[2, 1]
                                            val_SDh = surface_file.iloc[3, 1]
                                            val_avh = surface_file.iloc[4, 1]
                                            val_est_ADAM = surface_file.iloc[5, 1]
                                            val_over = surface_file.iloc[7, 1]
                                            val_SFA = surface_file.iloc[9, 1]
                                            val_SFA_alt = surface_file.iloc[13, 1]
                                            num_p = surface_file.iloc[10, 1]
                                            num_c = surface_file.iloc[11, 1]
                                            num_e = surface_file.iloc[12, 1]
                                            val_NUFEB = surface_file.iloc[14, 1]
                                            new_row = [val_s_area,val_ps_area,val_SDh,val_avh,val_est_ADAM,val_over, val_SFA, val_SFA_alt, val_NUFEB, num_p, num_c , num_e , series_num,replicate_num]
                                            surface_df.loc[len(surface_df)] = new_row
                                            print(TAB)
                                        if surface_cell_output_files in file:
                                            print(TAB)

# CLEANER ============================================================================================================

File_Name = "Unknown_"

if Growth_str in home_exp_directory_str:
    surface_df["Sample_Num"] = surface_df["Sample_Num"].replace(
        {1: "0.0008", 2: "0.0028", 3: "0.0048", 4: "0.0068", 5: "0.0088", 6: "0.0108", 7: "0.0128", 8: "0.0148"})
    timepoint_df["Sample_Num"] = timepoint_df["Sample_Num"].replace(
        {1: "0.0008", 2: "0.0028", 3: "0.0048", 4: "0.0068", 5: "0.0088", 6: "0.0108", 7: "0.0128", 8: "0.0148"})
    File_Name = "Growth_"
if Yield_str in home_exp_directory_str:
    surface_df["Sample_Num"] = surface_df["Sample_Num"].replace(
        {1: "0.41", 2: "0.46", 3: "0.51", 4: "0.56", 5: "0.61", 6: "0.66", 7: "0.71", 8: "0.76"})
    timepoint_df["Sample_Num"] = timepoint_df["Sample_Num"].replace(
        {1: "0.41", 2: "0.46", 3: "0.51", 4: "0.56", 5: "0.61", 6: "0.66", 7: "0.71", 8: "0.76"})
    File_Name = "Yield_"

# EXPORTER ===========================================================================================================

os.makedirs(f"{home_exp_directory}/{File_Name}Matrix_Data")
for key, value in matrix_dictionary.items():
    source_matrix_path = value
    copied_matrix_path = f"{home_exp_directory}/{File_Name}Matrix_Data/{key}"
    shutil.copy(source_matrix_path, copied_matrix_path)


savedir_con_surf = f"{home_exp_directory}/{File_Name}Experiment_surface_data_xlsx.xlsx"
savedir_con_time = f"{home_exp_directory}/{File_Name}Experiment_timepoint_data_xlsx.xlsx"
surface_df.to_excel(savedir_con_surf, sheet_name="A", index=False)
timepoint_df.to_excel(savedir_con_time, sheet_name="A", index=False)

# RUNNER =============================================================================================================

print(surface_df)

Result_Surface_Analyser.all_cells_plotter(f"{home_exp_directory}/Experiment_surface_data_xlsx.xlsx",home_exp_directory)
