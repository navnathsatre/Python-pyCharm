if __name__ == '__main__':
    nCount = int(input())
    result = []
    for item in range(nCount):
        usrInput = input()
        lstUsrInput, *vals = usrInput.strip().split()
        # "insert 0 7" => ["insert", "0", "7"]
        ops = lstUsrInput[0]
        lstVals = list(map(int, vals))
        if ops == "print":
            print(result)
        elif ops == "insert":
            result.insert(lstVals[0], lstVals[1])
        elif ops == "remove":
            val = int(lstVals[0])
            result.remove(val)
        elif ops == "append":
            val = int(lstVals[0])
            result.append(val)
        elif ops == "sort":
            result.sort()
        elif ops == "pop":
            result.pop()
        elif ops == "reverse":
            result.reverse()
