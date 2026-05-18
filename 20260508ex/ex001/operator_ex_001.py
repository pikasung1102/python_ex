# data = int(input('수심을 입력하세요.'))
# temperrature = 20 - (data // 10 * .7)
# print(f'temperrature: {temperrature}')

# speed = input('주행 속도:')
# time = input('주행 시간:')
# distance = int(speed) * int(time)
# print(f'주행 거리: {distance}')

#퀴즈
'''
a회사는 3대의 컴퓨터로 8시간을 일하면 하루 업무를 처리할 수 있습니다.
그런데 단축 업무를 하게 되어 근무 시간이 줄게 되었다면
몇 대의 컴퓨터가 더 필요할까요?

근무 시간을 입력하면 필요한 컴퓨터 수량을 파악하는 프로그램을 만들어 봅시다.
'''
# 3 * 8 = 24
# 24 / 8 = 3
# time = int(input('근무 시간을 입력하세요'))         # 단축 근무 시간
# computer = 3 * 8 // time
# addcomputer = 1 if (3 * 8 % time) > 0 else 0

# totalcomputer = computer  + addcomputer
# print(f'필요한 컴퓨터 개수: {totalcomputer}')

#  maskPice
#  maskcut = int(input('마스크 구매 개수'))
#  totalPice = maskPice * maskcut
#  cash = int(input('지불 금액:'))
#  change = cash - totalPice
#  print(f'거스름돈 = {result}') 
    
# 13시 30분 25초를 초로 나타내시오.
# print(f'{25 + (60 * 30) + (60 * 60 * 13)}')

# 학생의 국어 영어 수학 점수를 입력하면 총점과 평균을 출력하는 프로그램을 만드시오
# kor = int(input('국어점수: '))
# eng = int(input('영어점수: '))
# mat = int(input('수학점수: '))
# totalScore = kor + eng + mat
# averageScore = totalScore / 3
# print(f'totalScore: {totalScore}')
# print(f'averageScore: {averageScore}')

# 밤 최저 기온과 낮 최고 기온을 입력하면 일교차를 출력하는 프로그램을 만드시오
# low_temp = float(input('밤 최저 기온을 입력하시오.'))
# high_temp = float(input('낮 최고 기온을 입력하시오.'))
# daily_range = high_temp - low_temp
# print('-' * 30)
# print(f'오늘의 최저 기온: {low_temp}')
# print(f'오늘의 최저 기온: {high_temp}')
# print(f'오늘의 일교차는 총 {daily_range}도 입니다')

# 사용자가 길이(cm)를 입력하면 inch로 환산하는 프로그램을 만드시오(단 1cm는 0.39inch로 한다).
cm = float(input("길이(cm)를 입력하세요: "))

inch = cm * 0.39

print(cm, "cm는", inch, "inch입니다.")