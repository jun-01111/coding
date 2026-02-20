import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    N = int(input_data[0])
    M = int(input_data[1])
    
    S = set(input_data[2 : 2+N])
    
    queries = input_data[2+N :]
    
    count = 0
    
    for q in queries:
        if q in S:
            count += 1
            
    print(count)
    
solve()