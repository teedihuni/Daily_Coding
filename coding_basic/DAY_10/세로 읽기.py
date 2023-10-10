def solution(my_string, m, c):
    string = [my_string[i:i+m] for i in range(0,len(my_string),m)]
    
    answer = [string[i][c-1] for i in range(len(string))]
    
    return ''.join(answer)

# ::를 사용해서 더 쉽게 풀 수 있었음..
def solution(s, m, c):
    return s[c-1::m]