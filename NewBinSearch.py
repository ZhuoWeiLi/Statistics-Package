def binSearch(ls, key, lf = None, rt = None, numRec = 0):
    if ls is None:
        return "List doesn't exist."
    if ls == []:
        return "List is empty."

    if rt is None: rt = len(ls)-1
    if lf is None: lf = 0

    if key <= ls[lf]: return lf

    elif key > ls[rt]: return None

    mid = (lf+rt)//2    
    midVal = ls[mid]

    if midVal == key:
        return mid

    elif key < midVal:

        if ls[mid-1] < key:
            return mid

        return binSearch(ls, key, lf, mid-1)

    else:

        if ls[mid+1] >= key:
            return mid+1

        return binSearch(ls,key,mid+1, rt)


