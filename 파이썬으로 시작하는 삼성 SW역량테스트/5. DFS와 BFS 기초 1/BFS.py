n, m, v = map(int,input().split())
# 1. 인접 행렬
# 노드 번호가 1부터 n까지이므로 편리함을 위해 n+1로함
# 1번과 2번 노드가 연결되어 있다면 a[1][2], a[2][1]에 1을 입력한다.
a1 = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int,input().split())
    a1[x][y] = 1
    a1[y][x] = 1

for x in a1:
    print(x)

# 2. 인접 리스트
# n+1개의 리스트를 만들어 두고
# 1번과 2번 노드가 연결되어 있다면 1번째 리스트에 2추가, 2번째 리스트에 1 추가
# 정점 번호 작은 순이면 정렬 해주어야 함
a2 = [list() for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split())
    a2[x].append(y)
    a2[y].append(x)
for x in a2:
    x.sort()

# 큐와 방문의 중복을 방지하기 위한 체크배열이 필요하다.
# 체크는 큐에 처음 들어가는 시점에 해준다.
import queue
chk = [False]*(n*1)
q = queue.Queue()
q.put(v)
chk[v] = True