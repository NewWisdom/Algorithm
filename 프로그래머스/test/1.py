def solution(grades, weights, threshold):
    answer = -1234567890
    grade_list = {"A+":10, "A0":9,"B+":8, "B0":7, "C+":6, "C0":5, "D+":4, "D0":3, "F":0 }
    print(grade_list["A+"])
    grade_sum = 0
    for i,g in enumerate(grades):
        grade_sum += grade_list[g] * weights[i]
    answer = grade_sum - threshold

    return answer

print(solution(["A+","D+","F","C0"],	[2,5,10,3],	50))