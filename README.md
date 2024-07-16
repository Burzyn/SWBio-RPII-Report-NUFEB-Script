# NUFEB-2 Simuations as part of the SWBio DTP RPII report
#
#
#
#
## Framework Features

The follwoing Python framework allowed to substantially automate the process of generating and analysing NUFEB-2 simuations.

## Framework Files

Files used to create the experiemnt directories, NUFEB input files and .sh scripts based on experiemental design:

- NUFEB_Seed_Randomiser_Exp4
- NUFEB_Seed_Randomiser_Exp5
- NUFEB_Seed_Randomiser_Exp6

Files used to analyse the NUFEB simulations in parent directory and combine all data into specific files:

- HDF5_Code_Reader
    - HDF5_Cell_Reader
    - HDF5_CellMaxSurface_Finder
    - HDF5_Surface_Finder
- Result Contactor

Files used to analyse and plot all data:

- Result_Plotter
    - Result_Timepoint_Analyser
    - Result_Surface_Analyser_I
    - Result_Surface_Analyser_II
    - Result_Surface_Analyser_III
- Result_Matrix_Analyser

