"""
1. 노란색의 약수를 찾아라
2. 각각 ((약수 + 2 한 값) * 2 -2) == brown
"""
def solution(brown, yellow):
    answer = []
    temp1 = 0
    temp2 = 0
    for i in range(1,int(yellow/2)+2):
        if yellow % i == 0:
            temp1 = (i + 2) * 2 - 2  
            temp2 = (int(yellow/i) + 2) * 2 -2
            if temp1 + temp2 == brown:
                answer.extend([int(yellow/i)+2,i+2])
                break
    return answer

print(solution(24,24))