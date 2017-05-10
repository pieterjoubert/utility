import glob, os
os.chdir("C:\\Users\\piete\Dropbox\\2017\\IIE\\GADE5112\\test\\")
for file in os.listdir("."):
	if file[:13] == "Test 1 Upload":
		print(file[14:22] + file[-4:])
		os.rename(file, file[14:22] + file[-4:])