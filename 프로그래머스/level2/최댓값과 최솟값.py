def solution(s):
    answer = ''
    num_arr = list(map(int,s.split()))
    answer += str(min(num_arr))
    answer += " " + str(max(num_arr))
    return answer

print(solution("-1 -2 -3 -4"))