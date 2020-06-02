from script import run
import sys
from stl import *
from obj import *

if len(sys.argv) == 2:
    sys.argv[1] = "files/" + sys.argv[1]
    clear_images()
    if sys.argv[1][-4:] == ".stl":
        parse_ASCIISTL(sys.argv[1])
    elif sys.argv[1][-4:] == ".mdl":
        run(sys.argv[1])
    elif sys.argv[1][-4:] == ".obj":
        parse_obj(sys.argv[1])
    else:
        print ("Please enter a valid file type (obj, mdl, ASCII stl).")
elif len(sys.argv) == 1:
    run(raw_input("Please enter the filename of a valid script file: \n"))
else:
    print("Too many arguments.")
