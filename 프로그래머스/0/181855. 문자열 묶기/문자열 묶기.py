from collections import defaultdict

def solution(strArr):
    groups = defaultdict(list)
    for i in strArr:
        groups[len(i)].append(i)
    
    return max(len(groups) for groups in groups.values())