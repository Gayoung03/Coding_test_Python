def solution(n):
    answer = 0
    list1 = []
    for i in range(1,n+1):
        if n%i ==0:
            list1.append(i)
    return sum(list1)