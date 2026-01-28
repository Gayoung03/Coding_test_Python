def solution(n):
    answer = 0
    sn = str(n)
    
    nlist = sorted(str(sn), reverse=True)
    n2 = "".join(nlist)
    
    return int(n2)