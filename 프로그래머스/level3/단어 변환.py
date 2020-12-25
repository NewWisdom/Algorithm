"""
단어 변환
문제 설명
두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
예를 들어 begin이 hit, target가 cog, words가 [hot,dot,dog,lot,log,cog]라면 hit -> hot -> dot -> dog -> cog와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

제한사항
각 단어는 알파벳 소문자로만 이루어져 있습니다.
각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
begin과 target은 같지 않습니다.
변환할 수 없는 경우에는 0를 return 합니다.
입출력 예
begin	target	words	return
hit	cog	[hot, dot, dog, lot, log, cog]	4
hit	cog	[hot, dot, dog, lot, log]	0
입출력 예 설명
예제 #1
문제에 나온 예와 같습니다.

예제 #2
target인 cog는 words 안에 없기 때문에 변환할 수 없습니다.
"""
from itertools import combinations
from collections import deque
def solution(begin, target, words):
    def bfs(start):
        count = 0
        q = deque()
        q.append([start,count])
        check[start] = True
        while q :
            now,v = q.popleft()
            for n in arr[now] :
                if check[n] == False:
                    check[n] = True
                    v += 1
                    if n == goal:
                        return v
                    q.append([n,v])
    answer = 0
    if target in words:
        new_words = [begin]
        new_words.extend(words)
        length = len(new_words)
        goal = new_words.index(target)
        arr = [list() for _ in range(length+1)]
        check = [False] * (length + 1)
        com = combinations(new_words,2)
        for c in com:
            if calSimilar(c[0],c[1]) == 1:
                arr[new_words.index(c[0])].append(new_words.index(c[1]))
                arr[new_words.index(c[1])].append(new_words.index(c[0]))
        print(arr)
        answer = bfs(0)
    return answer


def calSimilar(w1,w2):
    count =0
    for i in range(len(w1)):
        if(w1[i] != w2[i]):
            count += 1
    return count

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))