from collections import deque
# 시계방향
dx = deque([0, 1, 0, -1])
dy = deque([-1, 0, 1, 0])
N, M = map(int, input("미로의 크기를 입력하세요. : ").split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input())))
# 미로 모양보기
# for i in maze:
#     print(i)

def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for _ in range(4):
            nx = x + dx[0]
            ny = y + dy[0]
            dx.rotate(-1)
            dy.rotate(-1)

            if (0 <= nx < N and 0 <= ny < M):
                if (maze[nx][ny] == 1):
                    queue.append((nx, ny))
                    maze[nx][ny] = maze[x][y] + 1

if __name__ == '__main__':
    BFS(0, 0)
    print(maze[N - 1][M - 1])
