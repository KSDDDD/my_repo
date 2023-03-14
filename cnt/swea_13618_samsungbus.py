"""import sys

sys.stdin = open('s_input.txt')
T = int(input())
# N(버스 노선) = 2, A = [1, 2], B = [3, 5]
# 버스 노선 1 = 1, 2, 3 정류장을 거침
# 버스 노선 2 = 2, 3, 4, 5 정류장을 거침
# 출력은 1 2 2 1 1
# P(버스 정류장 갯수) = [5], C = [1,2,3,4,5]
for tc in range(1, T+1):
    N = int(input())
    A, B, C = [], [], []
    for i in range(N):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    P = int(input())
    for j in range(P):
        c = int(input())
        C.append(c)
    D = [0] * P
    for k in range(N):
        for l in range(A[k], B[k]+1):
            D[l-1] += 1
    print(f"#{tc}", *D)"""
import sys

sys.stdin = open('s_input.txt')
T = int(input())
for tc in range(1, T+1):
    bus_num = int(input())
    bus_info = []
    bus_stop = []
    max_stop = 0
    for i in range(bus_num):
        A = list(map(int, input().split()))
        bus_info.append(A)
    P = int(input())
    for k in range(1, P+1):
        c = int(input())
        bus_stop.append(c)
    for j in bus_info:
        if j[1] > max_stop:
            max_stop = j[1]
    all_stop = [0] * (max_stop)
    for i in bus_info:
        for j in range(i[0], i[1]+1):
            if j in bus_stop:
                all_stop[j-1] += 1
    # print(f'#{tc}', *all_stop)
    print(f"#{tc} {' '.join(map(str, all_stop))}")