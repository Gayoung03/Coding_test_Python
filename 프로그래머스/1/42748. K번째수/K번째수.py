def solution(array, commands):
    answer = []
    
    for idx,(i,j,k) in enumerate(commands):
        
        list1 = array[i-1:j]
        list1.sort()
        
        answer.append(list1.pop(k-1))
        
    return answer