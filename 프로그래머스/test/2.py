def solution(s, op):
    answer = []
    for i in range(len(s)-1):
        num1 = int(s[0:i+1])
        num2 = int(s[i+1:len(s)])
        if op == '+':
            answer.append(num1+num2)
        elif op == '-':
            answer.append(num1-num2)
        elif op == '*':
            answer.append(num1* num2)

    return answer

print(solution("1234","+"))