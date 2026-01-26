def solution(num_list):
    answer = 0
    x = 1
    xx = sum(num_list) **2
    
    for i in num_list:
        x*=i
        
    if x< xx:
        answer = 1
    else: answer = 0
    
    return answer