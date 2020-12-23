"""
내가 짰던 코드
def move(key_position,key,board):
    x, y = key_position
    c_board = board.copy()
    for i in range(len(key)):
        for j in range(len(key)):
            if c_board[i+x][j+y] + key[i][j] > 1:
                return False
            else :
                c_board[i+x][j+y] += key[i][j]
    return c_board

def rotate(key):
    return list(zip(*key[::-1]))

def checkUnlock(c_board,lock_in_board):
    for r1 in lock_in_board:
        for r2 in lock_in_board:
            if c_board[r1][r2] != 1 :
                return False
    return True

def solution(key, lock):
    answer = False
    board = [[0] * (len(key)*2 + len(lock)) for _ in range((len(key)*2 + len(lock))+1)]
    lock_in_board = list(range(len(key),len(key)+len(lock)))
    for i in range(len(lock_in_board)):
        for j in range(len(lock_in_board)):
            board[lock_in_board[i]][lock_in_board[j]] = lock[i][j]
    key_position = [0,0]
    for i in range(len(board)-len(key)):
        for j in range(len(board)-len(key)):
            for _ in range(4):
                key = rotate(key)
                c_board = move(key_position,key,board)
                if c_board:
                    answer = checkUnlock(c_board,lock_in_board)
                if answer :
                    break
            key_position[0] = i
            key_position[1] = j
    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
"""

def rotate90(arr):
    return list(zip(*arr[::-1]))

def check(startX, startY, key, lock, expendSize, start, end):
    expendList = [[0] * expendSize for _ in range(expendSize)]

    # expendList에 key 추가
    for i in range(len(key)):
        for j in range(len(key)):
            expendList[i][j] += lock[i-start][j-start]

    # expendList에 lock 추가하면서 기존 값이랑 더하기
    for i in range(start, end):
        for j in range(start, end):
            expendList[i][j] += lock[i-start][j-start]
            if expendList[i][j] != 1:
                return False
    return True

def solution(key, lock):
    start = len(key) -1 # expendList에서 lock의 시작 지점
    end = start + len(lock) # expendList에서 lock이 끝나는 지점
    expendSize = len(lock) + start * 2 # expendList 배열의 크기

    # lock은 고정이고 key가 움직인다.
    for _ in range(0,4):
        for i in range(end):
            for j in range(end):
                if check(i,j,key,lock,expendSize,start,end):
                    return True
        key = rotate90(key)
    return False
