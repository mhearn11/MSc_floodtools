# MSc_floodtools
The scripts contained in MSc_floodtools were developed over the course of my master's thesis research. They were developed as small, limited function scripts in order to allow for maximum visibility at each stage. With additional testing and needed capacity to automatically convert input format types, the these tools could eventually be combined into a stronger, more continuous program. I imagined them to represent a very limited form of prototype for speeding up calibration and uncertainty analyses in HEC-RAS. The title of this thesis is "Evaluation of 1D/2D river flood simulation with HEC-RAS 5.0.3 considering change of boundary conditions," and it was conducted at the Technische Universität Dresden from February-August 2017.

A number of the scripts are designed to create a series of input files (to then be run through HEC-RAS using the Run Multiple Plans feature), and others are for managing the results. There are also a couple to produce quick plots of all of the input hydrographs.

I had to create the HEC-RAS model first and build templates for the unsteady flow files and plan files. I had my folders set up within a separate folder on the C drive:
In the PROJ folder I stored the HEC-RAS project and added files to be directly run through HEC-RAS.
In the Qfiles folder I stored the discharge hydrographs (in my case as txt files).
In the Templates folder I stored templates for the unsteady flow files and plan files.
In the UNS folder I stored the unsteady flow files generated by a script using the template and hydrographs.
In the PLN folder I stored the plan files generated by a script using the template and hydrograph files.
When I ran HEC-RAS, results would be generated in the PROJ folder, and I created a new file in the PROJ folder called dmax_renamed (for maximum depth over a given simulation period) where I collected the result layers I wanted (and usually pulled them into ArcGIS for analysis, but I'm sure QGIS would be fine for analysis as well).
