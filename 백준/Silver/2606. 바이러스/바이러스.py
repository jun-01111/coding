import sys

input = sys.stdin.readline

def solve():
    N = int(input())
    M = int(input())
    
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * (N + 1)
    
    def dfs(computer):
        visited[computer] = True
        
        for next_comp in graph[computer]:
            if visited[next_comp] == False:
                dfs(next_comp)
    dfs(1)
    
    total_infected = sum(visited)
    
    print(total_infected - 1)
    
solve()