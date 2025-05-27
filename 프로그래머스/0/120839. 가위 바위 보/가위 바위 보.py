def solution(rsp):
    rsp_dic = {'2': '0', '0': '5', '5': '2'}
    return ''.join([rsp_dic[x] for x in rsp])