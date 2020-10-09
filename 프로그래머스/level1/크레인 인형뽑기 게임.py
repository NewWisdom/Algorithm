from collections import deque
def solution(board, moves):
    answer = 0
    leng = len(board)
    busket = []
    new_board = [deque() for _ in range(leng+1)]
    for i in range(leng):
        for j in range(leng):
            if board[i][j] != 0:
                new_board[j+1].append(board[i][j])
    for i in moves:
        if new_board[i]:
            cur = new_board[i].popleft()
            if busket and busket[-1] == cur:
                answer +=2
                busket.pop()
            else : 
                busket.append(cur)
        
        
    return answer