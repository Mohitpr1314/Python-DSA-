# sum of n number
def sumN(n):
    if n==0:
        return 0
    return n + sumN(n-1)

# print(sumN(10))
# sum of n odd number

def sumOdd(n):
    if n == 0:
        return 0
    return (2*n-1) + sumOdd(n-1)
# print(sumOdd(10))
# sum of even number

def sumEven(n):
    if n == 0:
        return 0
    return 2*n + sumEven(n-1)
# print(sumEven(10))

# factorial of n number

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)
# print(fact(10))

# sum of n squre number

def sumSqr(n):
    if n==0:
        return 0
    return n*n + sumSqr(n-1)

print(sumSqr(10))
