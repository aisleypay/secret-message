# Mini-Project: Secret Message

# Your friend has hidden your keys! To find out where they are,
# you have to remove all numbers from the files in a folder
# called prank. But this will be so tedious to do!

import os
def rename_files():
	# get file names from a folder
	#replace path with the file location you need
	file_list = os.listdir("/Users/nothinlkepaisley/Documents/Intro_to_Programming/prank")
	print file_list
	saved_path = os.getcwd()
	print ("Current working directory is " +saved_path)
	#replace path with the file location you need
	os.chdir("/Users/nothinlkepaisley/Documents/Intro_to_Programming/prank")

	
	#rename file name for each file
	for file_name in file_list:
		#removes number from file name
		print ("Old Name - "+file_name)
		os.rename(file_name, file_name.translate(None, "0123456789"))
		os.chdir(saved_path)
rename_files()