"""
나이트의 이동 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	18477	8545	6480	45.759%
문제
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?



입력
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력
각 테스트 케이스마다 나이트가 몇 번만에 이동할 수 있는지 출력한다.

예제 입력 1 
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
예제 출력 1 
5
28
0
"""
from collections import deque
n = int(input())

def bfs(start_x,start_y):
    q = deque()
    q.append([start_x,start_y])
    ch[start_x][start_y] = 1
    dx = [-2,-2,-1,-1,1,1,2,2]
    dy = [-1,1,-2,2,-2,2,-1,1]
    while q:
        x, y =q.popleft()
        if x== move_x and y ==move_y: 
            print(ch[move_x][move_y]-1)
            return
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<l and 0<=ny<l and ch[nx][ny] == 0:
                q.append([nx,ny])
                ch[nx][ny] = ch[x][y]+1


for _ in range(n):
    l = int(input())
    now_x, now_y = map(int,input().split())
    move_x,move_y = map(int,input().split())
    ch = [[0]*l for _ in range(l)]
    bfs(now_x,now_y)

    

     