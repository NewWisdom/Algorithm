# # 최대 공약수
# def getGCD(a,b):
#     c = max(a,b)
#     d = min(a,b)

#     while True:
#         if c % d == 0:
#             break
#         c, d = d, c%d
#     return d
# # 최대 공배수
# def getLCM(a,b):
#     return a * b / getGCD(a,b)

# def solution(arr):
#     answer = 0
#     while True:
#         arr.append(getLCM(arr.pop(),arr.pop()))
#         if len(arr) == 1:
#             break
#     answer = arr[0]
#     return answer

def lcs(a, b):
    if a % b == 0:
        return b
    else:
        return lcs(b,(a%b))

def solution(arr):
    answer = 1
    for i in arr:
        answer = (answer * i) / lcs(answer,i)
    return int(answer)
print(solution([2,6,8,14]))