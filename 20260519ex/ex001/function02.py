# 지역 변수 VS 전역 변수
# 지역 변수는 함수 내부에서 선언된 변수로 함수 내부에서만 사용 가능합니다.
# 전역 변수는 함수 외부에서 선언된 변수로 함수 내/외부에서 사용 가능합니다.

'''
cannot access local variable 'num' where it is not associated with a value
'''
# num = 10

# def fun():
#     # num = 20                # 지역 변수
#     global num
#     num = num + 1             # 데이터 수정 num(전역 변수) - 10 + 1
#     print(f'num: {num}')    # 10, 전역 변수 num

# print(f'num: {num}')        # 10, 전역 변수 num

# fun()

'''
global 키워드는 함수 내에서 전역변수의 값을 '수정'하고자 할때 반드시 명시하자!
'''

# quiz) 웹사이트의 누적방문 횟수 프로그램
# 웹사이트 방문 여부를 입력받아 웹사이트의 누적 방문 횟수를 출력해봅시다

# flag = True
# totalVisitor = 0

# def countVisitor():
#     totalVisitor = 0
#     totalVisitor += 1

# while flag:
#     selectedMenuNum = int(input('1.웹사이트 방문      2. 종료'))

#     if selectedMenuNum == 1:
#         countVisitor()
#         print(f'누적 방문 횟수: {totalVisitor}')
#     else:
#         flag = False
#         print('Good bye~')

# 매개변수(*******************************************************)
# 매개: 둘 사이에서 양편의 '관계를 맺어' 줌
# 함수를 사용하기 위해 먼저 함수를 정의하고 필요할 때 호출하죠.
# 이 때 함수를 정의하는 쪽을 함수 정의부(선언부), 함수를 호출하는 쪽을 호출부라고 합니다

# 함수를 호출할 때 데이터를 넘겨줄 수 잇는데 이 데이터를 '인수'라거 합니다
# 함수 정의부는 인수를 받으면 '매개변수'라는 변수에 저장합니다. 그리고 매개변수는 지역 변수의 일종입니다.

# def greet(name, age):
#     # name = '홍길동' or '박찬호' or '박세리'
#     print(f'{name}님 안녕하세요. 나이는 {age}입니다.')

# greet('홍길동', 25)
# greet('박찬호', 20)
# greet('박세리', 30)

# def forecastWeather(temp, humi, rain):
#     print('날씨 예보입니다')
#     print(f'최고 온도: {temp}도')
#     print(f'평균 습도: {humi}도')
#     print(f'비올 확률: {rain}도')

# forecastWeather(35, 70, 80)

# 인수의 개수를 모르는 경우
# 우리 학급 학생들의 시험 점수 총합과 평균을 구하는 함수를 만들자
# 우리 학급 학생 수는 총 3명이다

# def printScoreForStudent(subject, *Scores):            # 리스트(list) > 튜플(tuple)

#     print(f'scores type: {type(Scores)}')
#     print(f'scores lengrh: {len(Scores)}')
#     totalScore = 0
#     for score in Scores:
#         totalScore += score

#     print(f'{subject}: {totalScore}')
#     averageScor = totalScore
#     print(f'{subject}: {averageScore}')

# #     totalScore = Score1 + Score2 + Score3
# #     averageScore  = totalScore / 3

# #     print(f'총합: {totalScore}')
# #     print(f'평균: {averageScore}')

# # # 90, 80, 100
# printScoreForStudent('국어', 90, 80, 100)

'''
선생님이 몇명일지 모르는 학생의 점수를 입력한다.
이떄 학생 점수의 총합과 평균을 구하는 함수를 만들고 이를 이용하는 프로그램을 만들어보자
'''

# flag = True
# studentScores = []

# def printScoreForStudent(scores):
#     if len(scores)== 0:
#         print('학생수가 0명이라 총점과 평균을 구할 수가 없습니다.')
#     else:
#         totalScore = 0
#     for score in scores:
#         totalScore += score

#     average = totalScore / len(scores)
#     print(f'총점: {totalScore}')
#     print(f'평점: {average}')

    


# while flag:
#     selectedMenuNum  = int(input('1.학생 점수 입력         2. 종료'))
#     if selectedMenuNum == 1:
#         score = int(input('학생 점수 입력: '))
#         studentScores.append(score) 
#     else:
#         # flag = False
#         break

# printScoreForStudent(studentScores)


# quiz) SMS와 MMS 구별하기
'''
문자를 보낼 때 100자 이하인 경우에는 단문 메시지(SMS)로 50원을 부과합니다. 그런데 100자를 
넘어가면 장문 메시지(MMS)로 변경되면서 100원이 부과됩니다. 단문과 장문을 구별해서 돈을 부
과하는 프로그램을 만들어봅시다. 
'''

# def sendUserMassage(str):
#     strLensth = len(str)
#     print(f'사용자가 입력한 문자 길이: {strLensth}')

#     if strLensth <= 100:
#         print(f'SMS 발송 완료!')
#         print('50분 부과!')

#     else:
#         print(f'MMS 발송 완료!')
#         print('100분 부과!')


# inputData = input('문자 입력')
# sendUserMassage(inputData)

# 인수와 매개변수의 순서가 일치하지 않을 경우
# def printMemberInfo(name, email, major, grade):
#     print(f'Name\t: {name}')
#     print(f'Email\t: {email}')
#     print(f'Major\t: {major}')
#     print(f'Grade\t: {grade}')
#     print('------------------------------------------')
# printMemberInfo("gildong@gmail.com", 'Hong Gildong',  'art', 1)

# printMemberInfo(email = "gildong@gmail.com", 
#                 name = 'Hong Gildong',  
#                 major = 'art', 
#                 grade = 1)

# def printMemberInfo(info):
#     print(f'name\t: {info[name]}')
#     print(f'email\t: {info[email]}')
#     print(f'major\t: {info[major]}')
#     print(f'grade\t: {info[grade]}')

# printMemberInfo({
#         'email':"gildong@gmail.com", 
#         'name': 'Hong Gildong',  
#         'major': 'art', 
#         'grade': 1
#     })

# 매개변수의 기본값 설정
# 직업 급여 지급 프로그램을 만들어보자!
# def setsalary(name, pay = 200):
#     print(f'{name}의 급여 {pay}원 지급!!')

# setsalary('박찬호', 400)
# setsalary('박세리', 600)
# setsalary('박용택')

# 데이터 반환(return)
# 데이터 반한이란 함수는 실행이 끝난 후에 결과물(값)을 호출부로 반환할 수 있습니다.
# 이떄 사용하는 키워드가 return입니다
# 덧셈 연산 함수를 만들어 결과를 출력하는 프로그램을 만들어보자!

# def printResuit(value):
#     print(f'resuit: {value}')

# def addFuntion(n1, n2):
#     sum = n1 + n2       # 30
#     # print(f'결괏 값: {sum}')
#     printResuit(sum)
#     return sum

# resuit = addFuntion(10, 20)
# print(f'resuit: {resuit}')

# def fun1():
#     print('2222222222222222') 
#     if DEV_MOD == True:
#         print('1111111111111111')       # 개발단계에서 디버깅 용도로만 사용한다
#         return      
#     print('3333333333333333')

# fun1()

# 별탑 만들기
# def increasestart(limitStarCount):
#     # print('*')
#     # print('**')
#     # print('***')
#     # print('****')
#     # print('*****')
#     # print('******')
#     # print('*******')
#     for n in range(1, 8):
#         print('*' * n)
#         if n == limitStarCount:
#             break

# increasestart(5)

# 7 ~ 8교시
# Toy 프로젝트 진행
'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
메뉴: 1. 회원가입   2.로그인    3.특정 회원 정보 출력   4. 모든 회원 정보 출력  99.종료
'1.사용자가 '1.'회원가입'을 선택하면 회원 ID, 회원PW, 회원Email, 회원Phone 정보를 입력받아 회원가입 진행한다.
'2.'로그인'을 선택하면 회원 ID, 회원PW를 입력받아 로그인 '성공' 또는 '실패'를 출력한다
'3.'특정 회원 정보 출력'을 선택하면 회원 ID와 회원PW를 입력받아 일치하는 회원 정보를 모두 출력한다.
'4.'모든 회원 정보 출력'을 선택하면 가입되어 있는 모든 회원 정보를 출력한다.
'99.종료'를 선택하면 프로그램 종료 시킨다.

심심하면>특정 회원의 회원 ID와 회원PW를 입력받아 인증되면 회원 정보를 수정하는 기능을 구현해보자

'''
# SIGN_UP = 1
# LOGIN = 2
# SEARCH_USER = 3
# PRINT_ALL = 4
# UPDATE_USER = 5
# EXIT = 99
# member = []
# while True: 
#     menu = int(input('메뉴: 1.회원가입   2.로그인    3.특정 회원 정보 출력   4.모든 회원 정보 출력    5.회원 정보 수정    99.종료'))
#     if menu == SIGN_UP:
#         print('회원 가입을 위해 회원님의 아이디, 비밀번호, 이메일, 전화번호를 입력해주세요.')
#         userID = input(f'회원 ID: ')
#         userPW = input(f'회원 PW: ')
#         userEmail = input(f'회원 Email: ')
#         userPhone = input(f'회원 Phone: ')
#         member.append([userID, userPW, userEmail, userPhone])
    

#     elif menu == LOGIN:
#         print('로그인해주세요.')
#         login_id = input(f'LoginID: ')
#         login_pw = input(f'LoginPW: ')
#         success = False

#         for mem in member:
#             if mem[0] == login_id and mem[1] == login_pw:
#                 print('로그인 성공!')
#                 success = True
#                 break

#         if success == False:
#             print('로그인 실패!')
                    
#     elif menu == SEARCH_USER:
#         print('특정 회원 정보 출력을 위해 ID와 PW를 입력해주세요.')
#         user_id = input(f'userID: ')
#         user_pw = input(f'userPW: ')
#         found = False

#         for mem in member:
#             if mem[0] == user_id and mem[1] == user_pw:
#                 print('회원 정보를 출력합니다.')
#                 print(f'{mem[0]}, {mem[1]}, {mem[2]}, {mem[3]}')
#                 found = True
#                 break

#             if found == False:
#                 print('일치하는 회원 정보가 없습니다.')




#     elif menu == PRINT_ALL:
#         print('모든 회원 정보를 출력합니다.')
#         for mem in member:
#             print(f'{mem[0]}, {mem[1]}, {mem[2]}, {mem[3]}')

#     elif menu == UPDATE_USER:
#         print('회원 정보 수정을 위해 아이디와 비밀번호를 입력해주세요.')
#         user_id = input(f'userID: ')
#         user_pw = input(f'userPW: ')
#         done = False

#         for mem in member:
#             if mem[0] == user_id and mem[1] == user_pw:
#                 print('인증되었습니다. 회원 정보를 수정합니다.')
#                 new_id = input(f'NewID: ')
#                 new_pw = input(f'Newpw: ')
#                 new_email = input(f'NewEmail: ')
#                 new_phone = input(f'NewPhone: ')
#                 mem[0] = new_id
#                 mem[1] = new_pw
#                 mem[2] = new_email
#                 mem[3] = new_phone
#                 print('회원 정보 수정이 완료되었습니다.')
#                 done = True
#                 break
        
#         if done == False:
#             print('인증에 실패했거나 일치하는 회원이 없습니다.')




#     elif menu == EXIT:
#         print('프로그램을 종료합니다.')
#         break

