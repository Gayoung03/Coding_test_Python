def solution(numLog):
    answer = ''
    list1 =[]
    for i in range(len(numLog)-1):
        if (numLog[i+1]-numLog[i]) == 1:
            list1.append("w")
        elif (numLog[i+1]-numLog[i]) == -1:
            list1.append("s")
        elif (numLog[i+1]-numLog[i]) == 10:
            list1.append("d")
        else:
            list1.append("a")
            
        
    return "".join(list1)