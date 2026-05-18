# 데이터 입력(input data)
# input()

'''
print('데이터를 입력하세요.')
inputdata = input()
print(inputdata)
'''
'''
print('정수를 입력하세요.')
inputInteger = input() #6
print(inputInteger) #6
print(type(inputInteger)) #int
'''
'''
print('실수 입력하세요.')
inputFloat = input() #3.14
print(inputFloat) #3.14
print(type(inputFloat)) #syr
'''
'''
print('논리형 데이터 입력하세요.', end='') # 논리형 데이터 입력하세요. (자동개행)
inputBoolean = input #True
print(inputBoolean) #True
print(type(inputBoolean)) # str
'''


# inputBoolean = input('논리형 데이터 입력하세요.\n')       # Thre
# print(inputBoolean) 
# # print(type(inputBoolean)) # str

'''
# wkfy(data) 형을 변황해야 합니다. data type casting
userInputData = input('사용자야~~~~ 정수 입력해라~') # 10
print(userInputData) # 10
print(type(userInputData)) # str
userInputData = int(userInputData) # str --> int
print(type(userInputData)) # int
'''
# str -> boolean
# userInputDatainput = input('True or False 입력하세요.')
# print(userInputData) # True
# print(type(userInputData)) # str
# userInputData = bool(userInputData)
# print(type(userInputData))


# str -> float
# userInputData = input('실수 입력하세요.')
# print(userInputData)
# print(type(userInputData))
# userInputData = float(userInputData)
# print(type(userInputData))

# userInputData = 'True'
# userInputData = bool(userInputData)
# print(type(userInputData))

# x = 3
# y = float(x)
# print(y)

x = 3.141592
y = int(x)
print(y)
print(float(y))
