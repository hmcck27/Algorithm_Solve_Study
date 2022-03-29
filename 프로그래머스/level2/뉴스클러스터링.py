import re

def solution(str1, str2):
    str1List = []
    str2List = []

    str1 = str1.upper()
    str2 = str2.upper()

    # 쌍 구성
    for i in range(0,len(str1)-1,1):
        if ('a' <= str1[i] <= "z" or 'A' <= str1[i] <= "Z") and ('a' <= str1[i+1] <= "z" or 'A' <= str1[i+1] <= "Z"):
            str1List.append(str1[i] + str1[i+1])
    for i in range(0,len(str2)-1,1):
        if ('a' <= str2[i] <= "z" or 'A' <= str2[i] <= "Z") and ('a' <= str2[i + 1] <= "z" or 'A' <= str2[i+1] <= "Z"):
            str2List.append(str2[i] + str2[i+1])



    temp1 = str1List.copy()
    temp2 = str2List.copy()


    # 합집합 구하기
    unionDict1 = dict()
    unionDict2 = dict()

    for c1 in temp1:
        if c1 in unionDict1.keys():
            unionDict1[c1] += 1
        else:
            unionDict1[c1] = 1

    for c2 in temp2:
        if c2 in unionDict2.keys():
            unionDict2[c2] += 1
        else:
            unionDict2[c2] = 1

    unionDictMax = dict()
    setList1 = set(unionDict1.keys())
    setList2 = set(unionDict2.keys())
    setFinal = setList1.union(setList2)

    unionDictMin = dict()

    for key in setFinal:
        if key in setList1 and key in setList2:
            unionDictMax[key] = max(unionDict1[key], unionDict2[key])
            unionDictMin[key] = min(unionDict1[key], unionDict2[key])
        elif key in setList1:
            unionDictMax[key] = unionDict1[key]
        else:
            unionDictMax[key] = unionDict2[key]


    union = 0
    for key in unionDictMax:
        union += unionDictMax[key]
    intersect = 0
    for key in unionDictMin:
        intersect += unionDictMin[key]

    if intersect ==0 and union == 0:
        return 65536
    return int((float(intersect)/float(union))*65536)





if __name__ == "__main__":

    # str1 = "handshake"
    # str2 = "shake hands"

    str1 = "handshake"
    str2 = "shake hands"

    str1 = "aa1+aa2"
    str2 = "AAAA12"

    # str1 = "E=M*C^2"
    # str2 = "e=m*c^2"

    print(solution(str1, str2))