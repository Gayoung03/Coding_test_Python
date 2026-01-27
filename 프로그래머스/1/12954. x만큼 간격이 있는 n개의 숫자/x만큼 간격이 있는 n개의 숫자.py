def solution(x, n):
    answer = []
    last = x*n
    for i in range(1,n+1):
        num = i*x
        answer.append(num)
        
    return answer