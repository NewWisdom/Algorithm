import math
def solution(progresses, speeds):
    answer = []
    # 작업별 완료되기까지 걸리는 시간 zip은 동일한 크기의 배열을 묶어주는 역할
    progresses = [math.ceil((100-a)/b) for a, b in zip(progresses, speeds)] 
    front = 0
    for i in range(len(progresses)):
        # 맨 앞(front) 남은 기간보다 길게 걸리는지
        if progresses[front] < progresses[i]:
            answer.append(i-front)
            front = i # 맨 앞이 됨
    answer.append(len(progresses)-front)
    return answer
