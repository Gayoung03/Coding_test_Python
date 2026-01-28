def solution(a, b):
    answer = 0
    ilist =[]
    
    if a==b:
        return a
    elif b>a:
        for i in range(a,b+1):
            ilist.append(i)
    else: 
        for i in range(b,a+1):
            ilist.append(i)
            
    return sum(ilist)