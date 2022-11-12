# add -v for verbose
# get Pillow (fork of PIL) from
# pip before running -->pip
# pip install Pillow

# import required libraries
import os
import sys
from tkinter import filedialog
from PIL import Image
from tkinter.filedialog import*

# define a function for
# compressing an image
def compressMe(file, verbose = False):
	
	# Get the path of the file
	# filepath = os.path.join(os.getcwd(),file)
	filepath = askopenfilename()
	# open the image
	picture = Image.open(filepath)
	print('compressing', filepath[37:])
	
	picture.save("Compressed_"+filepath[37:],
				"JPEG",
				optimize = True,
				quality = 10)
	return

# Define a main function
def main():
	
	verbose = False
	
	# checks for verbose flag
	if (len(sys.argv)>1):
		
		if (sys.argv[1].lower()=="-v"):
			verbose = True
					
	# finds current working dir
	# change working directory

	cwd = os.chdir("Newfolder")

	formats = ('.jpg', '.jpeg')
	
	# looping through all the files
	# in a current directory
	for file in os.listdir(cwd):
		# If the file format is JPG or JPEG
		if os.path.splitext(file)[1].lower() in formats:
			# print('compressing', file)
			compressMe(file, verbose)
			break
		
	print("Done")

# Driver code
if __name__ == "__main__":
	main()
