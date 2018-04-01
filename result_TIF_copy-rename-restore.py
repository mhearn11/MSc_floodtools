# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 10:24:51 2017

Purpose of this program is just to copy all of the tifs from the indiv HECRAS
Q_sim output folders and save them in the Res_raw folder with a unique name

@author: Hearn
"""

import os
import shutil

main_dir = r"C:/thesisHECRAS/PROJ"
dst_dir = r"C:/thesisHECRAS/PROJ/dmax_renamed"
for foldername in os.listdir(main_dir):
    if foldername.startswith("HW"):
        if ".p" not in foldername:
            for filename in os.listdir(main_dir + "/" + foldername):
                if filename.endswith(".tif"):
                    src_dir= main_dir+"/"+foldername
                    src_file = os.path.join(src_dir, filename)
                    shutil.copy(src_file,dst_dir)
                    dst_file = os.path.join(dst_dir, filename)
                    new_dst_file_name = os.path.join(dst_dir, foldername.replace(" ","")+".tif")
                    os.rename(dst_file, new_dst_file_name)
                    continue
    else:
        continue
