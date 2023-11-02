import glob
import os

##Firstly, you delete the trimed.fa whose size is 0
##Find and delete empty files
directory_path = "./"
empty_files = []

##Detect the file whose size is 0 and append the "empty_files" list.
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
        empty_files.append(filename)
print(empty_files)

##Remove files whose size is 0
for filename in empty_files:
    file_path = os.path.join(directory_path, filename)
    os.remove(file_path)

##Write file names on "output.txt"
with open('output_iqtree.txt', 'w') as file:
    file.write(f"Deleted files are {', '.join(empty_files)}\n")

##Second, you make "run.nex" file to run iqtree2
list = []
for i in glob.glob('*.maffted.trimed.edit.fa'):
        list.append(os.path.split(i)[1].rstrip())

print(len(list))


f = open("run.nex", "w")
f.write("#nexus" + "\n")
f.write("begin sets;" + "\n")
character = "charset part"
for line, i in zip(list, range(len(list))):
        row = character + str(i+1) + " = " + line + ": ;"
        f.write("\t" + row + "\n")
f.write("end;" + "\n")
f.close()

##Next, you run the beloq command.
##sh iqtree.sh
