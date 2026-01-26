def solution(num_list):
    answer = 0
    
    odd="".join([str(x) for x in num_list if x % 2 != 0])
    even = "".join([str(x) for x in num_list if x % 2 == 0])
    
    answer = eval(odd)+eval(even)
    return answer