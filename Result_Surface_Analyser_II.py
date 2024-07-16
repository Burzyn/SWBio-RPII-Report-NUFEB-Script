import os


def surface_plotter_II(all_cells_datafile,file_path):

    # BANK ===========================================================================================================

    import h5py
    import pandas as pd
    import math
    from tkinter import filedialog
    import matplotlib.pyplot as plt
    import seaborn as sns
    import scipy.stats as stats
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    import matplotlib.patches as patches
    TAB = """
        """
    preset_str = ""
    type_preset_str = ""
    label_preset_str = ""
    surface_cell_output_str = "Experiment_cellmax_surface"
    Growth_str = "Growth"
    Yield_str = "Yield"
    Substrate_str = "Substrate"

    # INITIATOR ======================================================================================================

    # filename = filedialog.askopenfilename()

    filename = all_cells_datafile
    data = pd.read_excel(filename)
    corplot_color = "steelblue"
    do_cell_and_eps_cors = 1

    if surface_cell_output_str in filename:
        preset_str = "cellmax_"
        corplot_color = "darkred"
        do_cell_and_eps_cors = 0
    if Growth_str in filename:
        type_preset_str = "Growth_"
        label_preset_str = "Growth"
    if Yield_str in filename:
        type_preset_str = "Yield_"
        label_preset_str = "Yield"
    if Substrate_str in filename:
        type_preset_str = "Substrate_"
        label_preset_str = "Substrate"

    data.rename(columns={"N.C": "NC"}, inplace=True)
    data.rename(columns={"N.E": "NE"}, inplace=True)
    data.rename(columns={"N.P": "NP"}, inplace=True)
    data_file_samples = data["Sample_Num"].unique()

    num_columns = 4
    num_rows = 4
    fig, axs = plt.subplots(1, 1 * num_columns, figsize=(6*num_columns, 6 ))

    # CORRELATION PLOTTER ============================================================================================

    corr_value = data["SFA"].corr(data["SFA_alt"])
    sns.regplot(data=data, x="SFA", y="SFA_alt", ci=None, scatter_kws={"color": corplot_color},
               line_kws={"color": corplot_color, "alpha": 0.4}, ax=axs[0])
    plt.tight_layout(pad=4)
    axs[0].set_xlabel("Surface Smoothness Factor", fontsize=14)
    axs[0].set_ylabel("Adjusted Surface Smoothness Factor", fontsize=14)
    axs[0].set_title(f"Correlation Plot (r={corr_value})", x=0.5, y=1.05)


    corr_value = data["SD_Height"].corr(data["Av_Height"])
    sns.regplot(data=data, x="SD_Height", y="Av_Height", ci=None, scatter_kws={"color": corplot_color},
               line_kws={"color": corplot_color, "alpha": 0.4}, ax=axs[1])
    plt.tight_layout(pad=4)
    axs[1].set_xlabel("SD of Point Biofilm Height [m]", fontsize=14)
    axs[1].set_ylabel("Average Biofilm Height [m]", fontsize=14)
    axs[1].set_title(f"Correlation Plot (r={corr_value})", x=0.5, y=1.05)


    corr_value = data["SD_Height"].corr(data["SFA"])
    sns.regplot(data=data, x="SD_Height", y="SFA", ci=None, scatter_kws={"color": corplot_color},
               line_kws={"color": corplot_color, "alpha": 0.4}, ax=axs[2])
    plt.tight_layout(pad=4)
    axs[2].set_xlabel("SD of Point Biofilm Height [m]", fontsize=14)
    axs[2].set_ylabel("Surface Smoothness Factor", fontsize=14)
    axs[2].set_title(f"Correlation Plot (r={corr_value})", x=0.5, y=1.05)


    corr_value = data["SD_Height"].corr(data["Surface_Area"])
    sns.regplot(data=data, x="SD_Height", y="Surface_Area", ci=None, scatter_kws={"color": corplot_color},
               line_kws={"color": corplot_color, "alpha": 0.4}, ax=axs[3])
    plt.tight_layout(pad=4)
    axs[3].set_xlabel("SD of Point Biofilm Height [m]", fontsize=14)
    axs[3].set_ylabel("Biofilm Surface Area [m^2]", fontsize=14)
    axs[3].set_title(f"Correlation Plot (r={corr_value})", x=0.5, y=1.05)

    plt.savefig(f"{file_path}/{preset_str}{type_preset_str}Cor_Graph_Joined")


