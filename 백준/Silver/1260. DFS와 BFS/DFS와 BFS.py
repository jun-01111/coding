import sys
from collections import deque

# 1. 초고속 데이터 입력을 위한 파이프라인
input = sys.stdin.readline

def solve():
    # 2. 정점 개수(N), 간선 개수(M), 시작 정점(V)을 받습니다.
    N, M, V = map(int, input().split())
    
    # 3. 빈 지도(인접 리스트)를 만듭니다. 0번 인덱스는 안 쓰니 N+1개!
    graph = [[] for _ in range(N + 1)]
    
    # 4. M개의 줄에 걸쳐 도로 정보를 받아 지도에 그립니다. (양방향 연결)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    # 5. [중요 포인트] 방문할 수 있는 정점이 여러 개면 '작은 번호'부터 가야 합니다!
    # 각 도시마다 연결된 도로의 리스트를 오름차순으로 예쁘게 정렬해 줍니다.
    for i in range(1, N + 1):
        graph[i].sort()
        
    # ---------------------------------------------------------
    # [DFS 무대 세팅]
    # ---------------------------------------------------------
    visited_dfs = [False] * (N + 1)  # DFS 전용 방문 장부
    dfs_result = []                  # DFS 방문 순서를 모아둘 빈 배열
    
    # 6. 쥐구멍 파고들기 마법의 함수!
    def dfs(node):
        # 지금 도착한 곳에 방문 도장을 쾅 찍고, 결과 배열에 이름을 적습니다(문자로 변환).
        visited_dfs[node] = True
        dfs_result.append(str(node))
        
        # 지도를 보고 지금 도시와 연결된 다음 도시들을 차례대로 살펴봅니다.
        for next_node in graph[node]:
            # 만약 그 도시가 장부에 False(안 가봄)로 되어 있다면?
            if not visited_dfs[next_node]:
                # 깊게 파고들어라! 나 자신을 다시 호출합니다.
                dfs(next_node)
                
    # DFS 탐색 시작!
    dfs(V)
    
    # ---------------------------------------------------------
    # [BFS 무대 세팅]
    # ---------------------------------------------------------
    visited_bfs = [False] * (N + 1)  # BFS 전용 깨끗한 방문 장부
    bfs_result = []                  # BFS 방문 순서를 모아둘 빈 배열
    
    # 7. 물결 퍼뜨리기 마법의 함수!
    def bfs(start_node):
        # 양쪽이 뚫린 파이프(대기열)를 만들고 시작점을 넣습니다.
        queue = deque([start_node])
        
        # 시작점에 방문 도장을 쾅 찍습니다.
        visited_bfs[start_node] = True
        
        # 파이프 안에 대기자가 있는 동안 영원히 반복!
        while queue:
            # 파이프 '맨 앞'에서 사람을 꺼냅니다. (이게 큐의 핵심!)
            now = queue.popleft()
            bfs_result.append(str(now)) # 결과 배열에 기록
            
            # 지도를 보고 연결된 다음 도시들을 찾습니다.
            for next_node in graph[now]:
                # 안 가본 도시라면?
                if not visited_bfs[next_node]:
                    # 방문 도장을 미리 찍고, 파이프 '맨 뒤'에 줄을 세웁니다.
                    visited_bfs[next_node] = True
                    queue.append(next_node)
                    
    # BFS 탐색 시작!
    bfs(V)
    
    # 8. 모든 탐색이 끝났습니다. 배열에 모인 결과를 띄어쓰기(" ")로 연결해서 출력!
    print(" ".join(dfs_result))
    print(" ".join(bfs_result))

# 메인 함수 실행
solve()