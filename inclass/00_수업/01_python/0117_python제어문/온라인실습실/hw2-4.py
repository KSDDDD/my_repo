orders = ["아메리카노", "핫초코", "라떼", "딸기딜라이트", "딸기딜라이트", "딸기딜라이트"]


# 1. "딸기"가 들어간 메뉴를 총 몇번 주문했는지
# count("문자열")
# 해당 문자열에서 단어가 몇번 나오는지 횟수를 세준다.
orders = "아이스아메리카노,핫초코,아이스라떼,딸기딜라이트,딸기딜라이트,딸기딜라이트"

print(orders.count("아이스"))

# find("문자열")
# 문자열이 시작되는 index 찾아서 반환
orders = ["아메리카노", "핫초코", "라떼", "딸기딜라이트", "딸기딜라이트", "딸기딜라이트"]

cnt = 0
for order in orders:
    if order.find("딸기") >= 0:
        cnt+=1

print(cnt)

orders_dict = {} # 빈 딕셔너리를 생성 dict()
# 리스트를 순회하면서 메뉴를 확인
for order in orders:
    # order 가 내가 만든 딕셔너리의 키에 포함되어 있지 않다면 => 지금까지 한번도 등장한적 없는 메뉴
    # 그 order에 매칭되는 값을 0으로 초기화
    # key = 메뉴이름 , value = 주문건수
    if order not in orders_dict.keys():
        orders_dict[order] = 0
    # order 가 내가 만든 딕셔너리의 키에 포함되어 있다 => 이전에 등장한 메뉴
    orders_dict[order] += 1

print(orders_dict)


