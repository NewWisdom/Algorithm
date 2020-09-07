n, m, v = map(int, input().split())
a = [list() for _ in range(n+1)]
for _ in range(m):
    x, y= map(int,input().split())
    a[x].append(y)
    a[y].append(x)

for x in a:
    x.sort()
# 방문한 곳을 중복으로 방문하면 시간초과이니 체크해주어야한다.
chk = [False]*(n+1)

# DFS 는 재귀함수를 통해서 만들어진다.
# node = 방문할 노드 번호
def dfs(node):
    chk[node] = True
    for next in a[node]: # 현재 노드가 갈 수 있는 모든 노드
        if not chk[next]: # 방문하지 않은 노드라면
            dfs(next) # 들어간다.

