from itertools import permutations

def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))

def calculate(expression, op):
    cal_tmp = []
    for i in expression:
        if not i in op: # 숫자라면
            if len(cal_tmp) != 0 and not cal_tmp[-1] in op: # 처음 넣는게 아니라면
                cal_tmp[-1] = cal_tmp[-1] + i 
            else :
                cal_tmp.append(i)
        else:
            cal_tmp.append(i)
    result = []
    stack = []
    for o in op:
        while True :
            if len(cal_tmp) == 0:
                break
            tmp = cal_tmp.pop(0)
            if tmp == o:
                stack.append(operation(stack.pop(-1),cal_tmp.pop(0),o))
            else:
                stack.append(tmp)
        result.append(stack)
        cal_tmp = stack
        stack = []
    return result[-1]

def solution(expression):
    op = ['+','-','*']
    op = list(permutations(op,3))
    answer = 0
    for i in op:
        answer = max(answer,abs(int(calculate(expression,i)[0])))
    return answer
