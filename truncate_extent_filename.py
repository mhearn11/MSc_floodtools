#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Hearn
#
# Created:     14/07/2017
# Copyright:   (c) Hearn 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#truncate_extents

import os
import shutil

main_dir = r"C:/thesisCalRes/pln23_extents"
for filename in os.listdir(main_dir):
    if filename.startswith("Ext"):
         os.rename(os.path.join(main_dir,filename), os.path.join(main_dir,filename[6:]))
    continue