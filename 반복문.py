#for반복문(특정횟수로 반복 제어)
fruits = ['사과', '바나나', '딸기']
for fruit in fruits :
    print('이는 첫번째 코드블록 라인입니다. ', fruit)
print('이는 for 반복문의 코드블록 밖입니다.')

dic = {'과일':'사과', '숫자':1, '이름':'장영수'}
for a in dic :
    print(a, dic[a])
dic = {'봄':'숭어', '여름':'덥죠', '숫자':3}
for var in dic :
    print(var, dic[var])

# a = list(range(1,11))
# print(a)

string = "오늘은 너무 덥네요. 빨리 집에 가고 싶어요."
for s in string :
    print(s)




