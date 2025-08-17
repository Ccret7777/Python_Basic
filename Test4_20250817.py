# Test4_20250817

# If문
money = True
if money:
    print("택시 타고 가라")
else:
    print("걸어 가라")

busCard = 2000
card = True
if busCard >3000 or card:
    print("택시 타고 가라")
else:
    print("걸어 가라")

    
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:    # in을 활용한 if문
    print("택시 타고 가라")
elif card:               # else if와 같은 elif
    print("택시 타고 가라")
else:
    pass   # 아무것도 실행하고 싶지 않을 때 pass

score = 100
if score >= 60: print("success")
else: "failure"

# while문
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍음" % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다")
prompt = """
1. Add
2. Del
3. List
4. Quit
Enter Number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())   # 사용자에게 입력 받음
        
"""        
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다")
        coffee -= 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
    else:
        print("돈을 다시 돌려주고 커피를 주지 않는다")
        print("남은 커피 양은 %d개 입니다" % coffee)
    if coffee == 0:
        print("커피가 다 떨어져 판매를 중지")
        break    # break을 이용해 while문 조기종료
        """

# for문
li1 = ['one', 'two', 'three']
for i in li1:
    print(i)
li2 = [(1, 2), (3, 4), (5, 6)]
for (first, last) in li2:
    print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격 입니다." % number)

num = 0
for mark in marks:
    num += 1
    if mark >= 60: continue
    print("%d번 학생은 불합격 입니다." % num)

ran1 = range(0, 10) # 0~9 숫자
add = 0
for i in range(1, 11):
    add += i
print(add)

for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 합격입니다." % (number + 1))
    
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end= " ")
    print(' ')
