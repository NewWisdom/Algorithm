def solution(answers):
    answer = []
    per1 = [1,2,3,4,5]*2000
    per2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    per3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if per1[i] == answers[i] : cnt[0]+=1
        if per2[i] == answers[i] : cnt[1]+=1
        if per3[i] == answers[i] : cnt[2]+=1
    for i in range(len(cnt)):
        if cnt[i] == max(cnt) : answer.append(i+1)
    return answer