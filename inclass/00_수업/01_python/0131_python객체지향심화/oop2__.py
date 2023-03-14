class Person:

    def __init__(self, name, age, money, num):
        # public
        self.name = name
        self.age = age
        # protected
        self._money = money
        # private
        self.__num = num

    def get_money(self):
        print(self._money)

    def get_num(self, password):
        if password == "1234":
            print(self.__num)
        else:
            print("비밀번호를 잘못 입력했습니다.")

p1 = Person("홍길동" , 30, "1억", "1234-1234")

print(p1.age)

# print(p1._money)
p1.get_money()

p1.get_num("1234")

# 밖에서 private 에 접근
# print(p1._Person__num)