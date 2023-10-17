def solution(arr):
    
    two_index=[]
    answer=[]
        
    for i in range(len(arr)):
        if arr[i]==2:
            two_index.append(i)
            
    if two_index :
        answer = arr[two_index[0]:two_index[-1]+1]
    else:
        answer =[-1]
        
    return answer