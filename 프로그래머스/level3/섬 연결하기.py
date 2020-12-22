def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2]) # cost 기준으로 오름차순 정렬
    union = [i for i in range(n)]

    for s, d, cost in costs:
        if union[s] != union[d] : # union-find 값이 같으면 이미 연결된 상태이다.
            dest = union[d]
            for i in range(n): # 도착섬과 같은 값들을 모두 시작섬으로 변경
                if union[i] == dest:
                    union[i] = union[s]
            answer += cost # 최저 비용 더하기
            if len(set(union)) == 1:
                break
    return answer
print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	))