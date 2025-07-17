from collections import *
def solution(participant, completion):
    human_dic = defaultdict(int)
    answer = ''
    for part in participant:
        human_dic[part] += 1
    
    for com in completion:
        if com in human_dic:
            human_dic[com] -=1
            
            
    for person in human_dic:
        if human_dic[person] >0:
            answer= person
        
    
    return answer


solution(["mislav", "stanko", "mislav", "ana"],  ["stanko", "ana", "mislav"])