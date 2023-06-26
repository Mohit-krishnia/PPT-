def index_find(string):
    d = {}
    for i in range(len(string)):
        if string[i] in d:
            d[string[i]] += 1
        else:
            d[string[i]] = 1
    for i in range(len(string)):
        if d[string[i]] == 1:
            return i
    return -1

print(index_find('aabb'))
