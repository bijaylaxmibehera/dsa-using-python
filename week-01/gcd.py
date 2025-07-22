num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

def gcd(m,n):
    fm=[]
    for i in range(1, m+1):
        if m%i==0:
            fm.append(i)
    fn=[]
    for j in range(1, n+1):
        if n%j == 0:
            fn.append(j)
    cf=[]
    for f in fm:
        if f in fn:
            cf.append(f)
    return cf[-1]
print("The GCD of", num1, "and", num2, "is", gcd(num1,num2))
