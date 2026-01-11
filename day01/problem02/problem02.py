FILE_NAME = "/home/julieta-murias/advent-of-code-2025/day01/problem02/testInput.txt"            

def get_new_position(pos, action, steps, zeros): 

    if action == "L":
        steps = steps * -1

    original_pos = pos 
    pos += steps


    if action == "L": 
        pass



    if pos == 0: 
        zeros = zeros + 1

    while pos > 99 or pos < 0: 
        pos = pos % 100
        if original_pos != 0: 
            zeros = zeros + 1
    

    return pos, zeros

def solve_problem():
    pos = 50
    zeros = 0

    with open(FILE_NAME) as f:
        for line in f:
            action = line[0:1]
            steps = int(line[1:])

            pos, zeros = get_new_position(pos, action, steps, zeros)

    
    print(zeros)
        
            
solve_problem()

