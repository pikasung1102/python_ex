# 반복문(for문 & while문)

# for문: ~ 하는 동안 ==> 회수에 의한 반복
'''
for 변수 in 범위:
    실행구문
'''
# 1~10까지의 정수를 출력(1, 3, 5, 7, 9)
# 1 ~ n까지의 정수 range(1, (n+1), 1)
# for num in range(1, 11, 1):
#     print(f'{num} : hello')
#     print(f'hello')



# 0부터 10까지의 정수를 출력
# for num in range(0, 11, 1):
#     print(f'num: {num}')

# # range() 간략화 - 단계가 1인 경우 단계를 생략할 수 있다
# for num in range(0, 11):
#     print(f'num: {num}')

    # range() 간략화 - 단계가 생략되고 시작이 0이면 시작도 생략할 수 있다
# for num in range(11):   # == range(0, 11, 1)
#     print(f'num: {num}')


# quiz 2~8 사이에 짝수 출력하기
# for num in range(2, 9, 2):
#     print(f'num: {num}')
    

# for num in range(1, 16):
#     if (num <= 8) and (num % 2 == 0):
#             print(f'num: {num}')

# quiz) 사용자가 입력한 횟수 만큼 '메일 발송!' 문자열 출력하기
# count = int(input('메일을 몇번 발송할까요?'))
# for num in range(count):
#     print(f'{num}번 메일발송!')

# 1~10 사이의 정수를 출력하되, 정수가 3의 배수이면 '3의 배수!' 출력하기
# for number in range(1, 11):
#     if number % 3 == 0:
#         print(number, '3의 배수!')
        
#     else:print(number)

# 사용자가 원하는 구구단을 입력하면 해당 구구단을 츨력하자!
# print("--- 구구단 프로그램을 시작합니다 ---")
# userInputData = int(input("출력하고 싶은 단을 입력하세요."))

# for i in range(1, 10):
#    resultStr = (f"{userInputData} x {i} = {userInputData * i}")
#    print(resultStr)

# quiz) 1~10까지의 정수의 합 출력하기
# total = 0
# for number in range(1, 11):
#     total += number

# print("-" * 30)
# print(f"1부터 10까지의 합:{total}")
# print("-" * 30)

# quiz) for문을 이용해서 1~100까지의 정수 중에서
# 3과 7의 공배수와 최소공배수를 출력하시오.
# result = []

# for num in range(1, 101):
#     if num % 3 == 0 and num % 7 == 0:
#         result = result + [num]
#         if len(result) == 1:
#             print(f"최소공배수: {num}")

# print(f"3과 7의 공배수들: {result}")

# range() 함수 정리


# 문자열을 이용한 for문 (****)
'''
지금까지 이터러블에 range() 함수를 이용한 예를 살펴봤습니다.
그런데 이터러블에는 다음과 같이 문자열도 이용할 수 있습니다.
'''


# for ch in 'hel            lo':
#     print(f'ch: {ch}')

# 50보다 작은 7의 배수를 출력하는 프로그램을 만드시오.
# for num in range(1, 51):
#     if num % 7 == 0:
#         print(f'num: {num}')


# while문: ~ 하는 동안 ==> 조건에 의한 반복
# num = 1

# while num <= 10:
#     print(f'num: {num}')
#     num += 2

# quiz) 1~30까지의 정수 중 홀수와 짝수를 구분하여 출력하기

# for num in range(1, 31):
    # pass
# num = 1

# while num < 31:   
#     if num % 2 == 0:
#         print(f'{num}은 짝수!')
#     else:
#         print(f'{num}은 홀수!')

#     num += 1 

# quiz) 구구단 3단 출력하기 by whlie문
# num = 1
# while num <= 9:
#     print(f'3 * {num} = {3 * num}')
#     num = num + 1

# quiz) 구구단 전체(2단 3단 4단 .... 9단)
# num2 = 2
# while num2 <= 9:
#     num1 = 1

#     while num1 <= 9:
#         print(f'{num2} * {num1} =  {num2 * num1}')
#         num1 = num1 + 1

#     print()
#     num2 = num2 + 1

# num1 = 1
# while num1 <= 9:
#     num2 = 2
#     while num2 <= 9:
#         print(f'{num2} * {num1} = {num2 * num1:2d}', end=' | ')
#         num2 = num2 + 1
#     print()
#     num1 = num1 + 1

# num1 = 1
# while num1 < 10:

#     num2 = 2
#     str = ''
#     while num2 < 10:
#         str += f'{num2} X {num1} = {num2 * num1}\t' 
#         num2 += 1
        
#     print(str)
#     num1 += 1

# quiz) whlie문과 if문을 이용해서 0~100까지 정수 중 3과 8의 공배수와 최소공배수 출력하기
# num = 1     # 반복문의 시작(초기값)
# minNum = 0  # 최소공배수

# while num <= 100:

#     if num % 3 == 0 and num % 8 == 0:
#         print(f'3과 8의 공배수: {num}')     # 공배수 출력

#         if minNum == 0:
#             minNum = num                  # 24

#     num += 1

# print(f'3과 8의 최소공배수: {minNum}')

# 반복문 내 실행 제어(continue, break)
# continue:
# 빈복문에 continue 키워드를 사용하면 이후 '실행을 생략하고 다시 반복문의 처음'으로 돌아갑니다.
# continue를 이용해서 1부터 10까지 정수 중 홀수만 출력하는 프로그램을 만들어 봅시다.
# for num in range(1,11):
#     if num % 2 == 0:
#         continue
#     print(f'num: {num}')

# count = 1
# for num in range(10)







# break:
# 반복문에서 break 키워드를 만나면 '실행을 중단하고 반복문을 빠져'나옵니다.
# 1부터 10까지 정수를 더하되, 결과가 30 이상이 될때 정수를 찾는 프로그램을 만들어 봅시다.

# num = 1
# sum = 0

# while num < 11:
#     sum += num
#     if sum >= 30:
#         print(f'num: {num}')
#         break        # 8
#     num += 1

# for ~ else 키워드
'''
for문에 else 키워드를 사용하는 경우, else 이하의 구문은 for문의 반복 업무를 모두 완료하고
난 후 실행됩니다.
'''

# 1부터 5까지 정수를 출력하고 빈복문이 끝나면 완료 메세지를 출력하자
for num in range(1, 6)
    print(f'num: {num}')

print('완료!')

# pass 키워드
for num in range(1, 10):
    pass

# quiz
'''
삼각형의 넓이 구하기
가로와 세로 길이의 변화에 따른 삼각형의 넓이를 구하는 프로그램을 만들어보자
단, 가로 길이는 1부터 2의 배수로 증가하고
세로 길이는 1부터 3의 배수로 증가하며,
삼각형의 넓이가 150보다 크면 프로그램을 종료한다.
'''

count = 1
maxArea = 150

while True:
    resuit = ((count * 2) * (count * 3)) / 2
    if resuit > 150: break
    print(f'삼각형의 넓이는: {resuit}')
    count += 1
