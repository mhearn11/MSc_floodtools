#-------------------------------------------------------------------------------
# Name:        
# Purpose:      
# Author:      Hearn
#
# Created:     2017
# Copyright:   (c) Hearn 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import pandas as pd # For reading the excel file
import os
import matplotlib.pyplot as plt


# TO SET UP THE DF_ALL
txt = pd.read_csv("C:/thesisHECRAS/Qfiles/HW_EH5L3RACMO_00_1.txt")
txt.columns = ['Timestamp']
df = pd.DataFrame(txt.Timestamp.str.split('\t',1).tolist(), columns = ['timestamp','Q'])
df["timestamp"] = pd.to_datetime(df["timestamp"])
df_all = df

# TO POPULATE DF_ALL with all of the Q data
Qfilespath = "C:/thesisHECRAS/Qfiles/"

for filename in os.listdir(Qfilespath):
    if filename.endswith(".txt"):
        txt = pd.read_csv(os.path.join(Qfilespath,filename))
        txt.columns = ["Timestamp"]
        df = pd.DataFrame(txt.Timestamp.str.split('\t',1).tolist(), columns = ['timestamp','Q'])
        df_all = df_all.assign(Q=df.Q.values)
        df_all = df_all.rename(columns ={"Q":filename[:-4]})
        print filename
    
    
        output = df.drop(df.index[[range(408)]]).drop(df.index[[range(601,1000)]])
        print filename+" output created, now writing file"
        a= open("C:/thesisHECRAS/Qfiles/8day/"+filename,"w+")
        a.write(output.to_string())
        a.close()
    
    

# TO PLOT THEM ALL ON THE SAME PLOT (by simulation-hour, but still)
for i in range(56):
    plt.plot(df_all[[i+1]])

#in case you want the timestamp
#print df_all[[0]]


# EXTRA STUFF THAT DIDN'T GET USED
#from datetime import datetime
#datstr = df.Timestamp[0]
#datdt = datetime.strptime(datstr,"%Y-%m-%d %H:%M:%S")
#says it doesn't work for df column b/c it is a series, not a string
#df = df.assign(dtstamp=datetime.strptime(df.Timestamp,"%Y-%m-%d %H:%M:%S")
