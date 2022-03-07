from ij import IJ
import os 
from os.path import basename
from ij.plugin.frame import RoiManager
from ij.gui import PolygonRoi
from ij.gui import Roi
from java.awt import FileDialog
import glob

fd = FileDialog(IJ.getInstance(), "Open", FileDialog.LOAD)
fd.show()
path = fd.getDirectory()
print(path)

files = glob.glob(path+"*.tif")
RM = RoiManager()
rm = RM.getRoiManager()
rm.runCommand('reset')
	
print(files)
for file in files:
	imp = IJ.openImage(file)
	ImName=os.path.basename(file)
	InNamewhithoutext=os.path.splitext(ImName)[0]
	file_name= path+InNamewhithoutext+'_cp_outlines'+'.txt'
	print(file_name)
	imp.show()
	
	RM = RoiManager()
	rm = RM.getRoiManager()

	imps = IJ.getImage()

	textfile = open(file_name, "r")
	for line in textfile:
    	 xy = map(int, line.rstrip().split(","))
    	 X = xy[::2]
    	 Y = xy[1::2]
    	 imp.setRoi(PolygonRoi(X, Y, Roi.POLYGON))
    	 # IJ.run(imp, "Convex Hull", "")
    	 roi = imp.getRoi()
    	 print(roi)
    	 rm.addRoi(roi)
	textfile.close()
	rm.runCommand("Associate", "true")
	rm.runCommand("Show All")
	roiname=path+InNamewhithoutext+'ROI'+'.zip'
	rm.runCommand("save selected", roiname)
	rm = RoiManager.getInstance()
	rm.runCommand('reset')
	imp.close()
	
	

