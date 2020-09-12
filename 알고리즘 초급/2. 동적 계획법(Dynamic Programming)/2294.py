"""
동전 2 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초 (추가 시간 없음)	128 MB	34279	10013	6879	28.138%
문제
n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다. 가치가 같은 동전이 여러 번 주어질 수도 있다.

출력
첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.

예제 입력 1 
3 15
1
5
12
예제 출력 1 
3
"""
# n,k = map(int,input().split())
# arr = [int(input()) for _ in range(n)]
# dp = [0]*(k+1)
# for i,v in enumerate(arr):
#     if v <= k :
#         dp[v] = 1

# for i in range(1,k+1):
#     for j,v in enumerate(arr):
#         if 0 <= i-v < k+1 and dp[i-v] !=-1:
#             if dp[i] == 0 :
#                 dp[i] = dp[i-v]+1
#             else: 
#                 dp[i] = min(dp[i],dp[i-v]+1)
#         else:
#             dp[i] = -1
# if dp[k] == 0 : dp[k] = -1

# print(dp[k])

n,k = map(int,input().split())
dp = [0 for _ in range(k+1)]
c = [int(input()) for _ in range(n)]

for i in range(1,k+1): # k까지
    a=[]
    for j in c: # 동전 하나하나
        if j<=i and dp[i-j]!=-1: # 동전 가치가 만들 수 있는 수보다 작거나 같고, 이 동전을 넣기 전 가치가 만들 수 없는 경우가 아니라면
            a.append(dp[i-j])
    if not a:
        dp[i] = -1 # 만들 수 없음
    else :
        dp[i] = min(a) +1
print(dp[k])