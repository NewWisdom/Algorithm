import queue

def solution(v):
    answer = [0,0,0]
    n = len(v)
    chk = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0 and chk[i][j] == 0:
                answer[0] +=1
                bfs([i,j],n,chk,v,0)
            elif v[i][j] == 1 and chk[i][j] == 0:
                answer[1] +=1
                bfs([i,j],n,chk,v,1)
            elif v[i][j] == 2 and chk[i][j] == 0:
                answer[2] +=1
                bfs([i,j],n,chk,v,2)
    return answer

def bfs(start,n,chk,v,m):
    q = queue.Queue()
    q.put(start)
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    chk[start[0]][start[1]] =1
    while not q.empty():
        x, y = q.get()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx>=n or ny < 0 or ny >= n:
                continue
            if chk[nx][ny] == 0  and v[nx][ny] ==m:
                q.put([nx,ny]) 
                chk[nx][ny] = 1

    return 

print(solution([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]))