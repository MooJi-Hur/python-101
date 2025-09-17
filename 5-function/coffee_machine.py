# pass   # 함수 골격은 만들어두었고, 내용을 당장 사용하지는 않을 때 사용하는 키워드, 존재하지만 기능은 없는 함수


def coffee(quantity, price):
    change = price - (quantity * 200)

    if change >= 0:
        show(quantity, change)
    else:
        show()


def show(quantity=0, change=0):
    if quantity == 0 & change == 0:
        print("금액이 부족합니다. ")
    else:
        print(f"커피 {quantity}잔과 잔돈 {change}원이 나왔습니다. ")

def start():
    my_quantity = int(input("커피 몇 잔이 필요하신가요?"))
    my_price = int(input("금액을 넣어주세요. 1잔에 200원"))

    coffee(my_quantity, my_price)

