from itertools import permutations
def solution(numbers):
    answer = []
    numbers = list(numbers)
    for i in range(1,len(numbers)+1):
        per = list(permutations(numbers,i))
        per = set(per)
        for p in per:
            isPrime = True
            p = int("".join(p))
            if p == 1 or p ==0 : 
                isPrime = False
                continue
            for i in range(2,p):
                if p % i == 0 : 
                    isPrime = False
                    break
            if isPrime:
                answer.append(p)
    answer = set(answer)
    return len(answer)

print(solution("9"))