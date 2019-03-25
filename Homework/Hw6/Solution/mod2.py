def Sum(a,b):
    return int(a)+int(b)
def Fib(n):
    n+=1
    fibo=[0,1]
    if n==0 or n==1:
        return fibo[:n+1]
    for i in range(2,n):
        fibo.append(fibo[-1]+fibo[-2])
    return fibo
