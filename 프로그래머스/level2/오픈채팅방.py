def solution(record):
    result = []
    changeNicknameRecord = dict()

    for oneRecord in record:

        recordSplit = oneRecord.split()
        command = recordSplit[0]
        uid = recordSplit[1]

        if command == "Enter":
            nickname = recordSplit[2]
            changeNicknameRecord[uid] = nickname

            result.append(["님이 들어왔습니다.", uid])

        elif command == "Leave":
            result.append(["님이 나갔습니다.", uid])

        elif command == "Change":

            nickname = recordSplit[2]
            changeNicknameRecord[uid] = nickname

    for oneResult in result:
        oneResult[0] = changeNicknameRecord[oneResult[1]] + oneResult[0]

    result = [oneResult[0] for oneResult in result]

    return result



if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

    print(solution(record))
