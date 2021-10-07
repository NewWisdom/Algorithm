"""
문제 설명
도둑이 어느 마을을 털 계획을 하고 있습니다. 이 마을의 모든 집들은 아래 그림과 같이 동그랗게 배치되어 있습니다.

image.png

각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.

각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.

제한사항
이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.
money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.
입출력 예
money	return
[1, 2, 3, 1]	4
"""
def solution(money):
    answer = 0
    # 첫집을 무조건 터는 경우
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, len(money)-1): 
        dp1[i] = max(dp1[i-1], money[i] + dp1[i-2])
    
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    # 마지막 집을 무조건 터는 경우
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], money[i] + dp2[i-2])
    
    return max(max(dp1), max(dp2))

print(solution([1, 2, 3, 1]	))

"""
https://velog.io/@imacoolgirlyo/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8F%84%EB%91%91%EC%A7%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC
집이 1개일 경우 - 무조건 그 집
집이 2개일 경우 - 두 집 중 더 큰집
집이 3개일 경우 - 현재 i 집 money + i-2 번째 집 money 혹은 i-1집 money 중 더 큰 값 (dp[i] = max(dp[i-1], money[i]+ dp[i-2]))
하지만 첫 집, 마지막 집은 연결되어 있으므로 다음과 같은 경우도 생각해보아야 한다.
1) 첫 번째 집을 무조건 털고, 마지막 집은 털지 않는 경우
2) 마지막 집을 무조건 털고 첫 번째 집은 털지 않는 경우
로 나눠서 생각해야 한다.
"""