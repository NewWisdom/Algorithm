"""
문제 설명
두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

제한사항
각 단어는 알파벳 소문자로만 이루어져 있습니다.
각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
begin과 target은 같지 않습니다.
변환할 수 없는 경우에는 0를 return 합니다.
입출력 예
begin	target	words	return
"hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
"hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	0
입출력 예 설명
예제 #1
문제에 나온 예와 같습니다.

예제 #2
target인 "cog"는 words 안에 없기 때문에 변환할 수 없습니다.
"""
from collections import deque

def check(s, begin):
    answer = 0 
    # 일치하는지 안일치하는지 검증
    for i in range(len(s)):
        if list(s)[i] != list(begin)[i]:
            answer += 1
    return True if answer == 1 else False

def solution(begin, target, words):
    answer = 0
    if not target in words:
        return 0
    
    queue = deque() 
    queue.append([begin, []])

    while queue:
        n, l = queue.popleft()
        for word in words:
            # 경로에 없으면서 1개만 일치할 때
            if word not in l and check(word, n):
                if word == target:
                    return len(l) + 1
                tmp = l[0:]
                tmp.append(word)
                queue.append([word, tmp])
                print(n, l)

    return answer

def solution2(begin, target, words):
    if not target in words:
        return 0

    answer = 0
    word_len = len(begin)
    word_list = [begin]
    diff_word = list()

    while(1):
        for wl in word_list:
            diff_word.clear()
            for word in words:
                diff = 0
                for idx in range(0, word_len):
                    if wl[idx] != word[idx]: diff += 1
                    if diff > 1: break
                if diff == 1:
                    diff_word.append(word)
                    words.remove(word)
        answer += 1
        if target in diff_word: return answer
        else : word_list = diff_word

print(solution2("hit", "cog"	, ["hot", "dot", "dog", "lot", "log", "cog"]))
# https://muhly.tistory.com/86
# https://moseory20.tistory.com/31
"""
1. 변환할 수 없는 경우의 예외처리를 먼저 수행한다.

2. 기준이 될 현재 단어들을 word_list에 저장하며 words에서 word_list들과 비교했을 때 한 글자만 다른 글자들을 차례대로 찾는다. word_list는 begin 단어로 초기화하고 시작한다.

3. word_list와 한 글자만 다른 글자들을 찾아 diff_word에 삽입하고 words에서 삭제한다. 
모든 word_list와 수행한 후,
- diff_word에 target이 있다면 바로 answer(begin부터 한 글자씩 달라질 때마다 +1)를 반환한다. 
- diff_word에 target이 없다면 다음 턴에 비교할 현재 단어 리스트(word_list)를 diff_word로 치환하고 2번을 반복한다.
"""