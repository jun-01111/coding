import sys

def solve():
    N = int(sys.stdin.readline())
    
    low = 1
    high = N
    
    while low <=high:
        mid = (low + high) // 2
        
        mid_squared = mid * mid
        
        if mid_squared == N:
            print(mid)
            break
            
        elif mid_squared < N:
            low = mid + 1
            
        else:
            high = mid - 1
            
solve()