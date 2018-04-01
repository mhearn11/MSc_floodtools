#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Hearn
#
# Created:     13/07/2017
# Copyright:   (c) Hearn 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------



import pandas as pd # For reading the excel file
import os
import numpy as np

df = pd.DataFrame(np.random.randn(64,4),index=range(0,64),columns=list('hfmc'))
i = 0

### START HERE - write a for loop that does this for each file in the folder....
for filename in os.listdir("C:/thesisCalRes/pln23_h_fp_m_tables"):
    t = pd.read_excel("C:/thesisCalRes/pln23_h_fp_m_tables/"+filename,filename[:-4])
    h = t["POLY_AREA"][0]
    fp = t["POLY_ARE_1"][1]
    m = t["POLY_ARE_2"][2]
    csi = h/(h+fp+m)
#   getting the ID in, would need to convert a column to string, meh
#    id = filename[:-4][4:]
#    df.set_value(i,'t',id)
    df.set_value(i,'h',h)
    df.set_value(i,'f',fp)
    df.set_value(i,'m',m)
    df.set_value(i,'c',csi)
    print i
    i=i+1
#writer = pd.ExcelWriter('C:/thesisCalRes/csi.xlsx')
#df.to_excel(writer,'Sheet1')
#writer.save()    


#    a= open("C:/thesisCalRes/csi.csv","w+")
#    a.write(df)
#    a.close()

print "done"
