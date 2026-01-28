def solution(n):
    answer = 0
    xlist = []
    for i in range (1,n):
        if n%i == 1:
            xlist.append(i)
    answer = min(xlist)
    return answer