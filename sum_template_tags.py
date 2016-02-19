# this program should be ran to get all tags within the simages

# TODO: implement checking if any tags are just never used within templates
	# shouldn't be hard :^)

import os

listDir = os.listdir("./templates/")
clone = list(listDir)

types = []
numtype = []
trouble = []
for i in listDir:
	# split each entry in template
	# get tags string (first sub entry)
	# split tags string
	# sift for trouble
	
	for x in i.split(";"):
		for type in i.split(",")[0].split(" "):
			if type in types:
				numtype[types.index(type)] = numtype[types.index(type)] + 1
			else:
				if type == "":
					trouble.append(i)
				else:
					types.append(type)
					numtype.append(1)

	if ", " in i and i not in trouble:
		trouble.append(i)
		
Files = ""
for n in range(len(types)):
	idkStr = ("\n" if n != (len(types) - 1) or len(trouble) > 0 else "")
	Files += "- " + str("\"" + types[n]) + "\" with " + str(numtype[n]) + " templates" + idkStr

print(Files, end = "")

if len(trouble) > 0:
	print("Also, these files are trouble!:\n" + "\n".join(trouble), end = "")