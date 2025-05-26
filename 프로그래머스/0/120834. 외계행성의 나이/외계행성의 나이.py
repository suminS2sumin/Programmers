def solution(age):
    age_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    age = str(age)
    return "".join([age_list[int(age[i])] for i in range(len(age))])
        