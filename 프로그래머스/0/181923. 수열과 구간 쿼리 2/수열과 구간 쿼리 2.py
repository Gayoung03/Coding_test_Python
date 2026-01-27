def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        list_arr = arr[s:e+1]
        
        list_k = []
        for x in list_arr:
            if x > k:
                list_k.append(x)
        
        if not list_k: 
            answer.append(-1)
        else:
            answer.append(min(list_k)) 
            
    return answer