def solution(n, board):
    answer = 0
    location = [list() for _ in range(n*n+1)]
    location[0] = [0,0]
    for i in range(n):
        for j in range(n):
            location[board[i][j]] = [i,j]
    # print(location)

    for i in range(len(location)-1):
        x_min = min(abs(location[i][0]-location[i+1][0]), abs(n - (abs(location[i][0]-location[i+1][0]))))
        y_min = min(abs(location[i][1]-location[i+1][1]), abs(n - (abs(location[i][1]-location[i+1][1]))))
        answer += x_min + y_min +1
        # print(answer)
    return answer

print(solution(3,[[3, 5, 6], [9, 2, 7], [4, 1, 8]]))