# 연습 문제1

# 1
korean = 80
english = 75
math = 55
ave = (korean + english + math) / 3
print(ave)

# 2
if 13 % 2 == 0 : print("짝수 입니다")
else : print("홀수 입니다")

# 3, 4
pin = "881020-1068234"
print(pin[:6])
print(pin[7:])
print(pin[7])

# 5
a = "a:b:c:d"
b = a.replace(':', '#')
print(b)

# 6
li1 = [1, 3, 5, 4, 2]
li1.sort()
print(li1)
li1.reverse()
print(li1)

# 7
li2 = ['Life', 'is', 'too', 'short']
result = " ".join(li2)   # 리스트를 문자열로 만들기
print(result)

# 8
t1 = (1, 2, 3)
t1 = t1 + (4,)  # 튜플에 값 하나 추가
print(t1)

# 10
dic1 = {'A': 90, 'B': 80, 'C': 70}
result2 = dic1.pop('B')
print(dic1)
print(result2)

# 11
li3 = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
s1 = set(li3)
print(s1)
li4 = list(s1)
print(li4)







