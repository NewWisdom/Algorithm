"""
여행경로
문제 설명
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 ICN 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
입출력 예
tickets	return
[[ICN, JFK], [HND, IAD], [JFK, HND]]	[ICN, JFK, HND, IAD]
[[ICN, SFO], [ICN, ATL], [SFO, ATL], [ATL, ICN], [ATL,SFO]]	[ICN, ATL, ICN, SFO, ATL, SFO]
입출력 예 설명
예제 #1

[ICN, JFK, HND, IAD] 순으로 방문할 수 있습니다.

예제 #2

[ICN, SFO, ATL, ICN, ATL, SFO] 순으로 방문할 수도 있지만 [ICN, ATL, ICN, SFO, ATL, SFO] 가 알파벳 순으로 앞섭니다.
"""
"""
내 풀이 - 테케 1번이 안됨
from collections import deque
def solution(tickets):
    answer = []
    dic = makeDic(tickets)
    answer = bfs(dic)
    return answer

def makeDic(tickets):
    dic = dict()
    for t in tickets:
        if t[0] in dic.keys() :
            dic[t[0]].append(t[1])
        else :
            dic[t[0]] = [t[1]]
    for d in dic.values():
        d.sort()
    return dic

def bfs(dic):
    q = deque()
    q.append("ICN")
    check = []
    while q :
        now = q.popleft()
        check.append(now)
        if now in dic.keys() and dic[now] :
            for i,d in enumerate(dic[now]):
                if d in dic.keys():
                    q.append(dic[now].pop(i))
    for k in dic.keys():
        if dic[k] :
            check.append(dic[k][0])
    return check
"""
def solution(tickets):
    t = dict()
    for ticket in tickets:
        if ticket[0] in t:
            t[ticket[0]].append(ticket[1])
        else :
            t[ticket[0]] = [ticket[1]]
    for k in t.keys():
        t[k].sort(reverse=True)
    st = ["ICN"]
    answer = []
    while st:
        top = st[-1]
        print(st)
        if top not in t or len(t[top]) == 0:
            answer.append(st.pop())
        else :
            st.append(t[top][-1])
            t[top].pop()
    answer.reverse()
    return answer
print(solution([["ICN","A"],["ICN","A"],["A","ICN"]]))