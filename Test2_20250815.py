# Test2_20250815
str1 = "Life is too short"
print(str1.split())  # 공백을 기준으로 문자열 나눔
str2 = "Life:is:too:short"
print(str2.split(':')) # : 기호를 기준으로 문자열 나눔

# 리스트 (C++의 벡터와 비슷)
list1 = [1, 2, 3, 4, 5]   # 대괄호를 이용해 나타낸 리스트
print(list1 * 3)  # *로 리스트 반복하기
print(len(list1))  # 리스트 길이(크기)
del list1[0]   # 리스트 특정값 삭제
print(list1)
del list1[2:]  # 슬라이싱 기법 활용
print(list1)
list1.append(0)  # 리스트 마지막에 0 추가
list1.sort() # 리스트 오름차순 정렬
list1.reverse()  # 리스트 내림차순 정렬
print(list1)
list1.index(2)  # 2의 인덱스는 몇인가?를 반환
list1.insert(0, 4)   # 0의 인덱스에 4 삽입
list1.remove(0)   # 첫번째로 나오는 0 삭제
list1.pop()   # 맨 마지막 요소를 return해주고 삭제
# list1.pop(2)   # 2번째 인덱스를 return 해주고 삭제
list1.count(3)  # 리스트에 3은 몇 개 있는지를 반환

# 튜플 (C++에도 tuple이 있다고 함... 첨 들음) 굳이 따지자면 const랑도 유사하다고 함
# 리스트는 []으로 둘러싸지만 튜플은 ()로 둘러쌈. 리스트는 값들을 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없음
t1 = (1, 2, 'a')   # 자료형이 달라도 됨
t2 = 4, 5, 6   # 괄호를 생략해도 됨
t3 = (1,)   # 1개의 요소만 가질 때에는 요소 뒤에 콤마를 반드시 붙여야 함

# 딕셔너리
# C++의 unordered_map과 유사하지만, C++에선 map<string, int>처럼 타입이 고정되지만, 파이썬에서는 자유
dic1 = {'name': 'pey', 'phone' : '02020202', 'birth' : '0730'}  # key: name, phone, birth, value: 나머지
dic2 = {1: 'a'}
dic2[2] = 'b'  # key 2에 value 'b'추가
dic2['name'] = 'Ccret'  # 이렇게 key, value가 이전 자료형이랑 달라도 추가 가능
dic2[3] = [1, 2, 3]  # 리스트도 value로 추가 가능
print(dic2)
print(dic2.keys())  # 딕셔너리의 key만 모아서 dict_keys 객체를 반환해줌
list2 = list(dic2.keys())
print(list2)
list3 = list(dic2.values())   # 딕셔너리의 value만 모아서 dict_values 객체를 반환해줌
print(list3)
dic2.get(1)  # 만약 1 key의 value가 없다면 none을 반환
dic2.get(1, 'bar')   # 만약 1 key의 value가 없다면 bar 을 반환




