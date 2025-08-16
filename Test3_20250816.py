# Test3_20250816

# 집합 자료형
# C++의 unordered_set과 매우 유사, 순서가 없고, 중복 허용x
s1 = set([1, 2, 3])
print(s1)
s2 = set("Hello")
print(s2)   # 문자열 입력시 문자 하나하나 집합으로 저장 (중복 허용x)
li1 = list(s1)
print(li1)  # 인덱스 접근을 위해 set을 list로 변환
 # 교집합 구하기
s3 = set([2, 3, 4])
print(s1 & s3) 
print(s1.intersection(s3))
# 합집합 구하기
print(s1 | s3)
print(s1.union(s3))
# 차집합 구하기
print(s3 - s1)
print(s1.difference(s2))
# 값 하나 추가
s1.add(5)
# 값 여러개 추가
s1.update([6, 7, 8])
# 특정 값 제거
s1.remove(8)

# Bool 자료형
# 다른 자료형도 비어있으면 거짓이되고, 숫자는 0이 거짓
print(bool('phython'))   # True
print(bool(''))          # False

# 변수
a = [1, 2, 3]
b = a
print(id(a))
print(id(b))   # 복사를 하면 주소까지 완전히 동일
a[1] = 4
print(b)   # a값만 바꿔도 b값까지 바뀜
b[2] = 5
print(a)
# 이렇게 슬라이싱으로 해서 복사하면 a값을 바꿔도 c값은 바뀌지 않음
c = a[:]
a[1] = 6
print(c)
from copy import copy   # copy함수를 쓰기 위해 작성
d = copy(a)   # 이렇게 copy 함수를 통해 복사해도 d값은 바뀌지 않음
a[2] = 10
print(d)
num1 = 3
num2 = 5
num1, num2 = num2, num1   # 두 값 서로 바꾸기




      

