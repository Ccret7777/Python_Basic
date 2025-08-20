# Test6_20250820

# 클래스
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

class FourCal:
    def __init__(self, first, second):   # 생성자
        self.first = first
        self.second = second
        
    def setData(self, first, second):    # self 매개변수에는 setData매서드를 호출한 객체가 전달됨
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)
a.setData(4, 2)
print(a.first)
print(a.add())
b = FourCal(3, 7)
b.setData(3, 7)
print(b.first)

class MoreFourCal(FourCal):   # 부모 FourCal을 상속받는 자식 클래스
    def pow(self):
        result = self.first ** self.second
        return result

c = MoreFourCal(5, 6)   # 생성자를 포함해 부모의 기능들을 사용가능
print(c.add())
print(c.pow())

class SafeFourCal(FourCal):
    def div(self):    # 부모 클래스에 있는 매서드와 동일한 이름으로 만드는 것을 오버라이딩 이라고함
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

class Family:
    lastname = "김"   # 클래스 변수
print(Family.lastname)
    
        

