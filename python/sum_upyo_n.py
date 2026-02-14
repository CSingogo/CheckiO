
#Calculate sum of integers from 1 to given N (including).

def sum_upto_n(N: int) -> int:
    # your code here
    if N == 1: return 1
    num = 0
    for x in range(1,N+1):
        num = num + x
    return num

