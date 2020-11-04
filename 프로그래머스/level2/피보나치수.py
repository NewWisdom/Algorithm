def solution(n):
    answer = 0
    pb = [0 for _ in range(100001)]
    pb[1] = 1
    if n == 1:
        answer = pb[n] % 1234567
    else:
        for i in range(2,n+1):
            pb[i] = pb[i-2] + pb[i-1]
        answer = pb[n] % 1234567
    return answer