array = [('바나나',2),('당근',3),('사과',1)]

def setting(data):
    return data[1]

print(array)
print(array.sort(key=setting))
print(array)