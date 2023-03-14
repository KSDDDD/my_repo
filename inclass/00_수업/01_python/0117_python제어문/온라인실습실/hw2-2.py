orders = "아메리카노,핫초코,라떼,딸기딜라이트"

print(len(orders.split(",")))

orders = ["아메리카노", "핫초코", "라떼", "딸기딜라이트", "딸기딜라이트", "딸기딜라이트"]

# 중복을 제거하기 위해서 리스트를 세트로 변환
set_orders = set(orders)
# 정렬을 위해 시퀀스형 데이터인 리스트로 변환
list_orders = list(set_orders)

# sorted(정렬대상, 내림차순여부)
print(sorted(list_orders, reverse=True))


