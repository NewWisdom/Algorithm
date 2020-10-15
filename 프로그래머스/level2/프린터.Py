from collections import deque
def solution(priorities, location):
    answer = 0
    new_p = deque()
    index_arr = deque()
    new_p.extend(priorities)
    temp = []
    index_arr.extend([i for i in range(len(new_p))])
    while new_p:
        cur_max = max(new_p)
        tmp = new_p.popleft()
        if tmp >=cur_max:
            temp.append(index_arr.popleft())
        else :
            index_arr.append(index_arr.popleft())
            new_p.append(tmp)
    answer = temp.index(location)+1
    return answer
