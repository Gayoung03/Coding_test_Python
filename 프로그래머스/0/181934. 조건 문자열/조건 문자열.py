def solution(ineq, eq, n, m):
    answer = 0
    if eq == "!":
        eq =""
    a = str(n)+ineq+eq+str(m)
    b = eval(a)
    if b:
        answer = 1
    else: 0
    
    return answer