
def the_surface_finder(input_path):

    # BANK ===============================================================================================================

    import h5py
    import pandas as pd
    import math
    TAB = """
    """
    num_divide = 25
    cutoff_Z = 0.000099
    print("Proces initiated")
    result = "No"

    # FILE IMPORTER ======================================================================================================

    print(TAB)
    filename = input_path
    dir = str(filename)
    coordinates = pd.DataFrame(columns=["cell", "x", "y", "z", "length_numberY", "depth_numberZ"])
    file = h5py.File(filename, "r")
    listofkeys = []

    for key in file:
        listofkeys.append(key)
        if key == "x":
            indexX = listofkeys.index(key)
        elif key == "y":
            indexY = listofkeys.index(key)
        elif key == "z":
            indexZ = listofkeys.index(key)

    # TIME-POINT FINDER ==================================================================================================

    dataframe_max_Z = pd.DataFrame(columns=["Timepoint", "Max_Z", "All_Cells"])
    all_timepoints_list = []

    with h5py.File(filename, "r") as file:
        x_positions = list(file["z"])
        for timepoint in x_positions:
            x_positions = list(file["z"][timepoint][:])
            particle_type = list(file["type"][timepoint][:])
            all_p = len(x_positions)
            max_Z = max(x_positions)
            timepoint_int = int(timepoint)
            all_timepoints_list.append(timepoint_int)
            new_row = pd.DataFrame({"Timepoint": [timepoint_int], "Max_Z": [max_Z], "All_Cells": [all_p]})
            dataframe_max_Z = pd.concat([dataframe_max_Z, new_row], ignore_index=True)

    all_timepoints_list.sort()
    last_timepoint = all_timepoints_list[-1]
    table_sorted_Z = dataframe_max_Z.sort_values(by=["Timepoint"], ascending=True)
    iterator = 1
    while True:
        if iterator > 0:
            for index, row in table_sorted_Z.iterrows():
                if row["Max_Z"] > cutoff_Z:
                    last_timepoint = row["Timepoint"] - 10
                    iterator = 0
                    result = "Yes"
                    break
                if row["Timepoint"] == last_timepoint:
                    iterator = 0
                    break
        else:
            break

    last_timepoint_str = str(last_timepoint)

    # END EPS & CELL NUMERATOR ===========================================================================================

    with h5py.File(filename, "r") as f:
        a_group_key = list(f.keys())[indexX]
        timepoints = list(f[a_group_key])
        for item in timepoints:
            if item == last_timepoint_str:
                x_positions = list(f["x"][timepoint][:])
                particle_type = list(f["type"][timepoint][:])
                all_particles = len(x_positions)
                num_cells = particle_type.count(1)
                num_EPS = particle_type.count(2)

    # X LOCATOR ==========================================================================================================

    with h5py.File(filename, "r") as f:
        a_group_key = list(f.keys())[indexX]
        timepoints = list(f[a_group_key])
        for item in timepoints:
            if item == last_timepoint_str:
                group = f["x"]
                dataset1 = group[item]
                cellnum = 0
                # print("X coords initiated")
                for cell in dataset1:
                    coordinates.loc[cellnum, "cell"] = cellnum
                    coordinates.loc[cellnum, "x"] = cell
                    cellnum = cellnum + 1

    # Y LOCATOR ==========================================================================================================

    with h5py.File(filename, "r") as f:
        a_group_key = list(f.keys())[indexY]
        timepoints = list(f[a_group_key])
        for item in timepoints:
            if item == last_timepoint_str:
                group = f["y"]
                dataset1 = group[item]
                cellnum = 0
                # print("Y coords initiated")
                for cell in dataset1:
                    coordinates.loc[cellnum, "y"] = cell
                    cellnum = cellnum + 1

    # Z LOCATOR ==========================================================================================================

    with h5py.File(filename, "r") as f:
        a_group_key = list(f.keys())[indexZ]
        timepoints = list(f[a_group_key])
        for item in timepoints:
            if item == last_timepoint_str:
                group = f["z"]
                dataset1 = group[item]
                cellnum = 0
                # print("Z coords initiated")
                for cell in dataset1:
                    coordinates.loc[cellnum, "z"] = cell
                    cellnum = cellnum + 1

    # SEPARATOR ==========================================================================================================

    Xlist = coordinates['x'].tolist()
    Ylist = coordinates['y'].tolist()
    Zlist = coordinates['z'].tolist()

    x_max = 0
    x_min = 100
    for eachX in Xlist:
        if eachX >= x_max:
            x_max = eachX
    for eachX in Xlist:
        if eachX <= x_min:
            x_min = eachX
    x_range = x_max - x_min

    y_max = 0
    y_min = 100
    for eachY in Ylist:
        if eachY >= y_max:
            y_max = eachY
    for eachY in Ylist:
        if eachY <= y_min:
            y_min = eachY
    y_range = y_max - y_min

    z_max = 0
    z_min = 100
    for eachZ in Zlist:
        if eachZ >= z_max:
            z_max = eachZ
    for eachZ in Zlist:
        if eachZ <= z_min:
            z_min = eachZ
    z_range = z_max - z_min

    x_thresholds = []
    y_thresholds = []
    z_thresholds = []

    x_step = x_range / num_divide
    y_step = y_range / num_divide
    z_step = z_range / num_divide

    runnum = 1
    for step in range(num_divide):
        thresholdX = x_step * runnum
        x_thresholds.append(thresholdX)
        thresholdY = y_step * runnum
        y_thresholds.append(thresholdY)
        thresholdZ = z_step * runnum
        z_thresholds.append(thresholdZ)
        runnum = runnum + 1

    for index, row in coordinates.iterrows():
        temp_dataframe = pd.DataFrame(row).T
        y_temp_list = temp_dataframe["x"].tolist()
        y_temp_val = y_temp_list[0]
        z_temp_list = temp_dataframe["y"].tolist()
        z_temp_val = z_temp_list[0]
        foundY = 0
        foundZ = 0
        for element in x_thresholds:
            if foundY == 0:
                if y_temp_val <= element:
                    index_thr = x_thresholds.index(element) + 1
                    coordinates.loc[index, "length_numberY"] = index_thr
                    foundY = 1
        for element in y_thresholds:
            if foundZ == 0:
                if z_temp_val <= element:
                    index_thr = y_thresholds.index(element) + 1
                    coordinates.loc[index, "depth_numberZ"] = index_thr
                    foundZ = 1

    # COORDINATOR ========================================================================================================

    dirref = dir.replace("dump.h5", "")
    dirref_nospaces = dirref[:-1]
    list_directory = dirref_nospaces.split("/")
    folder_name = list_directory[-1]
    savedir = f"{dirref}Coordinates_{folder_name}_csv"
    coordinates.to_csv(savedir, index=False)

    # SURFER =============================================================================================================

    surface_df = pd.DataFrame(columns=["z", "length_numberY", "depth_numberZ"])
    data = pd.DataFrame(coordinates)
    for num1 in range(1, num_divide + 1):
        filter_row1 = data[data["length_numberY"] == num1]
        for num2 in range(1, num_divide + 1):
            filter_row2 = filter_row1[filter_row1["depth_numberZ"] == num2]
            try:
                maxX = filter_row2["z"].max()
                dnY_transform = filter_row2["length_numberY"].max()
                dnZ_transform = filter_row2["depth_numberZ"].max()
                if not maxX > 0:
                    maxX = 0
            except:
                print("Fail")
            else:
                dnY_transform = num1
                dnZ_transform = num2
            new_row = [maxX, dnY_transform, dnZ_transform]
            surface_df.loc[len(surface_df)] = new_row

    # MATRIX SMOOTHER ====================================================================================================

    for index, row in surface_df.iterrows():
        if row["z"] == 0:
            if row["length_numberY"] > 1:
                if row["length_numberY"] < 25:
                    if row["depth_numberZ"] > 1:
                        if row["depth_numberZ"] < 25:
                            current_Y = row["length_numberY"]
                            current_X = row["depth_numberZ"]
                            # ========== #
                            cell_above_frame = surface_df[(surface_df["length_numberY"] == current_Y + 1) & (
                                        surface_df["depth_numberZ"] == current_X)]["z"]
                            list_singleval_a = list(cell_above_frame)
                            cell_above = list_singleval_a[0]
                            # ========== #
                            cell_right_frame = surface_df[(surface_df["length_numberY"] == current_Y) & (
                                        surface_df["depth_numberZ"] == current_X + 1)]["z"]
                            list_singleval_r = list(cell_right_frame)
                            cell_right = list_singleval_r[0]
                            # ========== #
                            cell_below_frame = surface_df[(surface_df["length_numberY"] == current_Y - 1) & (
                                        surface_df["depth_numberZ"] == current_X)]["z"]
                            list_singleval_b = list(cell_below_frame)
                            cell_below = list_singleval_b[0]
                            # ========== #
                            cell_left_frame = surface_df[(surface_df["length_numberY"] == current_Y) & (
                                        surface_df["depth_numberZ"] == current_X - 1)]["z"]
                            list_singleval_l = list(cell_left_frame)
                            cell_left = list_singleval_l[0]
                            if cell_above != 0:
                                if cell_below != 0:
                                    if cell_right != 0:
                                        if cell_left != 0:
                                            cell_av = (cell_above + cell_right + cell_below + cell_left) / 4
                                            surface_df.iloc[index, 0] = cell_av

    # EXPORTER I =========================================================================================================

    # print("Surface matrix found")
    surface_matrix = surface_df.pivot(index="length_numberY", columns="depth_numberZ", values="z")
    dirref = dir.replace("dump.h5", "")
    savedir = f"{dirref}SurfaceMatrix_{folder_name}"
    savedir_xcl = f"{savedir}_xlsx.xlsx"
    surface_matrix.to_csv(f"{savedir}_csv", index=False, header=False)
    surface_matrix.to_excel(savedir_xcl, sheet_name="A", index=False)

    # ASSEMBLER ==========================================================================================================

    total_matrix_area = 0
    num_triangles = 0
    line_a = x_step
    line_b = y_step
    line_c = math.sqrt(line_a ** 2 + line_b ** 2)

    for index, row in surface_df.iterrows():
        if row["depth_numberZ"] != num_divide and row["length_numberY"] != num_divide:
            temporary_x = row["depth_numberZ"]
            temporary_y = row["length_numberY"]
            h_point = row["z"]
            shift_x = temporary_x + 1
            shift_y = temporary_y + 1
            # print(h_point)
            for index2, row2 in surface_df.iterrows():
                if row2["depth_numberZ"] == temporary_x and row2["length_numberY"] == shift_y:
                    h_point_x = row2["z"]
            for index3, row3 in surface_df.iterrows():
                if row3["depth_numberZ"] == shift_x and row3["length_numberY"] == temporary_y:
                    h_point_y = row3["z"]
            for index4, row4 in surface_df.iterrows():
                if row4["depth_numberZ"] == shift_x and row4["length_numberY"] == shift_y:
                    h_point_yx = row4["z"]

            h1 = abs(h_point - h_point_x)
            h2 = abs(h_point - h_point_y)
            val_x = math.sqrt(line_a ** 2 + h1 ** 2)
            val_y = math.sqrt(line_b ** 2 + h2 ** 2)
            val_z_tempt = abs(h_point_x - h_point_y)
            val_z = math.sqrt(val_z_tempt ** 2 + line_c ** 2)
            TriangleA_half_circumference = (val_x + val_y + val_z) / 2
            TCA = TriangleA_half_circumference
            F_TriangleA = math.sqrt(TCA * (TCA - val_x) * (TCA - val_y) * (TCA - val_z))

            h3x = abs(h_point_x - h_point_yx)
            h3y = abs(h_point_y - h_point_yx)
            val_x2 = math.sqrt(line_a ** 2 + h3x ** 2)
            val_y2 = math.sqrt(line_b ** 2 + h3y ** 2)
            val_z2 = val_z
            TriangleB_half_circumference = (val_x2 + val_y2 + val_z2) / 2
            TCB = TriangleB_half_circumference
            F_TriangleB = math.sqrt(TCB * (TCB - val_x2) * (TCB - val_y2) * (TCB - val_z2))
            sq_area = F_TriangleA + F_TriangleB
            total_matrix_area = total_matrix_area + sq_area
            num_triangles = num_triangles + 1

    total_perfect_smooth_matrix_area = ((num_divide - 1) * x_step) * ((num_divide - 1) * y_step)
    TPSMA = total_perfect_smooth_matrix_area
    surface_SD = surface_df["z"].std()
    av_biofilm_h = surface_df["z"].mean()

    estimated_arithmetic_difference_of_a_mean = 0
    summ_for_SFA = 0
    Nufeb_surface_factor_sum = 0
    EADM = estimated_arithmetic_difference_of_a_mean
    for index, row in surface_df.iterrows():
        temp_height_av = row["z"]
        difference = abs(temp_height_av - av_biofilm_h)
        val_for_SFA = difference/av_biofilm_h
        EADM = EADM + difference
        summ_for_SFA = summ_for_SFA + val_for_SFA
        diff_sq =  difference*difference
        Nufeb_surface_factor =  math.sqrt(diff_sq*(total_matrix_area/(num_divide^2)))
        Nufeb_surface_factor_sum = Nufeb_surface_factor_sum + Nufeb_surface_factor

    SFU = (total_matrix_area/TPSMA)*EADM
    SFA = (total_matrix_area/TPSMA)*(summ_for_SFA/(num_divide^2))
    SFA_alt = (total_matrix_area/TPSMA)*((summ_for_SFA^2)/(num_divide^2))
    NUFEB_surface = (Nufeb_surface_factor_sum/TPSMA)

    output_table = pd.DataFrame(columns=["Measurement", "Value"])
    new_row1 = pd.DataFrame({"Measurement": ["Number mesh triangles"], "Value": [num_triangles - 1]})
    new_row2 = pd.DataFrame({"Measurement": ["Total surface area"], "Value": [total_matrix_area]})
    new_row3 = pd.DataFrame({"Measurement": ["Total perfect smooth area"], "Value": [TPSMA]})
    new_row4 = pd.DataFrame({"Measurement": ["SD of the point biofilm height"], "Value": [surface_SD]})
    new_row5 = pd.DataFrame({"Measurement": ["Average biofilm height"], "Value": [av_biofilm_h]})
    new_row6 = pd.DataFrame({"Measurement": ["Estimated arithmetic difference of a mean"], "Value": [EADM]})
    new_row7 = pd.DataFrame({"Measurement": ["Last timepoint"], "Value": [last_timepoint]})
    new_row8 = pd.DataFrame({"Measurement": ["Overgrowth"], "Value": [result]})
    new_row9 = pd.DataFrame({"Measurement": ["Unadjusted Surface Factor*"], "Value": [SFU]})
    new_row10 = pd.DataFrame({"Measurement": ["Adjusted Surface Factor*"], "Value": [SFA]})
    new_row11 = pd.DataFrame({"Measurement": ["Number of Particles"], "Value": [all_particles]})
    new_row12 = pd.DataFrame({"Measurement": ["Number of EPSs"], "Value": [num_EPS]})
    new_row13 = pd.DataFrame({"Measurement": ["Number of cells"], "Value": [num_cells]})
    new_row14 = pd.DataFrame({"Measurement": ["SFA_alt"], "Value": [SFA_alt]})
    new_row15 = pd.DataFrame({"Measurement": ["NUFEB_surface"], "Value": [NUFEB_surface]})
    output_table = pd.concat([output_table, new_row1], ignore_index=True)
    output_table = pd.concat([output_table, new_row2], ignore_index=True)
    output_table = pd.concat([output_table, new_row3], ignore_index=True)
    output_table = pd.concat([output_table, new_row4], ignore_index=True)
    output_table = pd.concat([output_table, new_row5], ignore_index=True)
    output_table = pd.concat([output_table, new_row6], ignore_index=True)
    output_table = pd.concat([output_table, new_row7], ignore_index=True)
    output_table = pd.concat([output_table, new_row8], ignore_index=True)
    output_table = pd.concat([output_table, new_row9], ignore_index=True)
    output_table = pd.concat([output_table, new_row10], ignore_index=True)
    output_table = pd.concat([output_table, new_row11], ignore_index=True)
    output_table = pd.concat([output_table, new_row12], ignore_index=True)
    output_table = pd.concat([output_table, new_row13], ignore_index=True)
    output_table = pd.concat([output_table, new_row14], ignore_index=True)
    output_table = pd.concat([output_table, new_row15], ignore_index=True)

    savedir2 = f"{dirref}SurfaceOutput_{folder_name}"
    savedir_xcl2 = f"{savedir2}_xlsx.xlsx"
    output_table.to_excel(savedir_xcl2, sheet_name="A", index=False)

    print("Proces finished")

