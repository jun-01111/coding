import sys

input = sys.stdin.readline

def solve():
    P = int(input())
    
    for _ in range(P):
        N, M = map(int, input().split())
        
        f1 = 0
        f2 = 1
        
        count = 0
        
        while True:
            next_f = (f1 + f2) % M
            
            f1 = f2
            f2 = next_f
            
            count += 1
            
            if f1 == 0 and f2 == 1:
                break
               
        print(f"{N} {count}")
        
solve()