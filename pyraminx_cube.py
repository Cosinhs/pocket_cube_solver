# -*- coding: utf-8 -*-
r = 'r'
g = 'g'
b = 'b'
y = 'y'

'''
12 13 14 |  0  1  2 | 6  7  8
15 16 17 |  3  4  5 | 9 10 11
         ------------
           18 19 20 
           21 22 23
'''
# let cube[0] to cube[5] = b
std_cube = [b, b, b, b, b, b,
            y, y, y, y, y, y,
            r, r, r, r, r, r,
            g, g, g, g, g, g]

init_cube = [r, y, y, r, b, b,
             r, r, g, y, g, r,
             r, b, b, g, g, g,
             b, y, g, y, y, b]

def B(c):
    c = c[:]
    c[8], c[11], c[10], c[23], c[22], c[21], c[16], c[15], c[12] = \
          c[23], c[22], c[21], c[16], c[15], c[12], c[8], c[11], c[10]
    return c

def B_(c):
    c = c[:]
    c[23], c[22], c[21], c[16], c[15], c[12], c[8], c[11], c[10] = \
          c[8], c[11], c[10], c[23], c[22], c[21], c[16], c[15], c[12]
    return c

def U(c):
    c = c[:]
    c[12], c[13], c[14], c[0], c[1], c[2], c[6], c[7], c[8] = \
           c[0], c[1], c[2], c[6], c[7], c[8], c[12], c[13], c[14]
    return c

def U_(c):
    c = c[:]
    c[0], c[1], c[2], c[6], c[7], c[8], c[12], c[13], c[14] = \
           c[12], c[13], c[14], c[0], c[1], c[2], c[6], c[7], c[8]
    return c

def R(c):
    c = c[:]
    c[2], c[5], c[4], c[19], c[20], c[23], c[10], c[9], c[6] = \
          c[19], c[20], c[23], c[10], c[9], c[6], c[2], c[5], c[4]
    return c

def R_(c):
    c = c[:]
    c[19], c[20], c[23], c[10], c[9], c[6], c[2], c[5], c[4] = \
          c[2], c[5], c[4], c[19], c[20], c[23], c[10], c[9], c[6]
    return c
    
def L(c):
    c = c[:]
    c[0], c[3], c[4], c[19], c[18], c[21], c[16], c[17], c[14] = \
          c[16], c[17], c[14], c[0], c[3], c[4], c[19], c[18], c[21]
    return c

def L_(c):
    c = c[:]
    c[16], c[17], c[14], c[0], c[3], c[4], c[19], c[18], c[21] = \
          c[0], c[3], c[4], c[19], c[18], c[21], c[16], c[17], c[14]
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
        for o in U, U_, B, B_, R, R_, L, L_:
            next_cube = o(list(c))
            next_cube_str = "".join(next_cube)
            if next_cube_str not in op:
                path[-1].add(next_cube_str)
                op[next_cube_str] = op[c] + [{U: 'U', U_: 'U_',
                                              B: 'B', B_: 'B_',
                                              R: 'R', R_: 'R_',
                                              L: 'L', L_: 'L_'}[o]]
            if next_cube_str in reverse_path[-1]:
                t = reverse_op[next_cube_str][::-1]
                for i in range(len(t)):
                    t[i] = {'U': 'U_', 'U_': 'U',
                            'B': 'B_', 'B_': 'B',
                            'R': 'R_', 'R_': 'R',
                            'L': 'L_', 'L_': 'L'}[t[i]]
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
        for o in U, U_, B, B_, R, R_, L, L_:
            next_cube = o(list(c))
            next_cube_str = "".join(next_cube)
            if next_cube_str not in reverse_op:
                reverse_path[-1].add(next_cube_str)
                reverse_op[next_cube_str] = reverse_op[c] + \
                                            [{U: 'U', U_: 'U_',
                                              B: 'B', B_: 'B_',
                                              R: 'R', R_: 'R_',
                                              L: 'L', L_: 'L_'}[o]]
            if next_cube_str in path[-1]:
                t = reverse_op[next_cube_str][::-1]
                for i in range(len(t)):
                    t[i] = {'U': 'U_', 'U_': 'U',
                            'B': 'B_', 'B_': 'B',
                            'R': 'R_', 'R_': 'R',
                            'L': 'L_', 'L_': 'L'}[t[i]]
                print(op[next_cube_str] + t)
                print(len(path) + len(reverse_path) - 2)
                found = True
                break
        if found:
            break
    if found:
        break
    
print(time() - start)
