# this program should be ran to get all tags within the simages

# TODO: implement checking if any tags are just never used within templates
    # shouldn't be hard :^)

import os

listDir = os.listdir("./simages/")
clone = list(listDir)

types = []
numtype = []
trouble = []
for i in listDir:
    # get simply the tags string
    tags = (i[i.find(",") + 1:])
    tags = tags[:tags.find(".")]

    # check for troublesome stuff and count up any tags
    for type in tags.split(" "):
        if(type in types):
            numtype[types.index(type)] = numtype[types.index(type)] + 1
        else:
            if(type == "" or (i.find(".") == -1)):
                trouble.append(i)
            else:
                types.append(type)
                numtype.append(1)

    if ", " in i and i not in trouble:
        trouble.append(i)
        
Files = ""
for n in range(len(types)):
    idkStr = ("\n" if n != (len(types) - 1) or len(trouble) > 0 else "")
    Files += "-" + str("\"" + types[n]) + "\" with " + str(numtype[n]) + " files" + idkStr

print("Different tags in there:\n" + Files, end = "")

if len(trouble) > 0:
    print("Also, these files are trouble!:\n" + "\n".join(trouble), end = "")