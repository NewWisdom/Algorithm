"""
1. 두 수험자가 푼 문제 수가 같다. 단, 푼 문제 수가 5 미만인 경우는 제외한다.
2. 두 수험자가 푼 문제의 번호가 모두 같다.
3. 두 수험자가 푼 문제의 점수가 모두 같다.
"""
from itertools import combinations
def solution(logs):
    answer = []
    num_arr = [list() for _ in range(10)] # 문제 번호
    score_arr = [list() for _ in range(10)]
    per = []
    for i,l in enumerate(logs):
        temp = list(l.split())
        if temp[0] not in per :
            per.append(temp[0])
        if temp[1] in num_arr[per.index(temp[0])] : # 재시도로 푼 문제면
            tmp_num = num_arr[per.index(temp[0])].index(temp[1])
            num_arr[per.index(temp[0])][tmp_num] = temp[1]
            score_arr[per.index(temp[0])][tmp_num] = temp[2]
        else:
            num_arr[per.index(temp[0])].append(temp[1])
            score_arr[per.index(temp[0])].append(temp[2])
    com = list(combinations(range(len(per)),2))
   
    for c in com :
        # 1. 두 수험자가 푼 문제 수가 같다. 단, 푼 문제 수가 5 미만인 경우는 제외한다.
        isNot = False
        if len(num_arr[c[0]]) == len(num_arr[c[1]]) and len(num_arr[c[0]]) >= 5:
            # 2. 두 수험자가 푼 문제의 번호가 모두 같다.
            for num1 in num_arr[c[0]]:
                if num1 not in num_arr[c[1]] :
                    isNot = True
                    break
                # 3. 두 수험자가 푼 문제의 점수가 모두 같다.
                if score_arr[c[0]][num_arr[c[0]].index(num1)] != score_arr[c[1]][num_arr[c[1]].index(num1)]:
                    isNot = True
                if isNot:
                    break
            if isNot:
                continue
            answer.append(per[c[0]])
            answer.append(per[c[1]])
    if answer :
        answer = list(set(answer))
        answer.sort()
    else:
        answer.append("None")
    return answer

print(solution(["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "2001 1 100", "2001 2 100", "2001 4 100", "2001 7 95", "2001 9 100", "2002 1 95", "2002 2 100", "2002 4 100", "2002 7 100", "2002 9 100"]))