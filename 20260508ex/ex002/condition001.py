# 조건문 (if문)
'''
if 조건식
    실행문
'''

# num = 5
# if num > 10:
#             print('num은 10보다 크다.-----')
#                 print('num은 10보다 크다.-----')

# print('num은 10보다 크다.+++++++')

'''
if키워드: 조건문을 선언하기 위한 키워드로 '만약 ~라면의 뜻을 가지고 있다.
조건식: 특정 조건을 기술한다. 조건식의 결과에 따라 실행문의 실행 여부가 결정된다.
콜론: 코드 블록의 시작을 나타내는 것으로 콜론 이후부터가 실행될 문장이다.
실행문: 조건식의 결과가 참(True)인 경우 실행하는 명령문입니다. 
        조건식이 거짓(False)이면 실행문은 실행죄지 않는다.
'''

# 사용자가 입력한 정수가 10보다 크면 실행문을 출력하는 프로그램을 만들어 봅시다.
# num = int(input('piease input integer number'))
# if num > 10:
#     print(f'{num}은 10보다 크다')

# if num == 10:
#     print(f'{num}은 10과 같다')

# if num < 10:
#     print(f'{num}은 10보다 작다')

# 퀴즈) 속도 위반 경고하기
# 제한 속도가 50km/h인 도로에서 속도위반을 하는 자동차에 경고를 하는 프로그램을 만들어 봅시다.
# carSpeed = int(input('자동차의 현재 속도 입력: '))

# if carSpeed > 50:
#       print(f'속도 위반!!!')

# if carSpeed <= 50:
#       print(f'정상 운행~~')

# carSpeed = 40
# if carSpeed <= 50: print(f'정상 운행~~')

# num = 5
# if num > 0:
#     pass

# if ~ else 구문
# else: 그렇지 않으면~
# myScore = 70
# if myScore >= 90:
#     print('용돈 획득~')

# if myScore < 90:
#     print('빠따~')

# if myScore >= 90:
#     print('용돈 획득~')
# else:
#     print('빠따~')

# if  elif 구문    -> 다중선택
'''
점수가 90점 이상이면 'A' 출력
점수가 80점 이상 ~ 90점 미만이면 'B'출력
점수가 70점 이상 ~ 80점 미만이면 'C'출력
점수가 60점 이상 ~ 70점 미만이면 'D'출력
'''

# myScore = int(input('점수 입력'))
# if myScore >= 90:
#     print('A')
# elif (myScore >= 70) and (myScore < 80):               #70이상 80미만
#     print('C')
# elif (myScore >= 80) and (myScore < 90): 
#     print('B')
# elif (myScore >= 60)and (myScore < 70): 
#     print('D')
# else:
#     print('F')

# 퀴즈) 자동 주문 시스템 만들기
'''
다국어를 지원하는 식당에서 사용할 자동 주문 시스템을 만들고자 합니다.
1번을 누르면 한국어로, 2번을 누르면 영어로, 3번을 누르면 중국어로,
그 외 번호는 영어로 주문을 받는 프로그램을 만들어 봅시다
1.대한민국      2.USA       3.中国
1: 주문하시겠습니까?
2: wouid you like to order?
3: 您要点菜吗？
그외. wouid you like to order?
'''

# KOREA_NUMBER = 1
# USA_NUMBER = 2 
# CHINA_NUMBER = 3

# selectedNumber = int(input("1. 대한민국         2. USA 3.       中国"))
# if selectedNumber == KOREA_NUMBER:
#     print("주문하시겠습니까?")
# elif selectedNumber == USA_NUMBER:
#     print("wouid you like to order?")
# elif selectedNumber == CHINA_NUMBER:
#     print("您要点菜吗？")
# else:
#     print("Would you like to order?")

# 퀴즈 국가재난 \지언금 수령액 조회하기
'''
다음은 가구 인원수에 따른 국가재난지원금 수령액을 안내하는 프로그램입니다.
표를 참고하여 프로그램을 만들어봅시다
1인 가구:400,000원
2인 가구:600,000원
3인 가구:600,000원
4인 이상 가구:1,000,000원
'''

# family = int(input('가구 인원수를 입력하세요.'))
# if family == ONE_PERSON
#     print('400000원')
# elif family == TWO_PERSON
#     print ('600000원')
# elif family == THREE_PERSON
#     print ('800000원')
# else:
#     print ('1000000원')

'''
다음 요구사항을 충족하는 프로그램을 if~elif문을 이용해서 만드시오
-BMI 지수를 입력한다
-BMI 지수가 90 이하면 '저채중'을 출력한다
-BMI 지수가 90 초과~110이하면 '정상체중'을 출력한다
-BMI 지수가 110 초과~120이하면 '과체중'을 출력한다
-BMI 지수가 120 초과~140이하면 '비만'을 출력한다
-BMI 지수가 140 초과면 '고도비만'을 출력한다
'''

#  bmi = int(input('BMI지수를 입력하시오.'))
#  if BMI <= 90:
#     print('저채중') 
#  elif BMI > 90 and bmi <= 110:
#     print('정상채중')
#  elif BMI > 110 and bmi <= 120:
#     print('과채중')
#  elif BMI > 120 and bmi <= 140:
#     print('비만')

#  else:
#   print('고도비만')

# 중첩 조건문
# 조건문 내에 또 다른 조건문을 쓸 수 았는데 이를 중첩 조건문이라고 한다
# 사용자가 입력한 정수에서 양수(0도 포함)인지를 판단하고 양수라면 홀/짝인지 구분하자

# myInteger = int(input('정수 입력'))
# if myInteger > 0:
#     if myInteger % 2 == 0:
#         print('짝수!')
#     else:
#         print('홀수!')
# else:
#     print('음수!')


# 퀴즈 짝수 홀수를 판별하는 프로그램을 만들어
# num = int(input('사용자야~~ 양의 점수 입력해주라~'))
# if num >= 0:
#     if num % 2 == 0:
#         print('짝수!!')
#     else:
#         print('홀수!!')


# else:
#     print('입력한 점수는 0또는 음수입니다')

# 퀴즈
'''
출생연도 끝자리(endBirthYear)와 나이(age)를 입력하면 다음 요구 사항에 맞춰
마스크 구매 가능한 용일을 출력하는 프로그램을 만드시오.
-1,6 => 월
-1,6 => 화
-1,6 => 수
-1,6 => 목
-1,6 => 금
-만 65세 이상 어르신은 언제든지 구매 가능
'''

# endBirthYear = int(input('출생연도 끝자리 입력'))
# age = int(input('나이 입력'))

# if age < 65:
#     if endBirthYear == 1 or endBirthYear == 6:
#         print('월요일에 구매 가능합니다')
#     elif endBirthYear == 2 or endBirthYear == 7:
#         print('화요일에 구매 가능합니다')
#     elif endBirthYear == 3 or endBirthYear == 8:
#         print('수요일에 구매 가능합니다')
#     elif endBirthYear == 4 or endBirthYear == 9:
#         print('목요일에 구매 가능합니다')
#     elif endBirthYear == 5 or endBirthYear == 10:
#         print('금요일에 구매 가능합니다')

# else:
#     print('언제나 구매 가능합니다.')

# # 날짜 관련 모듈: datetime
# from datetime import datetime

# #  현재 일 구하기
# print(datetime.todey().weekday())       #4 (0:월 1: 화 2: 수:3 목:4 금 

# from datetime import datetime
# dayNum = datetime.today().day

# carNum = int(input("차량 번호 4자리를 입력하세요. "))

# print(f'오늘 날짜 : {dayNum}일')

# if dayNum & 2 == 0:
#     print('오늘 입차: 번호가 짝수인 차량')
# else:
#     print('오늘 입차: 번호가 짝수인 차량')

# if dayNum % 2 == carNum % 2:
#     print('귀하의 차량은 입차 가능합니다')

# else:
#     print('귀하의 차량은 입차 불가합니다')
import time
time = int(input('최초 장비를 사용하기까지 걸린 시간(초)를 입력하세요'))
if time <= 60:
   survival_rate = '85%'
elif time <= 120:
   survival_rate = '76%'
elif time <= 180:
   survival_rate = '66%'
elif time <= 240:
   survival_rate = '57%'
elif time <= 300:
   survival_rate = '47%'
else:
    survival_rate = '47%'
print(f'생존율 : {survival_rate}')



