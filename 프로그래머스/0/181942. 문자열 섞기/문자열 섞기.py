def solution(str1, str2):
    answer = ''
    list1 = list(str1)
    list2 = list(str2)
    
    list3=[]
    for i in range(len(list1)):
                   list3.append(list1[i])
                   list3.append(list2[i])
    answer = "".join(list3)
    return answer