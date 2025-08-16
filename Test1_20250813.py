# Test1_20250813.py
print("Hello World")
"""
이 프로그램은 Hello World를 출력하는 프로그램이다.
"""

a = 0o177   # 8진수
b = 0xABC   # 16진수
print(a+b)

a = 2
b = 4
print(a**b) # 제곱을 나타내는 **연산자

str1 = "My name's Ccret"  # 문자열 안에 '가 있어서 "사용
str2 = 'My name is "Ccret"' # 문자열 안에 "가 있어서 '사용
str3 = '''
My name
is
Ccret
'''   # My name\nis\Ccret과 동일
str4 = """
My name
is
Ccret
"""
print(str1)
print(str2)
print(str3)
print(str4)

print(str1 * 2)  # 문자열 곱하기도 가능 ㅋ

print("="*50)
print("My Program")
print("="*50)  # C++과 다른점은... \n을 안해도 print를 할 때마다 알아서 엔터가됨..?

print(len(str2))  # 문자열 길이 구하는 함수 len

print(str2[-1])  # 뒤에서 첫번째 문자.. -로도 인덱스 접근이 가능 ㄷ 대신 -0은 0과 똑같음

print(str2[0:2]) # 슬라이싱. 0<= < 2안의 인덱스 문자

s = "20010331Rainy"
date = s[:8]   # 처음부터 8번째 전 문자까지
weather = s[8:] # 8번째 문자부터 마지막까지
print(date)
print(weather)

#문자열 포매팅
str5 = "I eat %s apples." % "five"
#숫자 포매팅
str6 = "I eat %d apples." % 3
print(str5)
print(str6)
ch1 = "banana"
str6 = "I eat %d %s." % (a, ch1)  # 변수로도 가능, 2개 대입도 가능
print(str6)
str7 = "I solve %d%%" %100
print(str7)
print("%10.4f" % 3.42134234)  # 소수점 4번째 자리까지만 출력, 전체길이가 10개인 문자열 공간에서 오른쪽 정렬

#format 함수 이용
str5 = "i eat {0} apples".format(10)
str6 = "i eat {0} oranges".format("nine")
print(str5)
print(str6)
print("i eat {0} apples and {1} oranges".format(4, "four"))
print("{0:>10}".format("hi"))   # 오른쪽 정렬
print("{0:^10}".format("hi"))   # 가운데 정렬
print("{0:!^10}".format("hi"))  # !로 공백채우기


