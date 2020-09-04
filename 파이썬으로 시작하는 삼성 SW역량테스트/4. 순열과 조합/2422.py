"""
문제
한윤정과 친구들은 이탈리아로 방학 여행을 갔다. 이탈리아는 덥다. 윤정이와 친구들은 아이스크림을 사먹기로 했다. 아이스크림 가게에는 N종류의 아이스크림이 있다. 모든 아이스크림은 1부터 N까지 번호가 매겨져있다. 어떤 종류의 아이스크림을 함께먹으면, 맛이 아주 형편없어진다. 따라서 윤정이는 이러한 경우를 피하면서 아이스크림을 3가지 선택하려고 한다. 이때, 선택하는 방법이 몇 가지인지 구하려고 한다.

입력
첫째 줄에 정수 N과 M이 주어진다. N은 아이스크림 종류의 수이고, M은 섞어먹으면 안 되는 조합의 개수이다. 아래 M개의 줄에는 섞어먹으면 안 되는 조합의 번호가 주어진다. 같은 조합은 두 번 이상 나오지 않는다. (1 ≤ N ≤ 200, 0 ≤ M ≤ 10,000)

출력
첫째 줄에, 가능한 방법이 총 몇 개 있는지 출력한다.

예제 입력 1 
5 3
1 2
3 4
1 3
예제 출력 1 
3
힌트
5개의 아이스크림과 3가지 섞어먹으면 안 되는 조합이 있다. 1번은 2번 3번과 섞으면 안되고, 3번은 4번과 섞으면 안 된다. 따라서 (1 4 5), (2 3 5), (2 4 5)와 같이 3가지 방법이 있다.
"""
from itertools import combinations
import sys
input = lambda : sys.stdin.readline().strip()
# cnt = 0
# no_com = [list(map(int,input().split())) for _ in range(m)]
# for com in map(list,combinations(range(1,n+1),3)):
#     isPrint = True
#     for no in no_com:
#         if no[0] in com and no[1] in com:
#             isPrint = False
#             break
#     if isPrint :
#         cnt+=1
# print(cnt)

n, m = map(int,input().split())
ice = list(combinations(range(1,n+1),3))
no_ice = [[0]*(n+1) for _ in range(n+1)] # 아이스크림 종류 수 만큼 n * n 배열을 만들어주고 

for i in range(m):
    x,y= map(int,input().split())
    # 맛 없는 조합을 인덱스로 삼아 1을 대입한다.
    no_ice[x][y] = 1
    no_ice[y][x] =1
ans = 0
for i in ice:
    # 아이스크림 조합 3자리를 2개씩 묶어서 맛없는 조합에 있는지 찾는다.
    if no_ice[i[0]][i[1]] or no_ice[i[1]][i[2]] or no_ice[i[2]][i[0]]:
        continue
    ans +=1
print(ans)
