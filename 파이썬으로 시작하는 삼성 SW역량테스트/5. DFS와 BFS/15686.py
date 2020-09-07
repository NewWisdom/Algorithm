"""
치킨 배달 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	512 MB	26790	12136	6771	40.816%
문제
크기가 N×N인 도시가 있다. 도시는 1×1크기의 칸으로 나누어져 있다. 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다. 도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다.

이 도시에 사는 사람들은 치킨을 매우 좋아한다. 따라서, 사람들은 "치킨 거리"라는 말을 주로 사용한다. 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다. 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.

예를 들어, 아래와 같은 지도를 갖는 도시를 살펴보자.

0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 1 2
0은 빈 칸, 1은 집, 2는 치킨집이다.

(2, 1)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |2-1| + |1-2| = 2, (5, 5)에 있는 치킨집과의 거리는 |2-5| + |1-5| = 7이다. 따라서, (2, 1)에 있는 집의 치킨 거리는 2이다.

(5, 4)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |5-1| + |4-2| = 6, (5, 5)에 있는 치킨집과의 거리는 |5-5| + |4-5| = 1이다. 따라서, (5, 4)에 있는 집의 치킨 거리는 1이다.

이 도시에 있는 치킨집은 모두 같은 프랜차이즈이다. 프렌차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을 폐업시키려고 한다. 오랜 연구 끝에 이 도시에서 가장 수익을 많이 낼 수 있는  치킨집의 개수는 최대 M개라는 사실을 알아내었다.

도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다. 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.

둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.

도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다. 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

출력
첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.

예제 입력 1 
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
예제 출력 1 
5
예제 입력 2 
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
예제 출력 2 
10
예제 입력 3 
5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
예제 출력 3 
11
예제 입력 4 
5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
예제 출력 4 
32
"""
## 내가 풀다 포기...ㅎ
# import sys, queue
# from itertools import combinations
# input = lambda : sys.stdin.readline().strip()

# n, m = map(int,input().split())
# city = [list(map(int,input().split())) for _ in range(n)]

# house = [[i,j] for i in range(n) for j in range(n) if city[i][j] == 1]
# chicken = [[i,j] for i in range(n) for j in range(n) if city[i][j] ==2]

# com = list(combinations(chicken,m))


# print(com)
# min_cost = 10000000
# total_cost = 0
# def bfs(start,chicken):
#     chk = [[0]*n for _ in range(n)]
#     dx = [-1,0,0,1]
#     dy = [0,-1,1,0]
#     q = queue.Queue()
#     q.put(start)
#     while not q.empty():
#         x, y = q.get()
#         chk[x][y] = 1
#         if x == chicken[0] and y == chicken[1]:
#             print("abs",abs(start[0]-x)+abs(start[1]-y))
#             return abs(start[0]-x)+abs(start[1]-y)
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if 0<=nx<n and 0<=ny<n and chk[nx][ny] == 0 :
#                 q.put([nx,ny])

# print("house",house)
# h_arr = [list() for _ in range(len(house))]
# h_min_cost = 100000000000
# total_min = 1000000000000
# for tp in com:  
#     for t in tp:
#         h_min_cost = 0
#         print("chicke",t)
#         for i,h in enumerate(house):
#             h_arr[i].append(bfs(h,t))
#     print(h_arr)
#     for a in h_arr:
#         print("min a",min(a))
#         h_min_cost += min(a)
#     total_min = min(total_min,h_min_cost)
# print(total_min)

from itertools import combinations

n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

home = [[i,j] for i in range(n) for j in range(n) if a[i][j] == 1]
chicken = [[i,j] for i in range(n) for j in range(n) if a[i][j] ==2]

chi_list = list(combinations(chicken,m))

def calc_dist(h,chicken_list):
    min_dist = 1000000000
    for chi in chicken_list:
        dist = abs(chi[0]-h[0]) + abs(chi[1]-h[1])
        min_dist = min(min_dist,dist)
    return min_dist

ans = []
for chi in chi_list:
    total = 0
    for h in home:
        total +=calc_dist(h,chi)
    ans.append(total)

print(min(ans))