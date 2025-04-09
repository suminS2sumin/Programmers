def solution(myString, pat):
    position = myString.rfind(pat) # rfind 뒤에서부터 탐색
    return myString[0:position+len(pat)]