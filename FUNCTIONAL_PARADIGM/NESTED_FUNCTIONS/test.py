import os

path = "C:\\Users\\Назар\\Favorites\\Desktop\\PYTHON"
#for root, dirs, files in os.walk(path):
#    print("{0} has {1} directories and {2} files".format(root, len(dirs), len(files)))


cwd = os.walk(path)

for i in cwd:
    print()
    print(i)