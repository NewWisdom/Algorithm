def solution(s):
    answer = 0
    total = ["" for _ in range(int(len(s)/2)+1)]
    if len(s) == 1: answer =1
    else:
        for i in range(1,int(len(s)/2)+1):
            isExist = False
            per_cnt = 0
            for j in range(0,len(s)+1,i):
                if per_cnt == 0: # 맨 처음
                    temp = s[j:j+i]
                    per_cnt +=1
                elif temp == s[j:j+i]: # 압축 가능하면
                    per_cnt +=1
                else :
                    if per_cnt == 1: # 압축 문자가 1개면 저장하고 초기화
                        total[i]+=temp
                        temp = s[j:j+i]
                        per_cnt = 1
                    else:
                        total[i]+=str(per_cnt)
                        total[i]+=temp
                        temp = s[j:j+i]
                        per_cnt = 1
                        isExist = True
                if j + i > len(s):
                    total[i] += s[j:len(s)]
            if not isExist :
                total[i] = s
        answer = len(total[1])
        if len(total) == 1: pass
        else:
            for i in range(2,len(total)):
                answer = min(answer,len(total[i]))
    return answer
print(solution("abcabcdede"))