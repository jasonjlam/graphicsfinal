from script import run
import sys
from display import clear_images

if len(sys.argv) == 2:
    sys.argv[1] = "files/" + sys.argv[1]
    clear_images()
    run(sys.argv[1])
    # print ("Please enter a valid file type (obj, mdl, ASCII stl).")
elif len(sys.argv) == 1:
    run(raw_input("Please enter the filename of a valid script file: \n"))
else:
    print("Too many arguments.")
