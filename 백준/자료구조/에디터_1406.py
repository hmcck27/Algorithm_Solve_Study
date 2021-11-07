import sys



word_list = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())
commands = list()
Editor = editor()

for i in range(len(word_list)):
    Editor.words.append(word_list[i])
Editor.cursorPos = len(word_list)

for i in range(n):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "P":
        Editor.plusWord(command[1])
    elif command[0] == "L":
        Editor.moveCursorLeft()
    elif command[0] == "D":
        Editor.moveCursorRight()
    else:
        Editor.removeWord()


print("".join(Editor.words))