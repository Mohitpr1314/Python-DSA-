# print n number

def printN(n):
    if n>0:
        printN(n-1)
        print(n, end = ' ')

# printN(10)
# print n number in reverse order

def printNrev(n):
    if n>0:
        print(n, end = ' ')
        printNrev(n-1)
# printNrev(10)
# print n odd number

def printNodd(n):
    if n>0:
        printNodd(n-1)
        print(2*n -1, end = ' ')
# printNodd(10)
# print evev number

def printNeven(n):
    if n>0:
        printNeven(n-1)
        print(2*n , end = ' ')
# printNeven(10)
# print even number in reverse order

def printNevenRev(n):
    if n>0:
        print(2*n, end = ' ')
        printNevenRev(n-1)
# printNevenRev(10)
# prnit odd number in reverse order

def printNoddRev(n):
    if n>0:
        print(2*n-1, end = ' ')
        printNoddRev(n-1)

printNoddRev(10)