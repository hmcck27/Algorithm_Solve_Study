from itertools import combinations

def solution(relation):
    answer = 0

    indexSet = set(range(len(relation[0])))
    cList = list()
    for i in range(1, len(relation[0]) + 1):
        c = combinations(indexSet, i)
        for comb in c:
            cList.append(set(comb))

    l = sorted(cList, key=lambda x: len(x))
    m = len(relation)
    n = len(relation[0])

    while len(l) != 0:
        pop = l[0]
        l,flag =  popCheck(pop, l,m, relation)
        if flag == True:
            answer += 1



    return answer

def popCheck(pop, l, m, relation):

    for i in range(m-1):
        testComb = [relation[i][p] for p in pop]
        for j in range(i+1, m):
            if testComb == [relation[j][p] for p in pop] :
                return l[1:], False

    # 다 통과 했으니까 l에서 지우기

    i = 0
    rmIndexSet = set()
    for i in range(len(l)):
        if l[i].issuperset(pop):
            rmIndexSet.add(i)

    newList = list()
    for i in range(len(l)):
        if i not in rmIndexSet:
            newList.append(l[i])

    return newList, True




if __name__ == "__main__":
    relation = [["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","4"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]]
    print(solution(relation))