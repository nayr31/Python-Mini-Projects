import os, shutil

home = "C:\\Users\\Ryan\\My Drive\\Obsidian\\LancerStorage\\Tokens\\NPC Tokens\\SSC Black Suite"
os.chdir(home)

try:
    os.mkdir("no-glint")
except:
    print("// no-glint folder already exists //")

print("Gathering and moving files...")
for x in os.listdir():
    if os.path.isfile(x) and "-Inactive.png" in x:
        shutil.move(x, "no-glint\\" + x)
        print("Moved " + x)
print("Finished")