import os

dest = ""

os.chdir(dest)

for index, file in enumerate(os.listdir()):
    st = file.replace('0', str(index+1))
    print(st)
    os.rename(file, st)