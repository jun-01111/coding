import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    
    mod = 1000000
    
    p = 1500000
    
    target = n % p
    
    if target == 0:
        print(0)
        return
    elif target == 1:
        print(1)
        return
    
    f0 = 0
    f1 = 1
    
    for _ in range(target - 1):
        
        f0, f1 = f1, (f0 + f1) % mod
        
    print(f1)
    
solve()