from display import *
from matrix import *
from draw import *

def parse_ASCIISTL( fname):
    frame = 0
    while (frame < 50):

        view = [0,
                0,
                1];
        ambient = [50,
                   50,
                   50]
        light = [[0.5,
                  0.75,
                  1],
                 [255,
                  255,
                  255]]

        color = [0, 0, 0]
        tmp = new_matrix()
        ident( tmp )

        stack = [ [x[:] for x in tmp] ]
        screen = new_screen()
        zbuffer = new_zbuffer()
        tmp = []
        with open(fname, 'r', errors='replace') as f:
            lines = f.readlines()
        f.close()
        basename = fname[6:-4]
        clear_screen(screen)
        clear_zbuffer(zbuffer)
        step = 100
        step_3d = 20

        symbols = {'white':['constants',
                             {'red': [0.2, 0.5, 0.5],
                              'green': [0.2, 0.5, 0.5],
                              'blue': [0.2, 0.5, 0.5]}]}
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

        t = make_translate(250, 60, 0)
        matrix_mult(stack[-1], t)
        stack[-1] = [x[:] for x in t]

        t = make_scale(4, 4, 4)
        matrix_mult(stack[-1], t)
        stack[-1] = [x[:] for x in t]

        t = make_rotY(math.pi / 25 * frame)
        matrix_mult(stack[-1], t)
        stack[-1] = [x[:] for x in t]


        t = make_rotX(-80.0 * (math.pi / 180))
        matrix_mult(stack[-1], t)
        stack[-1] = [x[:] for x in t]

        matrix_mult(stack[-1], tmp)
        draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, 'white')

        sname = 'anim/%s%03d.png'%(basename, frame)
        print('Saving frame: '  + sname)
        save_extension(screen, sname)
        # end fromes loop
        frame +=1
    make_animation(basename, 3.3)
