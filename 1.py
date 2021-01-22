def solution(n, delivery):
    answer = ''
    is_del = ["?"] * (n+1)
    for d in delivery :
        if d[2] == 1:
            is_del[d[0]] = "O"
            is_del[d[1]] = "O"
    for d in delivery:
        if d[2] == 1 : # 배송 되었다면
            is_del[d[0]] = "O"
            is_del[d[1]] = "O"
        else: # 배송 안됐다면
            if is_del[d[0]] == '?' or is_del[d[1]] == '?':
                if is_del[d[0]] =='O':
                    is_del[d[1]] = 'X'
                elif is_del[d[1]] == 'O':
                    is_del[d[0]] = "X"
                elif is_del[d[0]] =='X':
                    pass
                elif is_del[d[1]] == "X":
                    pass


            else :
                if is_del[d[0]] == "O":
                    is_del[d[1]] ="X"
                elif is_del[d[1]] == "O":
                    is_del[d[0]] = 'X'
        # print(is_del)
    is_del.pop(0)
    answer = "".join(is_del)
    return answer

print(solution(	7, [[5, 6, 0], [1, 3, 1], [1, 5, 0], [7, 6, 0], [3, 7, 1], [2, 5, 0]]))