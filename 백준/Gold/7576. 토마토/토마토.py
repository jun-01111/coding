import sys
from collections import deque

input = sys.stdin.readline

def solve():
    # 1. M(가로/열), N(세로/행)을 입력받습니다.
    M, N = map(int, input().split())
    
    # 2. 토마토 창고를 나타낼 2차원 리스트와, BFS를 위한 큐를 준비합니다.
    box = []
    queue = deque()
    
    # 3. 창고의 상태를 한 줄씩 입력받으며 세팅합니다.
    for i in range(N):
        row = list(map(int, input().split()))
        box.append(row)
        
        # 4. [핵심] 입력받은 줄(row)을 훑어보면서, 익은 토마토(1)가 있다면
        # 큐에 그 위치(i, j)를 미리 모두 넣어둡니다! (동시 출발을 위해)
        for j in range(M):
            if row[j] == 1:
                queue.append((i, j))
                
    # 5. 상, 하, 좌, 우 방향을 나타내는 좌표입니다.
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 6. BFS 시작! 큐가 빌 때까지 반복합니다.
    while queue:
        # 7. 큐의 맨 앞에서 익은 토마토의 위치를 꺼냅니다.
        x, y = queue.popleft()
        
        # 8. 꺼낸 토마토의 상하좌우를 확인합니다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 9. 다음 위치가 창고 범위 안쪽이고,
            if 0 <= nx < N and 0 <= ny < M:
                # 10. 그곳에 아직 안 익은 토마토(0)가 있다면?
                if box[nx][ny] == 0:
                    # 11. 토마토를 익게 만들고, 현재 토마토의 날짜 값에 1을 더해 덮어씌웁니다.
                    box[nx][ny] = box[x][y] + 1
                    # 12. 방금 익은 토마토도 내일은 주변을 익게 만들 테니 큐에 넣습니다.
                    queue.append((nx, ny))

    # 13. 모든 토마토가 익었는지 확인하고, 걸린 날짜를 계산할 차례입니다.
    max_days = 0
    
    for row in box:
        for tomato in row:
            # 14. 창고를 다 훑었는데 아직도 안 익은 토마토(0)가 남아있다면?
            # -> 벽(-1)에 가로막혀 영원히 익을 수 없는 상태입니다.
            if tomato == 0:
                print(-1)
                return # 프로그램을 즉시 종료합니다.
                
            # 15. 가장 큰 값(가장 오래 걸린 날짜)을 찾아 갱신합니다.
            max_days = max(max_days, tomato)
            
    # 16. [주의] 처음에 익은 토마토를 1부터 시작했으므로, 
    # 실제 걸린 일수는 마지막 값에서 1을 빼주어야 합니다.
    print(max_days - 1)

# 메인 함수 실행
solve()