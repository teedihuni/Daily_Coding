def solution(intStrs, k, s, l):
    answer = []
    
    for case in intStrs:
        num = int(case[s:s+l])
        if num > k:
            answer.append(num)
    
    return answer