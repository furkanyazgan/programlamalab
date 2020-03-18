 power_i(a,b):   
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
