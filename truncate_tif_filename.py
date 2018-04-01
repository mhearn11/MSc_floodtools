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

# Works.
# shutil is unused

import os
import shutil

main_dir = r"C:/thesisHECRAS/short"
for filename in os.listdir(main_dir):
    if filename.startswith("HW"):
         os.rename(os.path.join(main_dir,filename), os.path.join(main_dir,filename.replace("_","")[7:]))
    continue