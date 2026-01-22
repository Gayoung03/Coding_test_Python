def solution(my_string, overwrite_string, s):
    answer = ''
    
    a = len(overwrite_string)
    my_list = list(my_string)
    
    my_list[s:s+a]=overwrite_string
    
    answer ="".join(my_list)
        
    
    
    return answer