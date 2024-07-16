


def surface_plotter_III(all_cells_datafile,file_path):
    # BANK ===========================================================================================================

    import pandas as pd
    import math
    from tkinter import filedialog
    import matplotlib.pyplot as plt
    import seaborn as sns
    import scipy.stats as stats
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    import matplotlib.patches as patches
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
    All_factors_str = "All_Factors"

    # PLOTTER ========================================================================================================

    # filename = filedialog.askopenfilename()

    filename = all_cells_datafile
    data = pd.read_excel(filename)

    if surface_cell_output_str in filename:
        preset_str = "cellmax_"
    if Growth_str in filename:
        type_preset_str = "Growth_"
        label_preset_str = "Growth"
    if Yield_str in filename:
        type_preset_str = "Yield_"
        label_preset_str = "Yield"
    if Substrate_str in filename:
        type_preset_str = "Substrate_"
        label_preset_str = "Substrate"
    if All_factors_str in filename:
        type_preset_str = "All_Factors_"
        label_preset_str = "All_Factors"

    data.rename(columns={"N.C": "NC"}, inplace=True)
    data.rename(columns={"N.E": "NE"}, inplace=True)
    data.rename(columns={"N.P": "NP"}, inplace=True)

    columns_list = data.columns.tolist()

    num_columns = 0
    for column in columns_list:
        num_columns = num_columns + 1

    num_columns = num_columns - 3
    print(num_columns)

    fig, axs = plt.subplots(1 * num_columns, 1 * num_columns, figsize=(6 * num_columns, 6 * num_columns))

    column_X_step = 0
    column_Y_step = 0
    for column_X in columns_list:
        if column_X != "Sample_Num":
            if column_X != "Replicate_Num":
                if column_X != "Overgrowth":
                    for column_Y in columns_list:
                        if column_Y != "Sample_Num":
                            if column_Y != "Replicate_Num":
                                if column_Y != "Overgrowth":
                                    print(column_X)
                                    print(column_X_step)
                                    print(column_Y)
                                    print(column_Y_step)
                                    print(TAB)
                                    corr_value = data[column_X].corr(data[column_Y])
                                    sns.regplot(data=data, x=column_X, y=column_Y, ci=None, scatter_kws={"color": "darkslategray"},
                                                line_kws={"color": "darkslategray", "alpha": 0.4},
                                                ax=axs[column_X_step, column_Y_step])
                                    plt.tight_layout(pad=4)
                                    plt.xlabel(column_X)
                                    plt.ylabel(column_Y)
                                    plt.title(f"Correlation Plot (r={corr_value})", x=0.5, y=1.05, ax=axs[column_X_step, column_Y_step])
                                    column_Y_step = column_Y_step + 1
                    column_Y_step = 0
                    column_X_step = column_X_step + 1

    plt.savefig(f"{file_path}/{preset_str}{type_preset_str}Cor_Graph_All")
