
# BANK ===============================================================================================================

import sys
from tkinter import filedialog
import os
import HDF5_Surface_Finder
import HDF5_Cell_Reader
import HDF5_CellMaxSurface_Finder
TAB = """
"""
series_num = 0

# FOLDER FINDER ======================================================================================================

home_exp_directory = filedialog.askdirectory()
# home_exp_directory = sys.argv
home_exp_directory_str = str(home_exp_directory)
experiment_replicates = os.listdir(home_exp_directory_str)

for replicate in experiment_replicates:
    if not replicate.endswith(".xlsx"):
        if not replicate.endswith(".png"):
            replicate_directory = home_exp_directory_str + "/" + replicate
            series_sample_list = os.listdir(replicate_directory)
            for series in series_sample_list:
                series_directory = replicate_directory + "/" + series
                file_list = os.listdir(series_directory)
                series_num = series_sample_list.index(series)+1
                for file in file_list:
                    if file.endswith(".h5"):
                        print(TAB)
                        print("=============================================================================================")
                        print("The file at following directory is being run:")
                        file_directory = series_directory + "/" + file
                        print(file_directory)
                        HDF5_Surface_Finder.the_surface_finder(file_directory)
                        HDF5_Cell_Reader.the_cell_reader(file_directory)
                        HDF5_CellMaxSurface_Finder.the_cellmaxsurface_finder(file_directory)



