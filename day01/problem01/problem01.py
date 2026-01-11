FILE_NAME = "/home/julieta-murias/advent-of-code-2025/day01/problem01/input.txt"            

def get_new_position(pos, action, steps) -> int: 

    if action == "L":
        steps = steps * -1
        
    pos += steps
    pos = pos % 100

    return pos

def solve_problem():
    pos = 50
    zeros = 0

    with open(FILE_NAME) as f:
        for line in f:
            action = line[0:1]
            steps = int(line[1:])

            pos = get_new_position(pos, action, steps)
            
            if pos == 0: zeros += 1
    
    print(zeros)
        
            
solve_problem()

