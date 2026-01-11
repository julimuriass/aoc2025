from dataclasses import dataclass
from typing import List

FILE_NAME = "/home/julieta-murias/advent-of-code-2025/day01/problem02/input.txt"            


    
def next_pos(current_pos: int, action: str) -> int:
    dir = action[0:1]
    steps = int(action[1:])
    if dir == "L":
        steps = steps * -1
    new_pos = (current_pos + steps) % 100

    #new_pos = current_pos + steps

    if new_pos < 0:
        pass
    elif new_pos > 99:
        pass

    return new_pos

def aoc_01_part1_decode(actions: List[str]):
    count = 0
    pos = 50
    for action in actions:
        pos = next_pos(pos, action)
        if pos == 0:
            count+=1
    return count



class DialCounter():
    def __init__(self):
        self.current_pos = 50
        self.zero_count = 0

    def execute_action(self, action: str):
        dir = action[0:1]
        steps = int(action[1:])
        for _ in range(steps):
            self._move(dir)
            if self.current_pos == 0:
                self.zero_count += 1
    
    def _move(self, dir):
        if dir == "L":
            self.current_pos -= 1
            if self.current_pos < 0:
                self.current_pos = 99
        else:
            self.current_pos += 1
            if self.current_pos > 99:
                self.current_pos = 0      


def aoc_01_part2_decode(actions: List[str]):
    counter = DialCounter()
    for action in actions:
        counter.execute_action(action)
    return counter.zero_count


if __name__ == "__main__":

    # Day 1.
    with open(FILE_NAME) as f:
        lines_day_1 = [line.strip() for line in f.readlines()]

    count_1_1 = aoc_01_part1_decode(actions=lines_day_1)
    count_1_2 = aoc_01_part2_decode(actions=lines_day_1)
    print(count_1_2)
