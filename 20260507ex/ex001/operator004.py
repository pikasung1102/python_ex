# 논리 연산자
# 논리 연산자 피연산자의 논리 자료형을 

# and 연산자
# and는 그리고 라는 뜻으로
# 피연산자가 모두 True 인 경우에만 True입니다.
# 피연산자가 하나라도 False이면 결과는 False
#var1 = True
#var2 = True
#print(var1 and var2)

#var1 = True
#var2 = False
#print(var1 and var2)

#var1 = False
#var2 = False
#print(var1 and var2)
#print(f'var1 & var2: {var1 & var2}')

#or 연산자
# or은 또는 이라는 뜻으로 피연산자 중 하나라도 True라면 True가 됩니다
#var1 = True
#var2 = True
#print(var1 or var2)

#var1 = True
#var2 = False
#print(var1 or var2)

# var1 = False
# var2 = False
# print(var1 or var2)
# print(f'var1 | var2: (var1 | var2)')
# # not 연산자
# # not은 부정이라는 뜻으로 피연산자의 현재 상태를 부정하는 연산자입니다
# # 피연산자가 True이면 결과로 False를 출력하고 False이면 True를 출력합니다
# var1 = True
# print(not var1)

# var1 = False
# print(not var1)
# print(f'var1 ~ var2: {~var1 ~ var2}')

# # quiz
# num1 = 10; num2 = 20; num3 = 30
# result = (num1 < num3) and (num2 < num3) 
# print(f'result: {result}')

# result = (num1 > num3) and (num2 < num3)
# print(f'result: {result}')

# result = (num1 < num3) and (num2 > num3)
# print(f'result: {result}')

# num1 = 10; num2 = 20; num3 = 30
# result = (num1 < num3) and (num2 < num3) and (num3 > num1)
# print(f'result: {result}')



# print('-------------------------------------')
# print(5 or 6)
# print(5 | 6)


# # and, or 연산시 주의사항
# # and 연산자는 모든 

# num1 = 10; num2 = 20
# result = (num1 < 15) and (num2 > 15)

# num1 = 17; num2 = 20
# result = (num1 < 15) and (num2 > 15)



# num1 = 10
# print(f'num1: {num1}')
# print(abc)            

# print((num1 > 5) or abc)

# 퀴즈
# 어린이날 범퍼카 탑승 가능
# dw 놀이동산은 어린이영 범퍼카의 사용기준을 신장이 120cm ㅣ상이고 170cm 미만인 어린이
# 라고 규정하였습니다. 어린이용 범퍼카를 탑승할 수 있는지 여부를 알려주는 프로그램을 만들어봅
#시다(탑승 가능은 true , 찹승 불가능은 False를 출력합니다).

# height = int(input('어린이의 신장을 입력하세요.'))
# result + (height >= 120) and (height < 170)
# printf(f'result: {result}')

# 조건식 == 삼향 연산자
num1 = 10       # 이향 연산자
num1 = 10 - 6   # 이향 연산자
not True        # 단항 연산자

targescore = 90
myscore = 95
# myscore가 targescore보다 크거나 같으면 합격! 그렇지 않으면 불합격
result + '합격' if myscore >= targescore else '불합격'
print(f'result --------------------------> {result}')

# 퀴즈
# dw 마트는 


incomig = int(input('수입:'))
outgoing = int(input('지출:'))
result = '흑자' if incomig > outgoing else '적자'
print(f'result: {result}')

# 조명장치 on/off 프로그램 만들기
currentLight = 58
targetLight = 60
result = 'Thrn on' if currentLight < targetLight else 'Turn off'
print(f'result: {result}')

