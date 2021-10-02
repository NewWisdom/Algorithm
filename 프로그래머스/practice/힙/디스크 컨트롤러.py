"""
문제 설명
하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.

예를들어

- 0ms 시점에 3ms가 소요되는 A작업 요청
- 1ms 시점에 9ms가 소요되는 B작업 요청
- 2ms 시점에 6ms가 소요되는 C작업 요청
와 같은 요청이 들어왔습니다. 이를 그림으로 표현하면 아래와 같습니다.
Screen Shot 2018-09-13 at 6.34.58 PM.png

한 번에 하나의 요청만을 수행할 수 있기 때문에 각각의 작업을 요청받은 순서대로 처리하면 다음과 같이 처리 됩니다.
Screen Shot 2018-09-13 at 6.38.52 PM.png

- A: 3ms 시점에 작업 완료 (요청에서 종료까지 : 3ms)
- B: 1ms부터 대기하다가, 3ms 시점에 작업을 시작해서 12ms 시점에 작업 완료(요청에서 종료까지 : 11ms)
- C: 2ms부터 대기하다가, 12ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 16ms)
이 때 각 작업의 요청부터 종료까지 걸린 시간의 평균은 10ms(= (3 + 11 + 16) / 3)가 됩니다.

하지만 A → C → B 순서대로 처리하면
Screen Shot 2018-09-13 at 6.41.42 PM.png

- A: 3ms 시점에 작업 완료(요청에서 종료까지 : 3ms)
- C: 2ms부터 대기하다가, 3ms 시점에 작업을 시작해서 9ms 시점에 작업 완료(요청에서 종료까지 : 7ms)
- B: 1ms부터 대기하다가, 9ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 17ms)
이렇게 A → C → B의 순서로 처리하면 각 작업의 요청부터 종료까지 걸린 시간의 평균은 9ms(= (3 + 7 + 17) / 3)가 됩니다.

각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)

제한 사항
jobs의 길이는 1 이상 500 이하입니다.
jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.
입출력 예
jobs	return
[[0, 3], [1, 9], [2, 6]]	9
입출력 예 설명
문제에 주어진 예와 같습니다.

0ms 시점에 3ms 걸리는 작업 요청이 들어옵니다.
1ms 시점에 9ms 걸리는 작업 요청이 들어옵니다.
2ms 시점에 6ms 걸리는 작업 요청이 들어옵니다.
"""
 # simple
def solution(jobs):
    answer, start, now = 0, 0, 0
    re_job = sorted(jobs, key=lambda x : x[1])
    while re_job:
        can = False
        for i, j in enumerate(re_job):
            if j[0] <= now:
                answer += now + j[1] - j[0]
                now += j[1]
                re_job.pop(i)
                can = True

                break
        if re_job and not can :  
            now +=1
    return answer // len(jobs)

#heapq
import heapq

def solution_heap(jobs):
    answer = 0
    # jobs의 최소힙
    jobs_heap = []
    # 시작 시간, 처음에는 -1 ~ 0 범위의 작업을 찾아야하므로 -1로 초기화
    start = -1
    # 현재 시간
    now = 0
    # 완료된 작업 수
    complited_jobs = 0
    # 작업의 수
    jobs_ea = len(jobs)
    # 모든 작업을 완료할 때 까지 실행
    while complited_jobs < jobs_ea:
        # 주어진 작업을 하나씩 접근
        for job in jobs:
            # 작업을 입력받은 시점이 시작 시간과 현재 시간의 사이인 경우
            if start < job[0] <= now:
                # jobs_heap에 push (최소힙)
                # 0번 인덱스를 기준으로 정렬되므로 0번 인덱스에 작업 처리 시간을 입력
                heapq.heappush(jobs_heap, [job[1], job[0]])
        # 최소힙에 작업이 들어와 있으면
        if jobs_heap:
            # 최소힙으로부터 최소 시간 작업 꺼내기
            min_job = heapq.heappop(jobs_heap)
            # 시작 시간에 현재 시간 입력
            start = now
            # 현재 시간에 최소 시간 작업을 처리한 시간 입력
            now += min_job[0]
            # answer에 현재 시간 - 최소 시간 작업을 입력받은 시점 입력
            answer += now - min_job[1]
            # 작업을 처리하였으므로 +1
            complited_jobs += 1
        # 최소힙에 아무것도 없어도 현재시간은 흘러야 하므로 +1
        else:
            now += 1

    return answer//jobs_ea
                
## heap 참고자료 https://littlefoxdiary.tistory.com/3
            

print(solution([[0, 3], [1, 9], [2, 6]]))