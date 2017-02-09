def main():
    intList = {}
    ints = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]

    for myInt in ints:
        if myInt in intList.keys():
            intList[myInt] += 1
        else:
            intList[myInt] = 1

    for key,value in intList.items():
        if value == 1:
            print (key)
    
main()
