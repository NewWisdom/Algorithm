"""
문제 설명
앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.
문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.

예를들면, 문자열 s가 abcdcba이면 7을 return하고 abacde이면 3을 return합니다.

제한사항
문자열 s의 길이 : 2,500 이하의 자연수
문자열 s는 알파벳 소문자로만 구성
입출력 예
s	answer
abcdcba	7
abacde	3
입출력 예 설명
입출력 예 #1
4번째자리 'd'를 기준으로 문자열 s 전체가 팰린드롬이 되므로 7을 return합니다.

입출력 예 #2
2번째자리 'b'를 기준으로 aba가 팰린드롬이 되므로 3을 return합니다.
""" 
def solution(s: str):
    def expand(left: int, right: int) -> str:
        # 현재 left, right index가 같은 문자일 경우 윈도우 크기를 좌우로 1씩 넓힌다.
        while left >= 0 and right <= len(s) and s[left] == s[right-1]:
            left -= 1
            right += 1
        return s[left+1:right-1]
    # 연산이 필요없는 경우
    if len(s) < 2 or s == s[::-1]:
        return len(s)
    result = ""
    for i in range(len(s)-1):
        result = max(result, expand(i, i+1), expand(i,i+2), key = len)
    return result
  
print(solution("abcdcba"))