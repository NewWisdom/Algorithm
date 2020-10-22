def solution(number, k):
    answer = ""
    s = []
    for n in number:
        while s and s[-1] < n and k>0:
            s.pop()
            k-=1
        s.append(n)
    while k > 0:
        s.pop()
        k-=1
    answer = "".join(s)
    
    return answer

print(solution("1231234",3))