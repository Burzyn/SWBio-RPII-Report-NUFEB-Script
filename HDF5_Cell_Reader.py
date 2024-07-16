
def the_cell_reader(inputh_path_cells):

    # BANK ===============================================================================================================

    import h5py
    import pandas as pd
    from tkinter import filedialog
    dataframe = pd.DataFrame(columns=["Timepoint","Num_Cells", "Num_EPS", "Num_Particles"])

    # FILE IMPORTER ======================================================================================================

    # filename = filedialog.askopenfilename()
    filename = inputh_path_cells
    dir = str(filename)

    # CALCULATOR =========================================================================================================

    with h5py.File(filename, "r") as file:
        x_positions = list(file["x"])
        for timepoint in x_positions:
            x_positions = list(file["x"][timepoint][:])
            particle_type = list(file["type"][timepoint][:])
            all_p = len(x_positions)
            num_of_1s = particle_type.count(1)
            num_of_2s = particle_type.count(2)
            timepoint_int = int(timepoint)
            new_row = pd.DataFrame({"Timepoint":[timepoint_int],"Num_Cells":[num_of_1s], "Num_EPS":[num_of_2s], "Num_Particles":[all_p]})
            dataframe = pd.concat([dataframe, new_row], ignore_index=True)


    tablefinal = dataframe.sort_values(by=["Timepoint"], ascending=True)
    dirref = dir.replace("dump.h5", "")
    dirref_nospaces = dirref[:-1]
    list_directory = dirref_nospaces.split("/")
    folder_name = list_directory[-1]
    savedir = f"{dirref}TimepointNumbers_{folder_name}_csv.csv"
    tablefinal.to_csv(savedir, index=False)
