num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

# approach-1 (using two lists)
# def gcd(m,n):
#     fm=[]
#     for i in range(1, m+1):
#         if m%i==0:
#             fm.append(i)
#     fn=[]
#     for j in range(1, n+1):
#         if n%j == 0:
#             fn.append(j)
#     cf=[]
#     for f in fm:
#         if f in fn:
#             cf.append(f)
#     return cf[-1]
# print("The GCD of", num1, "and", num2, "is", gcd(num1,num2))

#approach-2 (using single list)
# def gcd(m,n):
#     cf=[]
#     for i in range(1, min(m,n)+1):
#        if (m%i)==0 and (n%i)==0:
#            cf.append(i)
#     return(cf[-1])
# print("The GCD of", num1, "and", num2, "is", gcd(num1,num2))

#approach-3 (without using lists)
# def gcd(m,n):
#     for i in range(1, min(m,n)+1):
#         if (m%i)==0 and (n%i)==0:
#             mrcf=i
#     return mrcf
# print("The GCD of", num1, "and", num2, "is", gcd(num1,num2))

#approach-4 (scanning backward)
def gcd(m,n):
    i = min(m,n)
    while (i>0):
        if (m%i)==0 and (n%i)==0:
            return i
        else:
            i=i-1
print("The GCD of", num1, "and", num2, "is", gcd(num1,num2))