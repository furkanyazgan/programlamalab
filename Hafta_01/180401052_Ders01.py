def power_i(a,b):  
    if b == 0:
        return 1
    if b == 1:
        return a
    m = 1
    for i in range(b):
        m *= a
    return m

def power_ii(a,b): 
    if b == 0:
        return 1
    if b == 1:
        return a
    if b > 1:
        if b % 2 == 0:
            return power_ii(a*a, b/2)
        return power_ii(a*a, int(b/2))*a
        #return power_ii(a, b-1)*a



def findMaxRange_i(inlist=[4, -3, 5, -2, -1, 2, 6, -2]):
    max = 0
    for i in range(len(inlist)):
        for j in range(i+1, len(inlist)):
            # print(i, j)
            t = 0
            for k in range(i,j+1):
                t = t + inlist[k]
            if t > max:
                max = t
                i_1, i_2 = i, j
    return max , i_1, i_2

def findMaxRange_ii(inlist=[4, -3, 5, -2, -1, 2, 6, -2]):  
    max = 0
    for i in range(len(inlist)):
        t = 0
        for j in range(i, len(inlist)):
            t = t + inlist[j]
            if t > max:
                max = t
                i_1, i_2 = i, j
    return max , i_1, i_2
