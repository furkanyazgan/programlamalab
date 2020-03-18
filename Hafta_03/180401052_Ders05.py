

known = {0:0, 1:1}
def fibo_rec(n):
   
    if n in known:
        return known[n]
    else:
        result = fibo_rec(n-1) + fibo_rec(n-2)
        known[n] = result
        return result
        

s = FiniteSet(1, 1.5, Fraction(1, 5), 1, 1.5, 7, 42)
t = FiniteSet(Fraction(1,5), 1, 5, 1, 1, 91, 87) 

for member in s: # Print s set.
    print(member)
    
if s == t:
    print("True")
else:
    print("False")

