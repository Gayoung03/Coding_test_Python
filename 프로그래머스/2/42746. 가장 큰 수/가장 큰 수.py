def solution(numbers):
    strlist = list(map(str, numbers))
    
    strlist.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(strlist)))