- Root folder contains ConductedEmissionsGraph.exe which takes input data from "data" folder and makes plots of them. 
- Plots will be saved in "result" folder
- "data" must have this exact name, otherwise will not be found
- data contains subfolders, which contains .csv data of each particular measurement (AC-230V-L, AC-230V-N, Eth1 ... etc). Name of this folder will be 
also used as a name of each chart, so it should be named properly. 
- The name of each subfolders should contain "AC" for AC measurement, "DC" for DC measurement and "ETH" for ethernet measurement. Based on these characters
the proper limits are drawn into a plots.
- Each subfolder must contain Trace00000.csv (containing Peak measurement values from 150kHz to 80MHz) and Trace00001.csv (containing emi average measurement values from 150kHz to 80MHz). Both files must carry this exact name. 
- Subfolder may optionally contain also SignalL00000.csv (containing re-measurement of peak values from Trace00000.csv) and SignalL00001.csv (containing re-measurement of peak values from Trace00001.csv)


structure of files:

# root (home_path) - ConductedEmissionsGraph.exe
# 		   - data (test_path) - AC L (tests[0]) - Trace00000.csv (peak line)
#                                                       - Trace00001.csv (emi average line)
#                                                       - SignalL00000.csv (re-measurement points, optional)
#                                                       - SignalL00001.csv (re-measurement points, optional)
#                                     - Eth1 (tests[1]) - Trace00000.csv
#                                                       - Trace00001.csv
#                                                       - SignalL00000.csv (optional)
#                                                       - SignalL00001.csv (optional)
#                                           .
#                                           .
#                                           .
#                                           .
