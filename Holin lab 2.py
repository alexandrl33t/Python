def RAND(a,b,m,x_i):
    return (a * x_i + b) % m

a = 22695477 
b = 1
m = pow(2,32)

x0 = 1
A = 0
B = 10
N = 10**2

RNumsArr = []
#для N^2
RParamsArr_e2 = []
RNumsArr.append(RAND(a,b,m,x0))

for i in range(1,N-1):
    RNumsArr.append(RAND(a,b,m,RNumsArr[i-1]))

for i in range(0,N-1):
    RNumsArr[i] = RNumsArr[i]/m
    RParamsArr_e2.append(A + (B-A) * RNumsArr[i])

M_e2 = sum(RParamsArr_e2)/N

D_e2 = sum_2/N - pow(M_e2,2) * N/(N-1)


#для N^3

















