def solution(clothes):
    answer = 1
    clothes_name = [list() for i in range(30)]
    clothes_type = []
    for c in clothes : 
        if c[1] not in clothes_type :
            clothes_type.append(c[1])
        clothes_name[clothes_type.index(c[1])].append(c[0])
    for c in clothes_name:
        answer *= (len(c) +1)
    answer -=1
    return answer

print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))

