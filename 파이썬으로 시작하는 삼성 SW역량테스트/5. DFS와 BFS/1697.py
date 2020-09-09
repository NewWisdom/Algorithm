"""
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4
"""
"""
<내가 생각한 풀이>
일단 구할 수 있는 최소 시간은 걷기만 했을 때 abs(k-n)이다.
최대한 순간이동을 해야 빠르게 갈 수 있으므로
현재 위치에서 순간 이동한 값 - 동생 위치 < min_n이면 순간이동한다.?
아니면 현재 위치에서 걸은 값 - 동생 위치 < min_n이면 걷는다.
그리고 왔던 곳은 다시 와봐야 소용 없으니 chk하자.
"""

import sys
from collections import deque
input = lambda:sys.stdin.readline().strip()

chk = [0]* 100001
n, k = map(int,input().split())

chk[n] = 1 # 현재 위치
min_cnt = abs(n-k)
cnt = 0

q = deque()
q.append([0,n])
d = [-1,1,2] # 갈 수 있는 방향
while q:
    cnt, x = q.popleft()
    if x == k : break
    if cnt > min_cnt : continue # min_cnt보다 크면 그냥 가지마
    for i in range(3):  
        if i ==2:
            nx = x*d[2]
        else : nx =x +d[i]  
        if 0<=nx<=100000 and chk[nx] ==0:
            q.append([cnt+1,nx])
            chk[nx] =1
print(cnt)