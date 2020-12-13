def solution(n, horizontal):
    # 처음으로 움직이는 방향이 오른쪽인지 여부를 나타내는 진리값 horizontal
    answer = [[0]*n for _ in range(n)]
    # cnt_arr = [0]
    # path = []
    # path.append([0,0])
    # while path:
    #     x,y = path.pop(0)
    #     cnt = cnt_arr.pop(0)
    #     if location[0] == 0 or location[1] == 0:
    #         if horizontal :
    #             answer[x][y+1] = cnt
    #             while y >=0:
    #                 y -= 1
    #                 path.append([x+1,y])
    #                 cnt_arr.append(cnt+=2)
    #         else:
    #             answer[x+1][y] = cnt
    #             while x >= 0:
    #                 x -= 1
    #                 path.append([x,y+1])
    #                 cnt_arr.append(cnt+=2)
    # for i in range(n): # 위아래
    #     for j in range(n): # 왼쪽 오른쪽
    #         if i == 0 or i == n-1 or j == 0 or j == n-1:
    #             if horizontal :
    #                 cnt += 1
    #                 answer[i][j+1] = cnt
    #             else :
    #                 cnt +=1 
    #                 answer[i+1][j] = cnt
    x = 0
    y = 0
    cnt = 1
    while x < n and y <n :
        if horizontal :
            answer[x][y+1] = cnt
            while y >0:
                y -= 1
                x += 1
                cnt += 2
                answer[x,y] = cnt
            location = [x][y]
            horizontal = False
        else:
            answer[x+1][y] = cnt
            while x > 0:
                x -= 1
                y += 1
                cnt += 2
                path.append([x,y])
                answer[x,y] = cnt
            location = [x][y]
            horizontal = True
    return answer


print(solution(4,True))