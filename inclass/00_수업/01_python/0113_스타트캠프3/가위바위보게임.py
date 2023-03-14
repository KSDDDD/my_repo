import random

user = input()

com = random.choice(["가위", "바위", "보"])

winner = ""

if user == "가위":
    if com == "가위":
        print(f"나 : {user} / 컴퓨터 : {com}")
        print("무승부")
    elif com == "바위":
        print(f"나 : {user} / 컴퓨터 : {com}")
        print("패배")
    else:
        print(f"나 : {user} / 컴퓨터 : {com}")
        print("승리")       
elif user == "바위":
    if com == "가위":
        print(f"나 : {user} / 컴퓨터 : {com}")
        print("승리")
    elif com == "바위":
        print(f"나 : {user} / 컴퓨터 : {com}")
        print("무승부")
    else:
        print(f"나 : {user} / 컴퓨터 : {com}")
        print("패배")    
else:
    if com == "가위":
        print(f"나 : {user} / 컴퓨터 : {com}")
        print("패배")
    elif com == "바위":
        print(f"나 : {user} / 컴퓨터 : {com}")
        print("승리")
    else:
        print(f"나 : {user} / 컴퓨터 : {com}")
        print("무승부")    