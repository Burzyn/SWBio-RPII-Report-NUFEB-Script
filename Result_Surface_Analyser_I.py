import os


def all_cells_plotter(all_cells_datafile,file_path):

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

    # PLOTTER ========================================================================================================

    # filename = filedialog.askopenfilename()

    filename = all_cells_datafile
    data = pd.read_excel(filename)
    barplot_color = "skyblue"

    if surface_cell_output_str in filename:
        preset_str = "cellmax_"
        barplot_color = "darkred"
    if Growth_str in filename:
        type_preset_str = "Growth_"
        label_preset_str = "Growth"
    if Yield_str in filename:
        type_preset_str = "Yield_"
        label_preset_str = "Yield"
    if Substrate_str in filename:
        type_preset_str = "Substrate_"
        label_preset_str = "Substrate"

    os.makedirs(f"{file_path}/{preset_str}Stats")


    data.rename(columns={"N.C": "NC"}, inplace=True)
    data.rename(columns={"N.E": "NE"}, inplace=True)
    data.rename(columns={"N.P": "NP"}, inplace=True)

    fig, axs = plt.subplots(2, 4, figsize=(22, 6), gridspec_kw={'height_ratios': [5, 1]})
    sns.barplot(data = data, x = "Sample_Num", y = "NC", alpha=0.4, color=barplot_color, ax=axs[0, 0], capsize=0.15, err_kws={'linewidth': 1.5})
    plt.tight_layout(pad=1.6)
    axs[0, 0].set_xlabel(f"{label_preset_str} Factor")
    axs[0, 0].set_ylabel("Number of cells")
    formula = "NC~Sample_Num"
    anova_model = ols(formula, data = data).fit()
    anova_output = sm.stats.anova_lm(anova_model, typ=2)
    anova_output_df = anova_output.reset_index()
    anova_output_df.to_excel(f"{file_path}/{preset_str}Stats/stats_{formula}.xlsx")
    text = f"ANOVA F-Statistic: {anova_output_df["F"][0]:.2f} \n ANOVA p-value: {anova_output_df["PR(>F)"][0]:.4f}"
    axs[1, 0].text(0.5, 0.5, text, fontsize=12, ha='center', va='center')
    # square = patches.Rectangle((0, 0), 2, 2, color='white', alpha=1, zorder=100)
    # axs[1, 0].add_patch(square)
    # plt.figure(facecolor="white", axs=axs[1, 0])
    # axs[1, 0].set_color("white")


    sns.barplot(data = data, x = "Sample_Num", y = "NE", alpha=0.4, color=barplot_color, ax=axs[0, 1], capsize=0.15, err_kws={'linewidth': 1.5})
    plt.tight_layout(pad=1.6)
    axs[0, 1].set_xlabel(f"{label_preset_str} Factor")
    axs[0, 1].set_ylabel("Number of EPS particles")
    formula = "NE~Sample_Num"
    anova_model = ols(formula, data = data).fit()
    anova_output = sm.stats.anova_lm(anova_model, typ=2)
    anova_output_df = anova_output.reset_index()
    anova_output_df.to_excel(f"{file_path}/{preset_str}Stats/stats_{formula}.xlsx")
    text = f"ANOVA F-Statistic: {anova_output_df["F"][0]:.2f} \n ANOVA p-value: {anova_output_df["PR(>F)"][0]:.4f}"
    axs[1, 1].text(0.5, 0.5, text, fontsize=12, ha='center', va='center')

    sns.barplot(data = data, x = "Sample_Num", y = "Av_Height", alpha=0.4, color=barplot_color, ax=axs[0, 2], capsize=0.15, err_kws={'linewidth': 1.5})
    plt.tight_layout(pad=1.6)
    axs[0, 2].set_xlabel(f"{label_preset_str} Factor")
    axs[0, 2].set_ylabel("Average Biofilm Height [m]")
    formula = "Av_Height~Sample_Num"
    anova_model = ols(formula, data = data).fit()
    anova_output = sm.stats.anova_lm(anova_model, typ=2)
    anova_output_df = anova_output.reset_index()
    anova_output_df.to_excel(f"{file_path}/{preset_str}Stats/stats_{formula}.xlsx")
    text = f"ANOVA F-Statistic: {anova_output_df["F"][0]:.2f} \n ANOVA p-value: {anova_output_df["PR(>F)"][0]:.4f}"
    axs[1, 2].text(0.5, 0.5, text, fontsize=12, ha='center', va='center')

    sns.barplot(data = data, x = "Sample_Num", y = "SD_Height", alpha=0.4, color=barplot_color, ax=axs[0, 3], capsize=0.15, err_kws={'linewidth': 1.5})
    plt.tight_layout(pad=1.6)
    axs[0, 3].set_xlabel(f"{label_preset_str} Factor")
    axs[0, 3].set_ylabel("SD of Point Biofilm Height [m]")
    formula = "SD_Height~Sample_Num"
    anova_model = ols(formula, data = data).fit()
    anova_output = sm.stats.anova_lm(anova_model, typ=2)
    anova_output_df = anova_output.reset_index()
    anova_output_df.to_excel(f"{file_path}/{preset_str}Stats/stats_{formula}.xlsx")
    text = f"ANOVA F-Statistic: {anova_output_df["F"][0]:.2f} \n ANOVA p-value: {anova_output_df["PR(>F)"][0]:.4f}"
    axs[1, 3].text(0.5, 0.5, text, fontsize=12, ha='center', va='center')
    GLMmodel = sm.GLM(data["SD_Height"], data["Sample_Num"], family=sm.families.Binomial())
    GLMresult = GLMmodel.fit()
    GLMresult_summary = GLMresult.summary()
    GLMresult_summary_df = pd.DataFrame(GLMresult_summary.tables[1])
    GLMresult_summary_df.to_excel(f"{file_path}/{preset_str}Stats/stats_GLM_{formula}.xlsx")

    plt.savefig(f"{file_path}/{preset_str}Surface_Graphs_1")
    # plt.show()

    fig, axs = plt.subplots(2, 4, figsize=(22, 6), gridspec_kw={'height_ratios': [5, 1]})
    sns.barplot(data = data, x = "Sample_Num", y = "Est_ADAM", alpha=0.4, color=barplot_color, ax=axs[0, 0], capsize=0.15, err_kws={'linewidth': 1.5})
    plt.tight_layout(pad=1.6)
    axs[0, 0].set_xlabel(f"{label_preset_str} Factor")
    axs[0, 0].set_ylabel("""Estimated Arithmetic Difference
    of Mean Height [m]""")
    sns.regplot(x="Sample_Num", y="Est_ADAM", data=data, scatter=False, ax=axs[0, 0], line_kws={"color": "black", "alpha": 0.6})
    # axs[0, 0].set_yscale("log")
    formula = "Est_ADAM~Sample_Num"
    anova_model = ols(formula, data = data).fit()
    anova_output = sm.stats.anova_lm(anova_model, typ=2)
    anova_output_df = anova_output.reset_index()
    anova_output_df.to_excel(f"{file_path}/{preset_str}Stats/stats_{formula}.xlsx")
    text = f"ANOVA F-Statistic: {anova_output_df["F"][0]:.2f} \n ANOVA p-value: {anova_output_df["PR(>F)"][0]:.4f}"
    axs[1, 0].text(0.5, 0.5, text, fontsize=12, ha='center', va='center')

    sns.barplot(data = data, x = "Sample_Num", y = "Surface_Area", alpha=0.4, color=barplot_color, ax=axs[0, 1], capsize=0.15, err_kws={'linewidth': 1.5})
    plt.tight_layout(pad=1.6)
    axs[0, 1].set_xlabel(f"{label_preset_str} Factor")
    axs[0, 1].set_ylabel("Biofilm Surface Area [m^2]")
    formula = "Surface_Area~Sample_Num"
    anova_model = ols(formula, data = data).fit()
    anova_output = sm.stats.anova_lm(anova_model, typ=2)
    anova_output_df = anova_output.reset_index()
    anova_output_df.to_excel(f"{file_path}/{preset_str}Stats/stats_{formula}.xlsx")
    text = f"ANOVA F-Statistic: {anova_output_df["F"][0]:.2f} \n ANOVA p-value: {anova_output_df["PR(>F)"][0]:.4f}"
    axs[1, 1].text(0.5, 0.5, text, fontsize=12, ha='center', va='center')
    GLMmodel = sm.GLM(data["Surface_Area"], data["Sample_Num"], family=sm.families.Binomial())
    GLMresult = GLMmodel.fit()
    GLMresult_summary = GLMresult.summary()
    print(GLMresult_summary)
    GLMresult_summary_df = pd.DataFrame(GLMresult_summary.tables[1])
    GLMresult_summary_df.to_excel(f"{file_path}/{preset_str}Stats/stats_GLM_{formula}.xlsx")


    sns.barplot(data = data, x = "Sample_Num", y = "SFA_alt", alpha=0.4, color=barplot_color, ax=axs[0, 2], capsize=0.15, err_kws={'linewidth': 1.5})
    plt.tight_layout(pad=1.6)
    axs[0, 2].set_xlabel(f"{label_preset_str} Factor")
    axs[0, 2].set_ylabel("Adjusted Surface Smoothness Factor")
    formula = "SFA_alt~Sample_Num"
    anova_model = ols(formula, data = data).fit()
    anova_output = sm.stats.anova_lm(anova_model, typ=2)
    anova_output_df = anova_output.reset_index()
    anova_output_df.to_excel(f"{file_path}/{preset_str}Stats/stats_{formula}.xlsx")
    text = f"ANOVA F-Statistic: {anova_output_df["F"][0]:.2f} \n ANOVA p-value: {anova_output_df["PR(>F)"][0]:.4f}"
    axs[1, 2].text(0.5, 0.5, text, fontsize=12, ha='center', va='center')
    GLMmodel = sm.GLM(data["SFA_alt"], data["Sample_Num"], family=sm.families.Binomial())
    GLMresult = GLMmodel.fit()
    GLMresult_summary = GLMresult.summary()
    GLMresult_summary_df = pd.DataFrame(GLMresult_summary.tables[1])
    GLMresult_summary_df.to_excel(f"{file_path}/{preset_str}Stats/stats_GLM_{formula}.xlsx")


    sns.barplot(data = data, x = "Sample_Num", y = "SFA", alpha=0.4, color=barplot_color, ax=axs[0, 3], capsize=0.15, err_kws={'linewidth': 1.5})
    plt.tight_layout(pad=1.6)
    axs[0, 3].set_xlabel(f"{label_preset_str} Factor")
    axs[0, 3].set_ylabel("Surface Smoothness Factor")
    formula = "SFA~Sample_Num"
    anova_model = ols(formula, data = data).fit()
    anova_output = sm.stats.anova_lm(anova_model, typ=2)
    anova_output_df = anova_output.reset_index()
    anova_output_df.to_excel(f"{file_path}/{preset_str}Stats/stats_{formula}.xlsx")
    text = f"ANOVA F-Statistic: {anova_output_df["F"][0]:.2f} \n ANOVA p-value: {anova_output_df["PR(>F)"][0]:.4f}"
    axs[1, 3].text(0.5, 0.5, text, fontsize=12, ha='center', va='center')
    GLMmodel = sm.GLM(data["SFA"], data["Sample_Num"], family=sm.families.Binomial())
    GLMresult = GLMmodel.fit()
    GLMresult_summary = GLMresult.summary()
    GLMresult_summary_df = pd.DataFrame(GLMresult_summary.tables[1])
    GLMresult_summary_df.to_excel(f"{file_path}/{preset_str}Stats/stats_GLM_{formula}.xlsx")

    plt.savefig(f"{file_path}/{preset_str}Surface_Graphs_2")
    # plt.show()

