# func: looks in a folder (temporarily will be folder called softwareblurbs)
# 	and gets all the text files, creates a .md file based off of that 
# 	and adds it to the btl repo in the folder software	

import glob, os

os.chdir("../softwareblurbs")
for file in glob.glob("*.txt"):
	doc = open(file)
		
	name = doc.readline().strip()
	newfile = open("../software/" + name + ".md", "w")
	newfile.write(doc.read())

