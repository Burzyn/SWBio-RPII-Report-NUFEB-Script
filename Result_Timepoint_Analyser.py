

def all_timepoint_plotter(all_cells_datafile,file_path):

    # BANK ===========================================================================================================

    import h5py
    import pandas as pd
    import math
    from tkinter import filedialog
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    TAB = """
        """
    preset_str = ""
    type_preset_str = ""
    label_preset_str = ""
    surface_cell_output_str = "Experiment_cellmax_surface"
    Growth_str = "Growth"
    Yield_str = "Yield"
    Substrate_str = "Substrate"
    color_palette = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f"]
    Growth_dictionary = {"0.00008": 1, "0.00028": 2,"0.00048": 3,"0.00068": 4,"0.00088": 5,"0.00108": 6,"0.00128": 7,"0.00148": 8}
    Yield_dictionary = {"0.41": 1, "0.46": 2,"0.51": 3,"0.56": 4,"0.61": 5,"0.66": 6,"0.71": 7,"0.76": 8}
    Substrate_dictionary = {"0.000005": 1, "0.000015": 2,"0.000025": 3,"0.000035": 4,"0.000045": 5,"0.000055": 6,"0.000065": 7,"0.000075": 8}

    # PLOTTER ========================================================================================================

    # filename = filedialog.askopenfilename()

    filename = all_cells_datafile
    data = pd.read_excel(filename)
    data_file_samples = data["Sample_Num"].unique()
    data_file_timepoints = data["Timepoint"].unique()

    if Growth_str in filename:
        type_preset_str = "Growth_"
        label_preset_str = "Growth"
        label_dictionary = Growth_dictionary
    if Yield_str in filename:
        type_preset_str = "Yield_"
        label_preset_str = "Yield"
        label_dictionary = Yield_dictionary
    if Substrate_str in filename:
        type_preset_str = "Substrate_"
        label_preset_str = "Substrate"
        label_dictionary = Substrate_dictionary

    print(data)

    new_data= pd.DataFrame(columns=["Timepoint", "Cells", "EPS", "All_Particles", "Sample_Num", "Replicate_Num"])

    for index, row in data.iterrows():
        EPS_num = row["EPS"]
        Cell_num = row["Cells"]
        Particle_num = EPS_num + Cell_num
        for key, value in label_dictionary.items():
            if value == row["Sample_Num"]:
                sample_name = key
        new_row = [row["Timepoint"], Cell_num, EPS_num, Particle_num, sample_name, row["Replicate_Num"]]
        new_data.loc[len(new_data)] = new_row

    print(new_data)
    new_data = new_data.sort_values(by=["Replicate_Num", "Sample_Num", "Timepoint"])
    print(new_data)

    plt.figure(figsize=(10, 6))
    sns.lineplot(x="Timepoint", y="Cells", data=new_data, hue="Sample_Num", errorbar="sd", alpha = 1.0, palette=color_palette)
    plt.minorticks_on()
    plt.xlabel(f"Timepoint")
    plt.xticks(np.linspace(data_file_timepoints.min(), data_file_timepoints.max(), num=10))
    plt.ylabel("Number of cells")
    plt.title(f"{label_preset_str} factor timepoint graph for the numer of cells")
    plt.legend(title=f"{label_preset_str} Factor")
    plt.savefig(f"{file_path}/{type_preset_str}Timepoint_Cell_Graph")

    # plt.show()

    plt.figure(figsize=(10, 6))
    sns.lineplot(x="Timepoint", y="EPS", data=new_data, hue="Sample_Num", errorbar="sd", alpha = 1.0, palette=color_palette)
    plt.minorticks_on()
    plt.xlabel(f"Timepoint")
    plt.xticks(np.linspace(data_file_timepoints.min(), data_file_timepoints.max(), num=10))
    plt.ylabel("Number of EPS particles")
    plt.title(f"{label_preset_str} factor timepoint graph for the numer of EPS particles")
    plt.legend(title=f"{label_preset_str} Factor")
    plt.savefig(f"{file_path}/{type_preset_str}Timepoint_EPS_Graph")
    # plt.show()

    plt.figure(figsize=(10, 6))
    sns.lineplot(x="Timepoint", y="All_Particles", data=new_data, hue="Sample_Num", errorbar="sd", alpha = 1.0, palette=color_palette)
    plt.minorticks_on()
    plt.xlabel(f"Timepoint")
    plt.xticks(np.linspace(data_file_timepoints.min(), data_file_timepoints.max(), num=10))
    plt.ylabel("Number of all particles (cells + EPS)")
    plt.title(f"{label_preset_str} factor timepoint graph for the numer of all particles (cells + EPS)")
    plt.legend(title=f"{label_preset_str} Factor")
    plt.savefig(f"{file_path}/{type_preset_str}Timepoint_AllParticles_Graph")
    # plt.show()


