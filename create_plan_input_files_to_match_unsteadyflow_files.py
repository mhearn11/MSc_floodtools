#-------------------------------------------------------------------------------
# Name:        pln_mod_1
# Purpose:      Create 99 HEC-RAS plan files that integrate the 99 flow files.
#                   Includes modifications to the title and flow file path

# Author:      Hearn
#
# Created:     05/04/2017
# Copyright:   (c) Hearn 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#   uns_mod_6 works for multiple sims and multiple subcatchments
#   pln_mod_1 was intended to jump over the need to import each of the uns files
#       but it seems that HEC-RAS requires us to import each of them anyway
#       so, skip this one /:
#   For what it's worth, it works for creating importable pXX files

# Prerequisites
#   -review the template file to make sure the rest of the data is correct
#   -remember that, if you save a HECRAS prj with a new name, it copies all of
#       the uns (and other) files, so you prob need to delete them in order to
#       make space for the 99
#   -make sure the template, data, and output file paths are correct

import os

# STEP 1: Create the template variable
template = open("C:/thesisHECRAS/Templates/Mulde3template.p99").read()
tick = 0

### START HERE - write a for loop that does this for each file in the folder....
for filename in os.listdir("C:/thesisHECRAS/Qfiles"):
        if filename.endswith(".txt"):
            # STEP 2: Create other 2 change variables
            title = filename[:-4]
            shortID = filename[:-4]
            tick = tick + 1

            flowfile = "u"+str(tick).zfill(2)
        
            # STEP 3: Output the new file
            # Need to change this to printing to a file, not just printing the output
            output = template.format(title, shortID, flowfile)
            print "output created, now writing file"
            a= open("C:/thesisHECRAS/PLN/Mulde3.p"+str(tick).zfill(2),"w+")
            a.write(output)
            a.close()

print "done"
