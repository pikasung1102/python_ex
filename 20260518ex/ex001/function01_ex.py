goods = {
    '새우깡': 1200,
    '비비빅':  400,
    '초코파이':  500,
    '맛동산': 1500
}

totalPrice = 0

def shrimpCrackerPrice():
    global totalPrice 
    totalPrice += goods['새우깡'] * shrimpCrackers
    print(f'새우깡 구매 금액: {goods['새우깡'] * shrimpCrackers}원')
def BibibigPrice():
    global totalPrice
    totalPrice += goods['비비빅'] * Bibibig
    print(f'비비빅 구매 금액: {goods['비비빅'] * Bibibig}원')
def ChocoPiePrice():
    global totalPrice
    totalPrice += goods['초코파이'] * ChocoPie
    print(f'초코파이 구매 금액: {goods['초코파이'] * ChocoPie}원')
def MatdongsanPrice():
    global totalPrice
    totalPrice += goods['맛동산'] * Matdongsan
    print(f'맛동산 구매 금액: {goods['맛동산'] * Matdongsan}원')

shrimpCrackers = int(input('새우깡 구매 개수'))
Bibibig = int(input('비비빅 구매 개수'))
ChocoPie = int(input('초코파이 구매 개수'))
Matdongsan = int(input('맛동산 구매 개수'))

print(f'새우깡 구매 개수: {shrimpCrackers}')
print(f'비비빅 구매 개수: {Bibibig}')
print(f'초코파이 구매 개수: {ChocoPie}')
print(f'맛동산 구매 개수: {Matdongsan}')
print('=' * 40)
shrimpCrackerPrice()
BibibigPrice()
ChocoPiePrice()
MatdongsanPrice()
print('=' * 40)
print(f'총 구매 금액: {totalPrice}원')