# Test5_20250818

# 함수
def add(a, b):
    return a + b
a = 3
b = 4
c = add(a, b)
print(c)

def add_many(*args):   # 입력값의 갯수가 가변일 때 *을 붙이면 입력값을 전부 모아 튜플로 만들어줌
    result = 0
    for i in args:
        result += i
    return result
d = add_many(1, 2, 3, 4, 5)
print(d)

def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)   # *을 2개 붙이면 딕셔너리로 저장됨 key: a, value: 1

def add_and_mul(a, b):
    return a+b, a*b   # 결과값이 2개이면 값이 튜플로 해서 2개로 저장됨
result1, result2 = add_and_mul(3, 4)
print(result1, result2)

add = lambda a, b: a+b   # 람다
print(add(3, 4))

# 입력과 출력
enter = input()
print(enter)
number = input("숫자를 입력하세요: ")
for i in range(10):
    print(i, end='')


# 파일 읽고 쓰기
f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄 입니다.\n" % i
    f.write(data)   # 파일에 쓰기
f.close()
import os

print(os.getcwd())  # 파일 생성된 경로

"""
파일 열기 모드
r: 읽기 모드 - 파일을 읽기만 할 때 사용
w: 쓰기 모드 - 파일에 내용을 쓸 때 사용 (원래 파일이 있다면 기존 내용은 모두 삭제되고, 없다면 새 파일이 생성됨)
a: 추가 모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용
"""
f = open("새파일.txt", 'r')
line = f.readline()  # 파일의 첫 번째 줄을 읽어와서 출력
print(line)
f.close

f = open("새파일.txt", 'r')   # 파일의 모든 줄을 읽어와서 출력 
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f = open("새파일.txt", 'r')
data = f.read()   # 파일의 전체 내용을 문자열로 돌려줌
print(data)
f.close()

f = open("새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)       # 값을 기존 파일의 마지막에 추가
f.close()



