from itertools import combinations
from collections import deque

def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])
    candidates = []
    for i in range(1,n_col+1):
        candidates.extend(combinations(range(n_col),i))
    final = []
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp)) == n_row:
            final.append(keys)
    answer = set(final[:])
    print(final)
    for i in range(len(final)):
        for j in range(i+1,len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))