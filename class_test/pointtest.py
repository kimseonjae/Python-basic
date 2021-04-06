from class_test.ColorPoint import ColorPoint
from class_test.Point import Point

p1 = Point(10, 20)

print(p1.x, p1.y)

p1.draw()

p2 = ColorPoint('red', 30, 50)
p2.draw() #상속을 통한 부모 클래스의 함수 재사용

print(Point.count_of_instance) #클래스 변수 접근

