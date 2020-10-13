def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    answer.sort()
    if not answer : answer.append(-1)
    return answer