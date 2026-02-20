import sys
import heapq

input = sys.stdin.readline

def solve():
    N = int(input())
    
    left_basket = []
    right_basket = []
    
    for _ in range(N):
        num = int(input())
        
        if len(left_basket) == len(right_basket):
            heapq.heappush(left_basket, -num)
            
        else:
            heapq.heappush(right_basket, num)
            
        if right_basket and -left_basket[0] > right_basket[0]:
            left_boss = -heapq.heappop(left_basket)
            right_boss = heapq.heappop(right_basket)
            
            heapq.heappush(left_basket, -right_boss)
            heapq.heappush(right_basket, left_boss)
            
        print(-left_basket[0])

solve()