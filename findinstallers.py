import os
import pathlib

path = input("Enter Path: ")
extenstions = []
quitb = "q"
ext = ""
while ext is not quitb:
    ext = input("Enter extension(*) or continue(q): ")
    if ext is not quitb:
        extenstions.append(ext)

files = os.listdir(path)
paths = [path]
while len(paths) > 0:
    for x in files:
        try:
            if os.path.isdir(paths[0]+"\\"+x):
                paths.append(paths[0]+"\\"+x)

            else:
                if len(extenstions) == 0:
                    print(paths[0]+"\\"+x)
                elif pathlib.Path(paths[0]+"\\"+x).suffix in extenstions:
                    print(paths[0]+"\\"+x)

        except:
            pass
    paths.pop(0)
    test = 0
    while test == 0:
        try:
            if len(paths) == 0:
                break
            files = os.listdir(paths[0])
            test = 1
        except:
            paths.pop(0)
