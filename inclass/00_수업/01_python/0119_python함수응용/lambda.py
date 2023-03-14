
# 람다 함수
# = 익명함수
# 한번 사용하고 버릴떄

v = (lambda x: x*x)(4)
print(v)

# 나중에 또 사용하려면 변수에 람다함수 저장
my_lambda = lambda x: x*x

print(my_lambda(4))

# sorted(key, reverse)
# key => 정렬 기준 (함수)

# 딕셔너리를 정렬
# 딕셔너리를 비시퀀스형이라서 순서가 의미가 없다.
# 순서가 없는데 정렬을 어떻게해여
# 시퀀스가 있는 형태로 바꿔서 정렬을 한다.
# items()

등수 = {"홍경환" : 2, "이정현" : 1, "김재만" : 3}
print(등수.items())
print(sorted(등수.items(), key=lambda x: x[1]))

def key_f(x):
    return x[1]

print(sorted(등수.items(), key=key_f))