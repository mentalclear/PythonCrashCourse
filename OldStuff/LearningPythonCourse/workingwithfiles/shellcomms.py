import os
from os import path
import shutil
from shutil import make_archive

def main():
    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")

        dst = src + ".bak"

        # shutil.copy(src, dst)
        # shutil.copystat(src, dst)

        #os.rename("textfile.txt.bak", "newfile.txt")

        # make archive
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)



if __name__ == '__main__':
    main()
