def solution(q, r, code):
    
    answer = ''
    
    for i in range(len(code)):
        if i%q ==r :
            answer+=(code[i])
    return answer

#나머지를 생각하면.. :: 를 사용해볼 수 있었음
def solution(q, r, code):
    return code[r::q]