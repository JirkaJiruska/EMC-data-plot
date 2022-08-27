from ntpath import join
from matplotlib import ticker
# pip install matplotlib==3.0.3 https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz
# older version freezes when as executable
import time
import os, sys
import matplotlib.pyplot as plt


def quit_fcn():
    print("\nQuitting in...")
    for i in [4, 3, 2, 1]:
        print(i)
        time.sleep(1)
    exit()


def draw_limits(name = ''):
  
    lim_color = 'black'
    lim_style = 'dashed'
    lim_width = 0.7
    text_space = 0.3

    if 'eth' in name.lower():
        x = [150000, 500000, 80000000]
        y_pk_B = [84, 74, 74]
        y_av_B = [74, 64, 64]
        y_pk_A = [97, 87, 87]
        y_av_A = [84, 74, 74]
        plt.plot(x, y_pk_A, x, y_av_A, color=lim_color, linestyle=lim_style, linewidth=lim_width)
        plt.plot(x, y_pk_B, x, y_av_B, color=lim_color, linestyle=lim_style, linewidth=lim_width)
        plt.text(1000000, y_pk_B[1]+text_space, "Class B limit for Peak detector")
        plt.text(1000000, y_av_B[1]+text_space, "Class B limit for Emi Average detector")
        plt.text(1000000, y_pk_A[1]+text_space, "Class A limit for Peak detector")
        plt.text(1000000, y_av_A[1]+text_space + 1.5, "Class A limit for Emi Average detector")
        return
    if 'dc' in name.lower():
        x = [150000, 500000, 500001, 80000000]
        y_pk = [79, 79, 73, 73]
        y_av = [66, 66, 60, 60]
        plt.plot(x, y_pk, x, y_av, color=lim_color, linestyle=lim_style, linewidth=lim_width)
        plt.text(1000000, y_pk[2]+text_space, "Limit for Peak detector")
        plt.text(1000000, y_av[2]+text_space, "Limit for Emi Average detector")
        return
    if 'ac' in name.lower():
        x = [150000, 500000, 500001, 5000000, 5000001, 80000000]
        y_pk_B = [66, 56, 56, 56, 60, 60]
        y_av_B = [56, 46, 46, 46, 50, 50]
        y_pk_A = [79, 79, 73, 73, 73, 73]
        y_av_A = [66, 66, 60, 60, 60, 60]
        plt.plot(x, y_pk_A, x, y_av_A, color=lim_color, linestyle=lim_style, linewidth=lim_width)
        plt.plot(x, y_pk_B, x, y_av_B, color=lim_color, linestyle=lim_style, linewidth=lim_width)
        plt.text(1000000, y_pk_B[3]+text_space, "Class B limit for Peak detector")
        plt.text(1000000, y_av_B[3]+text_space, "Class B limit for Emi Average detector")
        plt.text(1000000, y_pk_A[3]+text_space, "Class A limit for Peak detector")
        plt.text(1000000, y_av_A[3]+text_space, "Class A limit for Emi Average detector")
        return
    else:
        print("No limit selected")
        return


# root (home_path) - data (test_path) - AC L (tests[0]) - Trace00000.csv (peak line)
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



home_path = os.path.dirname(sys.argv[0])
test_path = home_path + "/data/"
results_path = home_path + '/results/'

if not os.path.exists(test_path):
    os.mkdir(test_path)
if not os.path.exists(results_path):
    os.mkdir(results_path)

# create list of present folders (without files) - "tests" is list of folders whose names is also used as a plot name
tests = [dir for dir in os.listdir(test_path) if os.path.isdir(join(test_path,dir))]

# search every subfolder in the root folder. Every folder represents one complete measurement (AC L, AC N, DC, Eth ... ) with complete data and each cycle will create one graph
for test in tests:
    data_path = test_path + test + '/'

    # colors
    colors_dict = {0:'blue', 1:'orange'}

    # list of files for particular measurement. Every file should contain "Trace_0000.csv" and "Trace_0001.csv" and may optionally contain "SignalL_0000.csv" and "SignalL_0000.csv"
    filelist = os.listdir(data_path)

    # load Trace csv files for Peak and Emi Average
    legend_dict = {"Trace_0000.csv" : "Peak", "Trace_0001.csv" : "Emi Average", "SignalL_0000.csv" : "Quasi Peak", "SignalL_0001.csv" : "Emi Average"}

    trace_files = []
    # find "Trace_0000.csv" which must contain PK values
    if "Trace_0000.csv" in filelist:
        trace_files.append("Trace_0000.csv")
    else:
        print("Trace_0000.csv not found")
        quit_fcn()
    # find "Trace_0001.csv" which must contain Emi average values
    if "Trace_0001.csv" in filelist:
        trace_files.append("Trace_0001.csv")
    else:
        print("Trace_0001.csv not found")
        quit_fcn()


    signal_files = []
    # find "SignalL_0000.csv" which must contain Emi average peak values for "Trace_0000.csv"
    if "SignalL_0000.csv" in filelist:
        signal_files.append("SignalL_0000.csv")
    else:
        print("SignalL_0000.csv not found")
    # find "SignalL_0001.csv" which must contain Emi average peak values for "Trace_0001.csv"
    if "SignalL_0001.csv" in filelist:
        signal_files.append("SignalL_0001.csv")
    else:
        print("SignalL_0001.csv not found")


    # legend to draw on the plot
    legend = []
    [legend.append(legend_dict[file]) for file in trace_files]
    [legend.append(legend_dict[file]) for file in signal_files]

    # creates plot with specific size. AX is object for working with axes
    #fig = plt.figure(figsize=(20,10))
    fig, ax = plt.subplots(1, figsize=(25,15))

    # draw Trace_0000.csv and Trace_0001.csv into a plot
    for file in trace_files:
        dataX = []
        dataY = []
        with open(data_path + file,'r') as f:
            lines = f.readlines()[19:]
            for line in lines:
                dataXY_str = line.split(',')
                dataXY_f = [float(dataXY_str[0]), float(dataXY_str[1])]
                dataX.append(dataXY_f[0])
                dataY.append(dataXY_f[1])
        
        # select color based on number in file name - 0=Peak, 1=Emi Average
        plt.plot(dataX, dataY, color=colors_dict[int(file[-5])])


    # draw SignalL_0000.csv and SignalL_0001.csv into a chart if there is any
    for file in signal_files:
        dataX = []
        dataY = []
        with open(data_path + file,'r') as f:
            lines = f.readlines()[9:]
            for line in lines:
                dataXY_str = line.split(',')
                dataXY_f = [float(dataXY_str[3]), float(dataXY_str[5])]
                dataX.append(dataXY_f[0])
                dataY.append(dataXY_f[1])
                
        # select color based on number in file name - 0=Peak, 1=Emi Average
        plt.scatter(dataX, dataY, color=colors_dict[int(file[-5])])
        

    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude [dBμV]')
    plt.title('Conducted emissions: ' + test)
    plt.grid(True)    
    plt.grid(which='minor')
    plt.legend(legend)
    plt.xlim(150000, 30000000)
    plt.xscale('log')

    # formats X-axis and adds suffix 
    mkfunc = lambda x, pos: '%1.0fM' % (x * 1e-6) if x >= 1e6 else '%1.0fK' % (x * 1e-3) if x >= 1e3 else '%1.0f' % x
    mkformatter = ticker.FuncFormatter(mkfunc)
    ax.xaxis.set_minor_formatter(mkformatter)
    ax.xaxis.set_major_formatter(mkformatter)
    

    draw_limits(test)    
    plt.savefig(results_path + test + '.png')


