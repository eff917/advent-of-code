from copy import deepcopy
filename = '2020/dec17/input.txt'
filename = '2020/dec17/input-example.txt'
init_state = {}
init_state[0] = {}
with open(filename, 'r') as infile:
    for line_index, line in enumerate(infile):
        line  = list(line.strip())
        init_state[0][line_index] = {}
        for cube_index, cube in enumerate(line):
            init_state[0][line_index][cube_index] = cube

for plane_id, plane in init_state.items():
    print(f"Plane: z={plane_id}")
    for line_id, line in plane.items():
        print(f"Line: y={line_id} {line}")

prev_state = deepcopy(init_state)
next_state = deepcopy(init_state)

# boot
next_state[min(prev_state.keys())-1] = {}
next_state[max(prev_state.keys())+2] = {}
for z_index in range(min(prev_state.keys()) - 1, max(prev_state.keys()) + 2):
    for y_index in range(min(prev_state[z_index].keys()) - 1, max(prev_state[z_index].keys()) + 2):
        for x_index in range(min(prev_state[z_index][y_index]) -1 , max(prev_state[z_index][y_index]) +2 ):
            pass
