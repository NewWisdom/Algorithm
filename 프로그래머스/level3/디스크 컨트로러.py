import heapq

def solution(jobs):
    count, last, answer = 0, -1, 0
    heap =[]
    # 들어온 시간 순서대로 정렬
    jobs.sort(key=lambda x: x[0])
    # 시작시간 초기화
    time = jobs[0][0]
    while count < len(jobs):
        for s, t in jobs:
            if last < s <= time:
                # 작업 소요 시간으로 min heap을 만들기 위해 (t, s) 푸시
                heapq.heappush(heap,(t,s))
        # 바로 수행할 수 있는 작업이 있는 경우
        if len(heap) > 0:
            count += 1
            last = time
            # term은 구간
            term, start = heapq.heappop(heap)
            # time은 끝난 시간
            time += term
            answer += (time - start)
        # 바로 수행할 수 있는 작업이 없는 경우
        else:
            time += 1
        print(last, time, term, start)
    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))