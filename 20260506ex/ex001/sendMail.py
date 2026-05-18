#print('회원 정보를 입력하세요.')

#userName = input('이름:')
#userMali = input('메일:')
#userId = input('아이디:')
#userPw = input('비밀번호:')

#print('------------------------------------')
#print('To.' + userMali)
#print('아이디 및 비밀번호 확인')
#print('------------------------------------')
#print(userName + ' 고객님 안녕하세요.')
#print(userName + ' 고객님의 아이디와 비밀번호는 아래와 같습니다.' )
#print('아이디: ' + userId)
#print('비밀번호: '+ userPw )
#print('감사합니다.')
#print('Naver 담당자.')
#print('------------------------------------')

userMali = 'pikasung1102@gmail.com'
print('To. pikasung1102@gmail.com')
print('To. ' + userMali)

print("이름:", "홍길동", "나이:", 20) #(*****)

print("2026", "05", "06", sep="-") #(**)

print("Hello", end=" ") #(*****)
print("world")

# f-string (가장 많이 사용)
name = "철수"
age = 25


print('이름은 ' + name +', 나이는 ' + str(age) + '입니다.')
print(f'이름은 {name}, 나이는 {age}입니다.')
