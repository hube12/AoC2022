for l in [4,14]:
 with open("../Download/input22_6.txt") as f:
    buffer=f.readline().rstrip()
    pattern_len=l
    current=[]
    are_distinct=False
    for i,c in enumerate(buffer):
        if len(current)<pattern_len:
            current.append(c)
            continue
        else:
            current.pop(0)
            current.append(c)
        are_distinct=len(set(current))==len(current)
        if are_distinct:
            print(i+1)
            break
