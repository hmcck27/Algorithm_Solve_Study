def solution(id_list, report, k):
    answer = []

    # 중복 제거
    report = set(report)

    reportedList = [oneReport.split()[1] for oneReport in report]
    suspendedList = []
    for id in id_list:
        if reportedList.count(id) >= k:
            suspendedList.append(id)

    answer = [0 for _ in id_list]
    for oneReport in report:
        if oneReport.split()[1] in suspendedList:
            answer[id_list.index(oneReport.split()[0])] += 1

    return answer

if __name__ == "__main__":
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2

    id_list = ["con", "ryan"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 3

    print(solution(id_list, report, k))