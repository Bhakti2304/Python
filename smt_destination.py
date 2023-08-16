from os import path


def create_file(dest):
    if not (path.isfile(dest)):
        f=open(dest,'w')
        f.write("Welcome to Python scripting")
        f.close()

dest="C:\\Users\\Bhakti\\Downloads\\sample.txt"

create_file(dest)

print("file created!")