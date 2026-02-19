import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    balloons = [int(x) for x in input_data[1:]]

    arrows = [0] * 1000002
    arrow_count = 0

    for h in balloons:
        if arrows[h] > 0:
            arrows[h] -= 1
            arrows[h - 1] += 1

        else:
            arrow_count += 1
            arrows[h - 1] += 1

    print(arrow_count)
    
solve()