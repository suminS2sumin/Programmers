import re
def solution(myStr):
    answer = []
    sm = re.split("[abc]", myStr)
    sm = [x for x in sm if x != ""]
    if sm == []: return ["EMPTY"]
    return sm