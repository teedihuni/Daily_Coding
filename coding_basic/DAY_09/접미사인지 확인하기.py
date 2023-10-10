# 문제에서 주어진 제한 사항에서 my_string이 100개 이하였기 때문에 if in을 사용
def solution(my_string, is_suffix):
    answer = [my_string[i:] for i in range(len(my_string))]
        
    if is_suffix in answer:
        return 1
    else:
        return 0 
    

# 만약 길이가 엄청 길었다면..?





