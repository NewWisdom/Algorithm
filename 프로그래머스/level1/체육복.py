def solution(n, lost, reserve):
    answer = 0
    set_r = set(reserve) - set(lost)
    set_l = set(lost) - set(reserve)
    # 왼쪽 학생부터 빌려주기
    for i in set_r:
        if i-1 in set_l:
            set_l.remove(i-1)
        elif i+1 in set_l:
            set_l.remove(i+1)
    answer = n - len(set_l)
    return answer
