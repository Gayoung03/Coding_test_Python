def solution(n):
    answer = 0
    list1=[]
    if (n&1) == 1:
        for i in range(1,n+2,2):
            list1.append(i)
        answer = sum(list1)
    else:
        for i in range(2,n+2,2):
            list1.append(i**2)
        answer = sum(list1)
        
    return answer