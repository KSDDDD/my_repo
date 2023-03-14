import numpy as np
# numpy 수학 라이브러리

a = 1
b = 0
c = -9

coeff = [a,b,c]
lower_x, upper_x = np.roots(coeff)
# round(x, y) : 반올림 함수
# x : 반올림 대상 , y : 자리수
print(round(lower_x, 4), round(upper_x,4))

