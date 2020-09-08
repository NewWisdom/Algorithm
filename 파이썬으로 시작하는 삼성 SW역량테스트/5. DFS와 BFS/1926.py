"""
그림 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	4260	1912	1380	43.837%
문제
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

입력
첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

출력
첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

예제 입력 1 
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
예제 출력 1 
4
9
"""
"""
<내가 생각한 풀이>

"""
import queue

n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
chk = [[0]*m for _ in range(n)]
max_pic = 0
cnt_pic = 0



def bfs(start):
    q = queue.Queue()
    cnt = 1
    q.put(start)
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    chk[start[0]][start[1]] =1
    while not q.empty():
        x, y = q.get()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx>=n or ny < 0 or ny >= m:
                continue
            if chk[nx][ny] == 0  and a[nx][ny] ==1:
                q.put([nx,ny]) 
                chk[nx][ny] = 1
                cnt +=1   
    return cnt

for i in range(n):
    for j in range(m):
        if a[i][j] == 1 and chk[i][j] == 0:
            cnt_pic +=1
            max_pic = max(max_pic,bfs([i,j]))

print(cnt_pic)
print(max_pic)