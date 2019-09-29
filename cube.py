# -*- coding: utf-8 -*-
r = 'r'
g = 'g'
b = 'b'
y = 'y'
w = 'w'
o = 'o'

'''
       0   1
       2   3
       ------
16 17 |4   5 |8   9 |12 13
18 19 |6   7 |10 11 |14 15
       ------
       20 21
       22 23
'''
# let cube[22] = r, cube[15] = w, cube[18] = b
std_cube = [o, o, o, o,
            y, y, y, y,
            g, g, g, g,
            w, w, w, w,
            b, b, b, b,
            r, r, r, r]

init_cube = [w, g, g, o,
             y, b, b, g,
             y, y, o, w,
             r, g, o, w,
             r, o, b, r,
             y, w, r, b]

def F(c):
    c = c[:]
    c[4], c[5], c[7], c[6] = c[6], c[4], c[5], c[7]
    c[2], c[3], c[8], c[10], c[21], c[20], c[19], c[17] = \
          c[19], c[17], c[2], c[3], c[8], c[10], c[21], c[20]
    return c

def F_(c):
    c = c[:]
    c[6], c[4], c[5], c[7] = c[4], c[5], c[7], c[6]
    c[19], c[17], c[2], c[3], c[8], c[10], c[21], c[20] = \
          c[2], c[3], c[8], c[10], c[21], c[20], c[19], c[17]
    return c

def U(c):
    c = c[:]
    c[0], c[1], c[3], c[2] = c[2], c[0], c[1], c[3]
    c[4], c[5], c[8], c[9], c[12], c[13], c[16], c[17] = \
          c[8], c[9], c[12], c[13], c[16], c[17], c[4], c[5]
    return c

def U_(c):
    c = c[:]
    c[2], c[0], c[1], c[3] = c[0], c[1], c[3], c[2]
    c[8], c[9], c[12], c[13], c[16], c[17], c[4], c[5] = \
          c[4], c[5], c[8], c[9], c[12], c[13], c[16], c[17]
    return c
    
def R(c):
    c = c[:]
    c[8], c[9], c[11], c[10] = c[10], c[8], c[9], c[11]
    c[3], c[1], c[12], c[14], c[23], c[21], c[7], c[5] = \
          c[7], c[5], c[3], c[1], c[12], c[14], c[23], c[21]
    return c

def R_(c):
    c = c[:]
    c[10], c[8], c[9], c[11] = c[8], c[9], c[11], c[10]
    c[7], c[5], c[3], c[1], c[12], c[14], c[23], c[21] = \
          c[3], c[1], c[12], c[14], c[23], c[21], c[7], c[5]
    return c

cube_str = "".join(init_cube)
path = [{cube_str}]
op= {cube_str: []}

std_cube_str = "".join(std_cube)
reverse_path = [{std_cube_str}]
reverse_op= {std_cube_str: []}

found = False

from time import time
start = time()
while 1:
    path.append(set())
    for c in path[-2]:
        for o in F, F_, U, U_, R, R_:
            next_cube = o(list(c))
            next_cube_str = "".join(next_cube)
            if next_cube_str not in op:
                path[-1].add(next_cube_str)
                op[next_cube_str] = op[c] + [{F: 'F', F_: 'F_',
                                              U: 'U', U_: 'U_',
                                              R: 'R', R_: 'R_'}[o]]
            if next_cube_str in reverse_path[-1]:
                t = reverse_op[next_cube_str][::-1]
                for i in range(len(t)):
                    t[i] = {'F': 'F_', 'F_': 'F',
                            'U': 'U_', 'U_': 'U',
                            'R': 'R_', 'R_': 'R'}[t[i]]
                print(op[next_cube_str] + t)
                print(len(path) + len(reverse_path) - 2)
                found = True
                break
        if found:
            break
    if found:
        break

    reverse_path.append(set())
    for c in reverse_path[-2]:
        for o in F, F_, U, U_, R, R_:
            next_cube = o(list(c))
            next_cube_str = "".join(next_cube)
            if next_cube_str not in reverse_op:
                reverse_path[-1].add(next_cube_str)
                reverse_op[next_cube_str] = reverse_op[c] + \
                                            [{F: 'F', F_: 'F_',
                                              U: 'U', U_: 'U_',
                                              R: 'R', R_: 'R_'}[o]]
            if next_cube_str in path[-1]:
                t = reverse_op[next_cube_str][::-1]
                for i in range(len(t)):
                    t[i] = {'F': 'F_', 'F_': 'F',
                            'U': 'U_', 'U_': 'U',
                            'R': 'R_', 'R_': 'R'}[t[i]]
                print(op[next_cube_str] + t)
                print(len(path) + len(reverse_path) - 2)
                found = True
                break
        if found:
            break
    if found:
        break
    
print(time() - start)
