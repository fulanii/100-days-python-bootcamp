
import os

# Small scrip to creat readme files for each day in the beginner section
os.chdir(f"BeginnerSection")

for i in range(1, 15):
    if i < 10:
        os.chdir(f"day0{i}")
        with open("README.md", "x") as file:
            file.write(f"##Day {i}")
        os.chdir("..")
    else:
        os.chdir(f"day{i}")
        with open("README.md", "x") as file:
            file.write(f"##Day {i}")
        os.chdir("..") 
print("Done")


# Small scrip to creat readme files for each day in the Intermediate section
os.chdir(f"IntermediateSection")

for i in range(15, 59):
    day = os.mkdir(f"day{i}")
    os.chdir(f"day{i}")

    with open("README.md", "x") as file:
        file.write(f"# Day {i} - ")
    os.chdir("..")
 
print("Done")


