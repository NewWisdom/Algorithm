def solution(n, horizontal):
    answer = [[0]*n for _ in range(n)]
    location = []
    location.append([0,0])
    cnt = 0
    isLast = True
    if n == 1:
        answer = [[0]]
    else :
        while location:
            if isLast :
                x, y = location.pop(0)
                if horizontal:
                    cnt +=1
                    y +=1
                    answer[x][y] = cnt
                    while y >0 :
                        y -= 1
                        x += 1
                        cnt += 2
                        answer[x][y] = cnt
                    if x == n-1:
                        isLast = False  
                    location.append([x,y])
                    horizontal = False       
                else:
                    cnt +=1
                    x +=1
                    answer[x][y] = cnt
                    while x >0 :
                        x -= 1
                        y += 1
                        cnt += 2
                        answer[x][y] = cnt
                    if y == n-1:
                        isLast = False
                    else :
                        location.append([x,y])
                        horizontal = True
            else :
                x, y = location.pop(0)
                if x == n-1 :
                    horizontal = True
                else :
                    horizontal = False
                if horizontal:
                    cnt +=1
                    y +=1
                    answer[x][y] = cnt
                    while y < n-1 :
                        y += 1
                        x -= 1
                        cnt += 2
                        answer[x][y] = cnt
                    if x == n-1 and y == n-1:
                        break    
                    location.append([x,y])
                    horizontal = False       
                else:
                    cnt +=1
                    x +=1
                    answer[x][y] = cnt
                    while x < n-1 :
                        x += 1
                        y -= 1
                        cnt += 2
                        answer[x][y] = cnt
                    if y == n-1 and x == n-1:
                        break
                    else :
                        location.append([x,y])
                        horizontal = True
    return answer

print(solution(1,True))
