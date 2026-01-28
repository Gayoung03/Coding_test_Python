def solution(arr, divisor):
    answer = []
    list1 =[]
    
    for i in arr:
        if  i %divisor == 0:
            list1.append(i)
            
    if len(list1) == 0:
        list1.append(-1)
        
    list1.sort()        
    return list1