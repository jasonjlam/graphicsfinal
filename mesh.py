from display import *
from matrix import *
from draw import *

def meshSelect(fname, tmp):
    fname = 'files/' + fname + '.obj'
    with open(fname, 'r', errors='replace') as f:
        lines = f.readlines()
    f.close()

# For some reason yacc doesn't play nice with file names, stl support deprecated
    if fname[-4:] == ".stl":
        parse_ASCIISTL(lines, tmp)
    elif fname[-4:] == ".obj":
        parse_OBJ (lines, tmp)
    else:
        print ("Please enter a valid mesh file.")

def parse_ASCIISTL(lines, tmp):
    c = 0
    while c < len(lines):
        line = lines[c].strip()
        if line == "outer loop":
            c+=1
            arg0 = lines[c].strip().split(' ')
            c+=1
            arg1 = lines[c].strip().split(' ')
            c+=1
            arg2 = lines[c].strip().split(' ')
            add_polygon(tmp, float(arg0[1]), float(arg0[2]), float(arg0[3]),
                        float(arg1[1]), float(arg1[2]), float(arg1[3]), float(arg2[1]), float(arg2[2]), float(arg2[3]))
        c+=1

def parse_OBJ (lines, tmp):
    # print (lines)
    c = 0
    count = 0
    points = [[0,0,0]]
    while c < len(lines):
        line = lines[c].strip().split(' ')
        if line[0] == "v":
            line[:] = [x for x in line if x.strip()]
            vertex = [float(i) for i in line[1:]]
            # print(vertex)
            points.append(vertex)
            # print (points)
        if line[0] == "f":
            i = 1
            indexes = []
            while i < len(line):
                # print (line)
                indexes.append(int((line[i].split('/')[0])))
                i += 1
            poly_index = len(line)
            poly_current = 0
            # print (indexes)
            # print (poly_index)
            while poly_current < poly_index - 3:
                # print(points)
                # print(points[indexes[0]])
                # print (poly_current)
                # print(indexes)
                add_polygon(tmp, points[indexes[0]][0], points[indexes[0]][1], points[indexes[0]][2],
                                 points[indexes[poly_current + 1]][0], points[indexes[poly_current + 1]][1], points[indexes[poly_current + 1]][2],
                                 points[indexes[poly_current + 2]][0], points[indexes[poly_current + 2]][1], points[indexes[poly_current + 2]][2])
                # print ([points[indexes[0]][0], points[indexes[0]][1], points[indexes[0]][2],
                #                  points[indexes[poly_current + 1]][0], points[indexes[poly_current + 1]][1], points[indexes[poly_current + 1]][2],
                #                  points[indexes[poly_current + 2]][0], points[indexes[poly_current + 2]][1], points[indexes[poly_current + 2]][2]])
                count +=1
                poly_current += 1
        c += 1
    # print (count)
