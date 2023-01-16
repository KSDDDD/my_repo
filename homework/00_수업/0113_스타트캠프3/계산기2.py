while True:
    a = int(input("N1 :"))
    b = int(input("N2 :"))

    op = input("연산자 :")

    if a == b == 0:
        print("0")
        break

    if op == "+":
        print("값 :", a+b)
    if op == "-":
        print("값 :", a-b)
    if op == "*":
        print("값 :", a*b)
    if op == "/":
        print("값 :", a/b)

   
    # if op != "+" or op != "-" or op != "*" or op != "/":
    #      while True:

    #         print("다시 입력해 주세요")
    #         break  