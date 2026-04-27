import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve():
    T = int(input())
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def dfs(x, y):
        field[x][y] = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if field[nx][ny] == 1:
                    dfs(nx, ny)
                    
    for _ in range(T):
        M, N, K = map(int, input().split())
        
        field = [[0] * M for _ in range(N)]
        
        for _ in range(K):
            X, Y = map(int, input().split())
            field[Y][X] = 1
            
        worm_count = 0
        
        for i in range(N):
            for j in range(M):
                if field[i][j] == 1:
                    dfs(i, j)
                    worm_count += 1
                    
        print(worm_count)
        
solve()        