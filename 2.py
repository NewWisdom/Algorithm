# def rotate(l, n):
#     return l[n:] + l[:n]
# def solution(encrypted_text, key, rotation):
#     answer = ''
#     alpha = [0]
#     alpha_str = 'abcdefghijklmnopqrstuvwxyz'
#     alpha.extend(list(alpha_str))
#     encrypted_text = list(encrypted_text)
#     key = list(key)
#     for i,v in enumerate(encrypted_text):
#         index = alpha.index(v)
#         print(index -i)
#         if index - i < len(alpha) - 1:
#             encrypted_text[i] = alpha[index - i-1]
#         else:
#             encrypted_text[i] = alpha[i-index-len(alpha)+2]
#     print(encrypted_text) 
#     for i in range(rotation):
#         encrypted_text = rotate(encrypted_text,1)
#     answer = "".join(encrypted_text)
#     return answer

def rotate(l, n):
    return l[n:] + l[:n]
def solution(encrypted_text, key, rotation):
    answer = ''
    alpha = [0]
    alpha_str = 'abcdefghijklmnopqrstuvwxyz'
    alpha.extend(list(alpha_str))
    encrypted_text = list(encrypted_text)
    key = list(key)
    for i,v in enumerate(encrypted_text):
        index = alpha.index(v)
        if 0 <= i - index:
            encrypted_text[i] = alpha[i-index]
        else:
            encrypted_text[i] = alpha[i-index+len(alpha)]
        
    for i in range(rotation):
        encrypted_text = rotate(encrypted_text,1)
    answer = "".join(encrypted_text)
    return answer

print(solution("qyyigoptvfb",	"abcdefghijk",	3))