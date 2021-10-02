"""
문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.
입출력 예
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
※ 공지 - 2019년 2월 28일 지문이 리뉴얼되었습니다.
"""
# simple
def solution(prices):
    answer = []
    answer = [0 for _ in range(len(prices))]
    
    for i in range(len(prices)):
        for j in range(i +1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else : 
                answer[i] += 1
                break
    return answer

# stack
def solution_stack(prices):
    answer = [0] * len(prices)
    # 인덱스를 넣어놓을 스택
    stack = []

    for i, p in enumerate(prices):
        # 스택이 비어있지 않고, 비교하는 값보다 스택의 마지막(비교)의 인덱스에 해당하는 값이 더 크면. 즉 가격이 떨어지면 
        while stack and p < prices[stack[-1]]:
            print(i, p, stack)
            # 가격이 떨어지는 시점이니 해당 인덱스에 값을 넣기 위해 pop
            tmp = stack.pop()
            answer[i] = i - tmp # 가격이 떨어지는 현재 시점에서 해당 인덱스 pop
        stack.append(i)
    
    while stack:
        j = stack.pop()
        answer[j] = len(prices) -1 -j
    return answer

def test(prices):
    answer = [0] * len(prices)
    stack = []
    for i, p in enumerate(prices):
        while stack and p < prices[stack[-1]]:
            tmp = stack.pop()
            answer[i] = i - tmp
        stack.append(i)
    
    while stack:
        tmp = stack.pop()
        answer[tmp] = len(prices) - 1 - tmp
    return answer

print(test([1, 2, 3, 2, 3]))

