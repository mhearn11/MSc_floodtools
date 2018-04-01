#-------------------------------------------------------------------------------
# Name:        uns_mod_1
# Purpose:      Create 99 HEC-RAS unsteady flow files based on a template with
#                   modifications to the title, initial flow condition for each
#                   upstream boundary station, and the flow hydrograph values
#                   (1-hour interval, fixed simulation length)
# Author:      Hearn
#
# Created:     03/04/2017
# Copyright:   (c) Hearn 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
######STATUS    uns_mod_2 works for 1 subcatchment and 1 uns file.
#               uns_mod_3 works for multiple subcatchments, but still 1 uns file
#               This file, uns_mod_6 works for multiple sims and multiple scs
#               Confirmed - it imports properly into HECRAS

# Prerequisites
#   -review the template file
#   -remember that, if you save a HECRAS prj with a new name, it copies all of
#       the uns (and other) files, so you prob need to delete them in order to
#       make space for the 99
#   -make sure the template, data, and output file paths are correct

import pandas as pd # For reading the excel file
import os

Qfilespath = "C:/thesisHECRAS/Qfiles/"

# STEP 1: Create the template variable
template = open("C:/thesisHECRAS/Templates/Mulde3template.u99").read()
tick = 0
tock = 0   



for filename in os.listdir(Qfilespath):
    if filename.endswith(".txt"):
    # STEP 2: Create hydrograph_str for input to template
        txt = pd.read_csv(os.path.join(Qfilespath,filename))
        txt.columns = ["Timestamp"]   
        df = pd.DataFrame(txt.Timestamp.str.split('\t',1).tolist(), columns = ['timestamp','Q'])
        df_peak = df.drop(df.index[[range(408)]]).drop(df.index[[range(601,1000)]])
        hydrograph = list(df_peak["Q"].values)     
      
        hydrograph_str = ""
        for i in range(1, len(hydrograph_stable)+1):
            hydrograph_str += "{:8}".format(hydrograph_stable[i-1])
            if i % 10 == 0:
                hydrograph_str += "\n" # start new line
    
        #  This will need to be changed if doing more than 99
        tick = tick + 1
    
        # STEP 3: Create title
        title = filename[:-4]
    
        # STEP 4: Output the new file
        output = template.format(title, hydrograph_str)
        print "output created, now writing file"
        a= open("C:/thesisHECRAS/UNS/Mulde3.u"+str(tick).zfill(2),"w+")
        a.write(output)
        a.close()

print "done"


df_peak.index = range(len(df_peak))
df_stable = df_peak
for j in df_peak:
    if flt(df_peak["Q"][j]) < 20:
        df_stable["Q"][j] = "20.00"


pd.to_numeric(df_peak)




  hydrograph_stable = [0]*len(df_peak)
        for j in hydrograph_flt:
            if j < 20.00:
                hydrograph_stable[tock] = 20
                tock = tock + 1
            else:
                hydrograph_stable[tock] = j
                tock = tock +1
                continue

hydrograph_stable = []
for i in hydrograph_flt:
    if hydrograph_flt[i] < 20.00:
        hydrograph_stable[i] = 20
    else:
        hydrograph_stable[i] = hydrograph_flt[i]
        
tock = 0   
n = 12 
hydrograph_stable = [0]*len(df_peak)
for i in hydrograph_flt:
    if i < 20.00:
        hydrograph_stable[tock] = 20
        tock = tock + 1
    else:
        hydrograph_stable[tock] = i
        tock = tock +1




        for value in hydrograph:
            if hydrograph[value] < 20:
                
hydrograph_flt = [float(i) for i in hydrograph]
data[data > upper_threshold] = default_value

for 
hydrograph_flt[hydrograph_flt < 20] = 20

