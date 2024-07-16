
# BANK ===============================================================================================================

import random
import shutil
from tkinter import filedialog
import pandas as pd
import os
df_columns = ["Replicate","Sample","Seed", "Values"]
seed_df = pd.DataFrame(columns=df_columns)
replciate_list = []
sample_list = []
rep_step = 1
sam_step = 1
seed = 0
### Varying Arguments ###
Experiments_str = "Cell & EPS"
replicates_num = 10
samples_num = 8


# INITIATOR =========================================================================================================

home_exp_directory = filedialog.askdirectory()
new_folders_directory = home_exp_directory
raw_file_script = f"{home_exp_directory}/inputscript.nufeb"

while True:
    if rep_step < replicates_num:
        replciate_list.append(rep_step)
        rep_step = rep_step + 1
    else:
        replciate_list.append(rep_step)
        break

while True:
    if sam_step < samples_num:
        sample_list.append(sam_step)
        sam_step = sam_step + 1
    else:
        sample_list.append(sam_step)
        break

# GROWTH SAMPLE MAKER ================================================================================================

random_numbers_list = []
new_Gexp_folder =  f"{new_folders_directory}/Growth"
os.makedirs(new_Gexp_folder, exist_ok=True)
for rep in replciate_list:
    new_Rep_folder = f"{new_Gexp_folder}/G_R{rep}"
    os.makedirs(new_Rep_folder, exist_ok=True)
    for sample in sample_list:
        new_sam_folder = f"{new_Rep_folder}/G_R{rep}_S{sample}"
        os.makedirs(new_sam_folder, exist_ok=True)

        random_number = random.randint(1000, 9999)
        while True:
            if random_number in random_numbers_list:
                random_number = random.randint(1000, 9999)
            if random_number not in random_numbers_list:
                random_numbers_list.append(random_number)
                break

        new_row = [rep, sample, random_number, Experiments_str]
        seed_df.loc[len(seed_df)] = new_row

        with open(raw_file_script, "rb") as nufeb_file:
            data = nufeb_file.read()

        text_data =  data.decode("utf-8")
        # print(text_data)

        update1_NUFEB = text_data.replace("nufeb/division/coccus 1.36e-6 1234",f"nufeb/division/coccus 1.36e-6 {random_number}")
        update2_NUFEB = update1_NUFEB.replace("nufeb/eps_secretion 2 EPS 1.3 30 2345",f"nufeb/eps_secretion 2 EPS 1.3 30 {random_number}")

        if sample == 1:
            updated_NUFEB = update2_NUFEB.replace("growth 0.00028 yield 0.61","growth 0.00008 yield 0.61")
        if sample == 2:
            updated_NUFEB = update2_NUFEB.replace("growth 0.00028 yield 0.61", "growth 0.00028 yield 0.61")
        if sample == 3:
            updated_NUFEB = update2_NUFEB.replace("growth 0.00028 yield 0.61", "growth 0.00048 yield 0.61")
        if sample == 4:
            updated_NUFEB = update2_NUFEB.replace("growth 0.00028 yield 0.61", "growth 0.00068 yield 0.61")
        if sample == 5:
            updated_NUFEB = update2_NUFEB.replace("growth 0.00028 yield 0.61", "growth 0.00088 yield 0.61")
        if sample == 6:
            updated_NUFEB = update2_NUFEB.replace("growth 0.00028 yield 0.61", "growth 0.00108 yield 0.61")
        if sample == 7:
            updated_NUFEB = update2_NUFEB.replace("growth 0.00028 yield 0.61", "growth 0.00128 yield 0.61")
        if sample == 8:
            updated_NUFEB = update2_NUFEB.replace("growth 0.00028 yield 0.61", "growth 0.00148 yield 0.61")

        with open(f"{new_sam_folder}/inputscript.nufeb", "w", encoding="utf-8") as file:
            file.write(updated_NUFEB)

        shutil.copy(f"{home_exp_directory}/atom.in", f"{new_sam_folder}/atom.in")

savedir_seed_file = f"{home_exp_directory}/Experiment_GrowthSeeds_xlsx.xlsx"
seed_df.to_excel(savedir_seed_file, sheet_name="A", index=False)

# YIELD SAMPLE MAKER ================================================================================================

random_numbers_list = []
new_Yexp_folder =  f"{new_folders_directory}/Yield"
os.makedirs(new_Yexp_folder, exist_ok=True)
for rep in replciate_list:
    new_Rep_folder = f"{new_Yexp_folder}/Y_R{rep}"
    os.makedirs(new_Rep_folder, exist_ok=True)
    for sample in sample_list:
        new_sam_folder = f"{new_Rep_folder}/Y_R{rep}_S{sample}"
        os.makedirs(new_sam_folder, exist_ok=True)

        random_number = random.randint(1000, 9999)
        while True:
            if random_number in random_numbers_list:
                random_number = random.randint(1000, 9999)
            if random_number not in random_numbers_list:
                random_numbers_list.append(random_number)
                break

        new_row = [rep, sample, random_number, Experiments_str]
        seed_df.loc[len(seed_df)] = new_row

        with open(raw_file_script, "rb") as nufeb_file:
            data = nufeb_file.read()

        text_data =  data.decode("utf-8")
        # print(text_data)

        update1_NUFEB = text_data.replace("nufeb/division/coccus 1.36e-6 1234",f"nufeb/division/coccus 1.36e-6 {random_number}")
        update2_NUFEB = update1_NUFEB.replace("nufeb/eps_secretion 2 EPS 1.3 30 2345",f"nufeb/eps_secretion 2 EPS 1.3 30 {random_number}")

        if sample == 1:
            updated_NUFEB = update2_NUFEB.replace("growth 0.00028 yield 0.61","growth 0.00028 yield 0.41")
        if sample == 2:
            updated_NUFEB = update2_NUFEB.replace("growth 0.00028 yield 0.61", "growth 0.00028 yield 0.46")
        if sample == 3:
            updated_NUFEB = update2_NUFEB.replace("growth 0.00028 yield 0.61", "growth 0.00028 yield 0.51")
        if sample == 4:
            updated_NUFEB = update2_NUFEB.replace("growth 0.00028 yield 0.61", "growth 0.00028 yield 0.56")
        if sample == 5:
            updated_NUFEB = update2_NUFEB.replace("growth 0.00028 yield 0.61", "growth 0.00028 yield 0.61")
        if sample == 6:
            updated_NUFEB = update2_NUFEB.replace("growth 0.00028 yield 0.61", "growth 0.00028 yield 0.66")
        if sample == 7:
            updated_NUFEB = update2_NUFEB.replace("growth 0.00028 yield 0.61", "growth 0.00028 yield 0.71")
        if sample == 8:
            updated_NUFEB = update2_NUFEB.replace("growth 0.00028 yield 0.61", "growth 0.00028 yield 0.76")

        with open(f"{new_sam_folder}/inputscript.nufeb", "w", encoding="utf-8") as file:
            file.write(updated_NUFEB)

        shutil.copy(f"{home_exp_directory}/atom.in", f"{new_sam_folder}/atom.in")

savedir_seed_file = f"{home_exp_directory}/Experiment_YieldSeeds_xlsx.xlsx"
seed_df.to_excel(savedir_seed_file, sheet_name="A", index=False)

# BASH SCRIPT MAKER =================================================================================================

bash_string = """
#!/bin/bash

cd /home/piotr/Desktop/NUFEB/Data/Experiment3

"""
experiment_folder = os.listdir(home_exp_directory)

for exp_folder in experiment_folder:
    if not exp_folder.endswith(".xlsx"):
        if not exp_folder.endswith(".png"):
            if not exp_folder.endswith(".nufeb"):
                if not exp_folder.endswith(".in"):
                    if not exp_folder.endswith(".txt"):
                        updateing_txt = f"cd {exp_folder}"
                        bash_string = f"{bash_string}\n{updateing_txt}"
                        exp_folder_directory = os.listdir(home_exp_directory + "/" + exp_folder)
                        for rep_folder in exp_folder_directory:
                            updateing_txt1 = f"cd {rep_folder}"
                            bash_string = f"{bash_string}\n{updateing_txt1}"
                            rep_folder_directory = os.listdir(home_exp_directory + "/" + exp_folder + "/" + rep_folder)
                            for sample_folder in rep_folder_directory:
                                print(sample_folder)
                                updateing_txt2 = f"cd {sample_folder}"
                                bash_string = f"{bash_string}\n{updateing_txt2}"
                                updateing_txt3 = "mpirun -np 24  nufeb_mpi -in inputscript.nufeb"
                                bash_string = f"{bash_string}\n{updateing_txt3}"
                                updateing_txt4 = "cd .."
                                bash_string = f"{bash_string}\n{updateing_txt4}"
                            updateing_txt5 = "cd .."
                            bash_string = f"{bash_string}\n{updateing_txt5}"

with open (f"{home_exp_directory}/Auto_NUFEB_Runner.sh", "w") as bash_file:
    bash_file.write(bash_string)
with open(f"{home_exp_directory}/Auto_NUFEB_Runner.txt", "w") as bash_file:
    bash_file.write(bash_string)


