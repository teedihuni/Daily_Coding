def solution(my_string, is_prefix):
    answer = [my_string[:i] for i in range(len(my_string))]
    
    if is_prefix in answer:
        return 1
    else:
        return 0


#다른 사람의 풀이 (startswith 사용)
def solution(my_string, is_prefix):
     return int(my_string.startswith(is_prefix))