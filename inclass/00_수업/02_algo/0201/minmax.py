T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    
    # 최솟값
    min_num = 1000000
    # 최댓값
    max_num = 0
    
    # 반복을 돌면서 최댓값, 최솟값 갱신하기
    for i in range(n):
        max_num = numbers[i] if max_num < numbers[i] else max_num
        min_num = numbers[i] if min_num > numbers[i] else min_num

    answer = max_num - min_num
    print(f"#{tc} {answer}")

