def solution(a, b):
    answer = 0
    
    num1 = int(str(a)+str(b))
    num2 = a*b*2
    
    if num1>=num2:
        answer = num1
    else:
        answer = num2
    return answer