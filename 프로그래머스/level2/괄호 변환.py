"""
내가 푼 방식... 실패 ㅜ 약간 감은 오는데...
def solution(p):
    answer = ''
    w = [] # 0 = (, 1 = )   
    for i in p:
        if i == '(':
            w.append(0)
        else:
            w.append(1)
    print(w)
    answer = step1(w)
    
    return answer
def step1(w):
    print("step1")
    # 1.입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if not w:  
        return w
    else :
        return step2(w)
    
        
def step2(w): 
    print("step2")
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
    # u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    u = []
    v = []
    cnt = 0
    while w :
        if w[0] == 0 :
            cnt -=1
            u.append(w.pop(0))
        else:
            cnt +=1
            u.append(w.pop(0))
        if cnt == 0:
            v.extend(w)
            break
    print(u,v)
    # 3. 올바른 문자열이 아니라면 step4()
    for i in range(0,len(u)-1,2):
        print('sum',sum(u[i:i+2]))
        if sum(u[i:i+2]) != 1: 
            return step4(u,v)
    return step3(u,v)
def step3(u,v):
    print("step3")
    if v :
        print(v)
        return u.extend(step1(v))
    else:
        print("step3",u,v)
        return u

def step4 (u,v):
    print("step4")
    temp = []
    temp.append(0)
    t=step1(v)
    print("t,",t)
    if t : 
        print("v",v)
        temp.extend(t)
        print("temp",temp)
    else : pass
    temp.append(1)
    u.pop(0)
    u.pop()
    for i in range(len(u)):
        if u[i] == 0:
            u[i] = 1
        else:
            u[i] = 0
    print("reverse u",u)
    temp.extend(u)
    print(temp)
    return temp
    
print(solution("()))((()"))
"""
# 문자열 w를 u, v로 분리하는 함수
def divide(w):
    openP = 0
    closeP = 0

    for i in range(len(w)):
        if w[i] == '(':
            openP += 1
        else :
            closeP += 1
        if openP == closeP:
            return w[:i+1], w[i+1:]

# 문자열 u가 올바른 괄호 문자열인지 확인하는 함수
def isBalanced(u):
    stack = []

    for p in u:
        if p == "(":
            stack.append(p)
        else:
            if not stack :
                return False
            stack.pop()
    return True

def solution(w):
    # 1.
    if not w:
        return ''
    
    # 2.
    u, v = divide(w)

    # 3.
    if isBalanced(u):
        # 3-1.
        return u + solution(v)
    # 4.
    else :
        # 4-1.
        answer = '('
        # 4-2.
        answer += solution(v)
        # 4-3.
        answer += ')'
        # 4-4.
        for p in u[1:len(u)-1]:
            if p == '(':
                answer += ')'
            else :
                answer += '('
        # 4-5.
        return answer



