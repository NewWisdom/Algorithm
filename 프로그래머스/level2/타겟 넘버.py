# def solution(numbers, target):
#     answer = 0
#     for i in range(len(numbers)+1):
#         op = []
#         op.extend('+' for _ in range(i))
#         op.extend('-' for _ in range(len(numbers)-i))
#         per = list(set(permutations(numbers,len(numbers))))
#         print(per)
#         for p in per:
#             p = list(p)
#             for j in range(len(op)):
#                 if op[j] == '+':
#                     p[j] = +p[j]
#                 else:
#                     p[j] = -p[j]
#             if target == sum(p):
#                 answer+= (1 * len(numbers))                
#     return answer

# print(solution([1, 1, 1, 3, 1],	3))

"""
dfs로 쉽게 풀 수 있는 문제였다..!
"""
def solution(numbers, target):
    answer = 0
    sup = [0]
    for i in numbers:
        sub = []
        for j in sup:
            sub.append(j+i)
            sub.append(j-i)
        sup = sub
    answer = sup.count(target)
    return answer

print(solution([1, 1, 1, 1, 1],	3))