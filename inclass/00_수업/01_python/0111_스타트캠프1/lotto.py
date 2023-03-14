import random

# 로또의 번호 범위는 1 ~ 45 
# 6개만 뽑기
for i in range(6):
    print(f"{i+1}번째 번호 : {random.choice(range(1,46))}")

numbers = range(1,46)

# sample(모음, 갯수)
lotto_nums = random.sample(numbers, 6)

print(lotto_nums)