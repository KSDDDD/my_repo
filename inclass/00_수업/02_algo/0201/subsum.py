T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    # 구간합의 최댓값
    max_sum = 0
    # 구간합의 최솟값
    min_sum = m * 10000

    # 현재위치 i 를 기준으로 구간을 구한다.
    # i의 범위
    for i in range(n - m + 1):
        # 현재 구간합
        sub_sum = 0
        # 현재위치 i에서 시작해서 m 만큼 가면서 구간합을 구한다.
        # i에서 이동할 칸 수 = j
        # i + j = 구간합을 더하는 위치
        for j in range(m):
            sub_sum += numbers[i + j]

        # 구간합 최대값, 최소값 갱신
        max_sum = sub_sum if sub_sum > max_sum else max_sum
        min_sum = sub_sum if sub_sum < min_sum else min_sum

    print(f"#{tc} {max_sum - min_sum}")
