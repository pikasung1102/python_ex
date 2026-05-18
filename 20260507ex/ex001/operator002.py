


#할당연산자(=)
num = 5

#복합대입 연산자
#num = num + 5
num += 5

#num = num - 5
num -= 5

#num = num * 5
num *= 5

#num = num / 5
num /= 5

#num = num % 5
num %= 5

#num = num // 5
num //= 5

#num = num ** 5
num **= 5





#길동이가 500만원 씩 5년 만기인 정기 예금 상품에 가입했을 때
#5년 후 받을 총 수령액을 게산해봅시다(이자율 연 5%)

myMomey = 5000000
rate = 0.05

# 1년 후 총 금액
myMomey + (myMomey * rate)

# 2년 후 총 수령액 
myMomey = myMomey + (myMomey * rate )

# 3년 후 총 수령액 
myMomey = myMomey + (myMomey * rate )

# 4년 후 총 수령액 
myMomey = myMomey + (myMomey * rate )

# 5년 후 총 수령액 
myMomey = myMomey + (myMomey * rate )

print(f'5년 후 총 수령액: {int(myMomey):,}원')