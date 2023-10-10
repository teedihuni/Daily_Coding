def solution(my_strings, parts):
    
    answer = "".join([my_strings[idx][x:y+1] for idx,[x,y] in enumerate(parts)])
        
    return answer


#''.join([x[y[0]:y[1]+1] for x,y in zip(my_strings, parts)])
