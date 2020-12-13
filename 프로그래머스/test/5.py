def solution(penter, pexit, pescape, data):
    answer = ''
    arr = [penter, pexit, pescape]
    n = len(penter)
    answer += penter
    for i in range(int(len(data)/n)):
        if data[n*i:n*i+n] in arr:
            answer += pescape
            answer += data[n*i:n*i+n]
        else :
            answer += data[n*i:n*i+n]
    answer += pexit
    return answer

print(solution("10",	"11",	"00",	"00011011"))